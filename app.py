import datetime
import os
import re
from urllib.parse import urlparse

from flask import Flask, jsonify, request, send_from_directory, session

from education import HELP_MESSAGE, SUBJECTS, WELCOME_MESSAGE

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_HTTPONLY"] = True


def normalize_text(text):
    return re.sub(r"\s+", " ", str(text).strip().lower())


def has_phrase(text, phrases):
    for phrase in phrases:
        pattern = r"(?<!\w)" + re.escape(phrase) + r"(?!\w)"
        if re.search(pattern, text):
            return True
    return False


def answer_math(user_input):
    cleaned = user_input.replace(" ", "")
    if not re.fullmatch(r"[0-9+\-*/().]+", cleaned):
        return None

    try:
        result = eval(cleaned, {"__builtins__": {}}, {})
    except Exception:
        return None

    return f"Javob: {result}"


def detect_subject(text):
    for key, subject in SUBJECTS.items():
        if has_phrase(text, subject["keywords"]):
            return key
    return None


def find_faq_answer(text, subject_key=None):
    keys = [subject_key] if subject_key else list(SUBJECTS.keys())

    for key in keys:
        for item in SUBJECTS[key]["faq"]:
            if has_phrase(text, item["keywords"]):
                return key, item["answer"]

    return None, None


def build_subject_overview(subject_key):
    subject = SUBJECTS[subject_key]
    summary = subject["summary"]

    lines = [
        subject["title"],
        f"Ta'rif: {subject['intro']}",
        "",
        "Asosiylar:",
        *summary["core"],
        "",
        "Formulalar:",
        *summary["formulas"],
        "",
        "Qo'llanish:",
        *summary["applications"],
    ]
    return "\n".join(lines)


def build_subject_formula_sheet(subject_key):
    subject = SUBJECTS[subject_key]
    formulas = "\n".join(subject["summary"]["formulas"])
    return f"{subject['title']} formulalari:\n{formulas}"


def build_faq_entry_payload(item):
    label_source = next(
        (keyword for keyword in item["keywords"] if "nima" not in keyword.lower()),
        item["keywords"][0],
    )
    term = re.sub(r"\s+nima\??$", "", label_source.strip(), flags=re.IGNORECASE)
    term = term[:1].upper() + term[1:] if term else "Atama"
    return {
        "term": term,
        "question": f"{term} nima?",
        "answer": item["answer"],
    }


def build_subject_fast_answer(user_input):
    normalized = normalize_text(user_input)
    subject_key = detect_subject(normalized)
    matched_subject, faq_answer = find_faq_answer(normalized, subject_key)

    if faq_answer:
        return f"{SUBJECTS[matched_subject]['title']}: {faq_answer}"

    if subject_key:
        if has_phrase(normalized, ["formula", "formulalar", "formula kerak"]):
            return build_subject_formula_sheet(subject_key)
        return build_subject_overview(subject_key)

    return None


def get_quiz_state():
    return session.get("quiz_state")


def clear_quiz_state():
    session.pop("quiz_state", None)
    session.modified = True


def quiz_question_payload(state):
    subject = SUBJECTS[state["subject"]]
    current = subject["quiz"][state["index"]]
    return {
        "subject": state["subject"],
        "subject_title": subject["title"],
        "index": state["index"] + 1,
        "total": len(subject["quiz"]),
        "score": state["score"],
        "awaiting_next": state["awaiting_next"],
        "question": current["question"],
        "options": current["options"],
    }


def quiz_state_payload(message=None):
    state = get_quiz_state()
    if not state:
        return {"active": False, "message": message or "Test boshlanmagan."}

    payload = quiz_question_payload(state)
    payload["active"] = True
    if message:
        payload["message"] = message
    return payload


def start_quiz(subject_key):
    session["quiz_state"] = {
        "subject": subject_key,
        "index": 0,
        "score": 0,
        "awaiting_next": False,
    }
    session.modified = True
    return quiz_state_payload("Test boshlandi.")


def submit_quiz_answer(answer):
    state = get_quiz_state()
    if not state:
        return {"active": False, "message": "Avval testni boshlang."}, 400

    if state["awaiting_next"]:
        payload = quiz_state_payload("Oldin `Keyingi savol` ni bosing.")
        payload["feedback"] = "Bu savol allaqachon tekshirilgan."
        return payload, 200

    subject = SUBJECTS[state["subject"]]
    current = subject["quiz"][state["index"]]
    correct_answer = current["answer"]
    is_correct = answer.upper() == correct_answer

    if is_correct:
        state["score"] += 1

    state["awaiting_next"] = True
    session["quiz_state"] = state
    session.modified = True

    payload = quiz_state_payload()
    payload["feedback"] = "To'g'ri." if is_correct else f"Noto'g'ri. To'g'ri javob: {correct_answer}."
    payload["explanation"] = current["explanation"]
    payload["answered"] = True
    payload["correct_answer"] = correct_answer
    payload["is_correct"] = is_correct

    if state["index"] == len(subject["quiz"]) - 1:
        final_score = state["score"]
        total = len(subject["quiz"])
        clear_quiz_state()
        payload["active"] = False
        payload["completed"] = True
        payload["final_score"] = final_score
        payload["total"] = total
        payload["message"] = f"Test tugadi. Natija: {final_score}/{total}."

    return payload, 200


def next_quiz_question():
    state = get_quiz_state()
    if not state:
        return {"active": False, "message": "Avval testni boshlang."}, 400

    if not state["awaiting_next"]:
        payload = quiz_state_payload("Javobni A, B, C yoki D dan tanlang.")
        return payload, 200

    state["index"] += 1
    state["awaiting_next"] = False
    session["quiz_state"] = state
    session.modified = True
    return quiz_state_payload("Keyingi savol."), 200


def subject_list_payload():
    return [
        {
            "key": key,
            "title": subject["title"],
            "intro": subject["intro"],
            "quick_faq": [build_faq_entry_payload(item) for item in subject["faq"][:3]],
            "terms": [build_faq_entry_payload(item) for item in subject["faq"]],
        }
        for key, subject in SUBJECTS.items()
    ]


def generate_response(user_input):
    normalized = normalize_text(user_input)

    if not normalized:
        return "Xabar bo'sh."

    if has_phrase(normalized, ["salom", "assalomu alaykum", "hello", "hi"]):
        return f"{WELCOME_MESSAGE}\n\n{HELP_MESSAGE}"

    if has_phrase(normalized, ["fanlar", "mavzular", "yordam", "menu", "nima qila olasan"]):
        return HELP_MESSAGE

    if has_phrase(normalized, ["vaqt", "soat", "time", "sana", "date"]):
        now = datetime.datetime.now()
        return f"Hozir {now.strftime('%H:%M')}. Bugun {now.strftime('%d.%m.%Y')}."

    subject_answer = build_subject_fast_answer(user_input)
    if subject_answer:
        return subject_answer

    math_answer = answer_math(normalized)
    if math_answer:
        return math_answer

    return (
        "Men 3 fan bo'yicha ishlayman.\n"
        "SI\n"
        "Ehtimollik va statistika\n"
        "Differensial tenglamalar\n"
        "Fan nomini yozing, men darrov tayyor konspekt chiqaraman."
    )


@app.after_request
def add_cors_headers(response):
    origin = request.headers.get("Origin", "")
    parsed_origin = urlparse(origin) if origin else None
    is_local_origin = parsed_origin and parsed_origin.scheme in {"http", "https"} and parsed_origin.hostname in {
        "127.0.0.1",
        "localhost",
    }

    if is_local_origin:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"

    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/")
def home():
    return send_from_directory(app.root_path, "index.html")


@app.route("/styles.css")
def styles():
    return send_from_directory(app.root_path, "styles.css")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "backend-ready"})


@app.route("/subjects", methods=["GET"])
def subjects():
    return jsonify({"subjects": subject_list_payload()})


@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return ("", 204)

    payload = request.get_json(silent=True) or {}
    user_input = str(payload.get("message", "")).strip()
    if not user_input:
        return jsonify({"reply": "Xabar bo'sh"}), 400

    return jsonify({"reply": generate_response(user_input)})


@app.route("/quiz/state", methods=["GET"])
def quiz_state():
    return jsonify(quiz_state_payload())


@app.route("/quiz/start", methods=["POST", "OPTIONS"])
def quiz_start():
    if request.method == "OPTIONS":
        return ("", 204)

    payload = request.get_json(silent=True) or {}
    subject_key = str(payload.get("subject", "")).strip().lower()
    if subject_key not in SUBJECTS:
        return jsonify({"active": False, "message": "Fan topilmadi."}), 400

    return jsonify(start_quiz(subject_key))


@app.route("/quiz/answer", methods=["POST", "OPTIONS"])
def quiz_answer():
    if request.method == "OPTIONS":
        return ("", 204)

    payload = request.get_json(silent=True) or {}
    answer = str(payload.get("answer", "")).strip().upper()
    if answer not in {"A", "B", "C", "D"}:
        return jsonify({"active": True, "message": "Faqat A, B, C yoki D yuboring."}), 400

    body, status_code = submit_quiz_answer(answer)
    return jsonify(body), status_code


@app.route("/quiz/next", methods=["POST", "OPTIONS"])
def quiz_next():
    if request.method == "OPTIONS":
        return ("", 204)

    body, status_code = next_quiz_question()
    return jsonify(body), status_code


@app.route("/quiz/stop", methods=["POST", "OPTIONS"])
def quiz_stop():
    if request.method == "OPTIONS":
        return ("", 204)

    clear_quiz_state()
    return jsonify({"active": False, "message": "Test yopildi."})


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000, use_reloader=False)
