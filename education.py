WELCOME_MESSAGE = (
    "Assalomu alaykum. Men SI, Ehtimollik va statistika, "
    "Differensial tenglamalar bo'yicha savol-javob va test o'tkazadigan o'quv chatbotman."
)

HELP_MESSAGE = (
    "Mavjud fanlar: SI, Ehtimollik va statistika, Differensial tenglamalar.\n"
    "Namuna so'rovlar:\n"
    "- SI haqida qisqacha tushuntir\n"
    "- Ehtimollikda dispersiya nima?\n"
    "- Differensial tenglama turlari\n"
    "- SI bo'yicha test boshlash\n"
    "- Ehtimollik test\n"
    "Testda javobni A, B, C yoki D ko'rinishida yuboring."
)

SUBJECTS = {
    "si": {
        "title": "Sun'iy intellekt",
        "keywords": [
            "si",
            "suniy intellekt",
            "sun'iy intellekt",
            "artificial intelligence",
            "ai",
        ],
        "intro": (
            "Sun'iy intellekt ma'lumotni tahlil qilib, qaror qabul qilish, "
            "tasniflash, bashorat qilish va matn yaratish kabi vazifalarni bajaradigan tizimlar sohasidir."
        ),
        "summary": {
            "core": [
                "Ta'rif: kompyuterning aqlli vazifalarni bajarish sohasi.",
                "Asosiy bo'limlar: machine learning, deep learning, NLP, computer vision.",
                "Vazifalar: klassifikatsiya, regressiya, tavsiya, generatsiya, bashorat.",
                "Muhim muammo: overfitting bo'lsa model yangi data da yomon ishlaydi.",
            ],
            "formulas": [
                "Accuracy = to'g'ri javoblar / jami javoblar",
                "Loss model xatosini o'lchaydi va treningda kamaytiriladi",
            ],
            "applications": [
                "Tibbiyotda diagnostika",
                "Bankda fraud aniqlash",
                "Chatbot va tarjimada matn ishlash",
            ],
        },
        "faq": [
            {
                "keywords": ["machine learning", "mashinali oqitish", "mashinali o'qitish"],
                "answer": (
                    "Mashinali o'qitish SI ning bo'limi bo'lib, model tayyor qoidalardan ko'ra "
                    "ma'lumotdan qonuniyatlarni o'rganadi."
                ),
            },
            {
                "keywords": ["deep learning", "chuqur oqitish", "chuqur o'qitish", "neyron tarmoq"],
                "answer": (
                    "Deep learning ko'p qatlamli neyron tarmoqlarga tayangan usul bo'lib, "
                    "rasm, ovoz va matn kabi murakkab ma'lumotlarda yaxshi ishlaydi."
                ),
            },
            {
                "keywords": ["supervised", "nazoratli oqitish", "nazoratli o'qitish"],
                "answer": (
                    "Nazoratli o'qitishda kirish ma'lumotlari bilan birga to'g'ri javob ham beriladi, "
                    "model esa shu juftliklardan o'rganadi."
                ),
            },
            {
                "keywords": ["unsupervised", "nazoratsiz oqitish", "nazoratsiz o'qitish"],
                "answer": (
                    "Nazoratsiz o'qitishda yorliq bo'lmaydi. Model ma'lumot ichidagi yashirin "
                    "guruhlar, tuzilmalar va o'xshashliklarni topadi."
                ),
            },
            {
                "keywords": ["overfitting", "ortiqcha moslashish"],
                "answer": (
                    "Overfitting modelning trening ma'lumotini juda yaxshi yodlab olib, "
                    "yangi ma'lumotlarda yomon ishlash holatidir."
                ),
            },
            {
                "keywords": ["classification", "klassifikatsiya", "tasniflash"],
                "answer": (
                    "Klassifikatsiya obyektni oldindan berilgan sinflardan biriga ajratish vazifasidir. "
                    "Masalan, email spam yoki oddiy xat ekanini topish."
                ),
            },
            {
                "keywords": ["regression", "regressiya"],
                "answer": (
                    "Regressiya uzluksiz qiymatni bashorat qiladi. Masalan, narx, harorat yoki talab hajmini topish."
                ),
            },
            {
                "keywords": ["training data", "trening data", "oquv malumotlari", "o'quv ma'lumotlari"],
                "answer": (
                    "O'quv ma'lumotlari model parametrlarini moslashtirish uchun ishlatiladigan asosiy ma'lumotlar to'plamidir."
                ),
            },
        ],
        "quiz": [
            {
                "question": "Sun'iy intellektning asosiy maqsadi nima?",
                "options": {
                    "A": "Faqat kalkulyator yaratish",
                    "B": "Inson kabi yoki undan foydali tarzda aqlli vazifalarni bajarish",
                    "C": "Faqat internetga ulash",
                    "D": "Faqat rasm chizish",
                },
                "answer": "B",
                "explanation": "SI ning maqsadi aqlli qaror, tahlil va avtomatlashtirilgan vazifalarni bajarishdir.",
            },
            {
                "question": "Mashinali o'qitish nimaga asoslanadi?",
                "options": {
                    "A": "Faqat qo'lda yozilgan qat'iy qoidalarga",
                    "B": "Faqat elektr quvvatiga",
                    "C": "Ma'lumotdan qonuniyat o'rganishga",
                    "D": "Faqat tasodifiy taxminga",
                },
                "answer": "C",
                "explanation": "Machine learning modelni ma'lumotdan o'rganishga tayantiradi.",
            },
            {
                "question": "Nazoratli o'qitishda modelga nima beriladi?",
                "options": {
                    "A": "Faqat kirishlar",
                    "B": "Kirishlar va ularga mos to'g'ri javoblar",
                    "C": "Faqat xatolar ro'yxati",
                    "D": "Faqat bo'sh jadval",
                },
                "answer": "B",
                "explanation": "Supervised learning da input va label birga bo'ladi.",
            },
            {
                "question": "Quyidagilardan qaysi biri klassifikatsiya misoli?",
                "options": {
                    "A": "Uy narxini aniq qiymat sifatida topish",
                    "B": "Haroratni bashorat qilish",
                    "C": "Emailni spam yoki spam emas deb ajratish",
                    "D": "Integrallash",
                },
                "answer": "C",
                "explanation": "Spam filtrlash klassifikatsiya vazifasidir.",
            },
            {
                "question": "Overfitting holatida nima yuz beradi?",
                "options": {
                    "A": "Model yangi ma'lumotlarda hamisha mukammal ishlaydi",
                    "B": "Model trening ma'lumotini yodlab oladi va umumlashtirish yomonlashadi",
                    "C": "Model umuman o'rganmaydi",
                    "D": "Model hajmi kamayadi",
                },
                "answer": "B",
                "explanation": "Overfitting umumlashtirish qobiliyatini pasaytiradi.",
            },
            {
                "question": "Neyron tarmoqning eng sodda qurilish birligi nima?",
                "options": {
                    "A": "Fayl",
                    "B": "Node yoki neyron",
                    "C": "Router",
                    "D": "Printer",
                },
                "answer": "B",
                "explanation": "Neyron tarmoq sun'iy neyronlardan tashkil topadi.",
            },
            {
                "question": "Regressiya odatda qanday natijani bashorat qiladi?",
                "options": {
                    "A": "Diskret sinfni",
                    "B": "Faqat matnni",
                    "C": "Uzluksiz sonli qiymatni",
                    "D": "Faqat rasmni",
                },
                "answer": "C",
                "explanation": "Regression continuous value ni bashorat qiladi.",
            },
            {
                "question": "Training data nima uchun kerak?",
                "options": {
                    "A": "Model parametrlarini o'rganish uchun",
                    "B": "Faqat bezak uchun",
                    "C": "Internet tezligini oshirish uchun",
                    "D": "Monitor rangini almashtirish uchun",
                },
                "answer": "A",
                "explanation": "Model aynan o'quv ma'lumotlari orqali moslashadi.",
            },
            {
                "question": "Quyidagilardan qaysi biri SI qo'llanilishiga misol bo'ladi?",
                "options": {
                    "A": "Tibbiy tasvirlarni tahlil qilish",
                    "B": "Faqat daftar tikish",
                    "C": "Faqat lampani yoqish",
                    "D": "Qog'ozni buklash",
                },
                "answer": "A",
                "explanation": "Tibbiy diagnostika SI ning muhim amaliy yo'nalishlaridan biri.",
            },
            {
                "question": "Deep learning qachon ayniqsa samarali bo'ladi?",
                "options": {
                    "A": "Murakkab rasm, ovoz va matn ma'lumotlarida",
                    "B": "Faqat chiziq chizishda",
                    "C": "Faqat kalkulyatorda",
                    "D": "Faqat internet bo'lmaganda",
                },
                "answer": "A",
                "explanation": "Ko'p qatlamli tarmoqlar murakkab signallarda kuchli natija beradi.",
            },
        ],
    },
    "stats": {
        "title": "Ehtimollik va statistika",
        "keywords": [
            "ehtimollik",
            "statistika",
            "ehtimollik va statistika",
            "probability",
            "statistics",
        ],
        "intro": (
            "Ehtimollik va statistika tasodifiy hodisalar, ma'lumotlarni yig'ish, "
            "tahlil qilish va xulosalash usullarini o'rganadi."
        ),
        "summary": {
            "core": [
                "Ta'rif: tasodifiy hodisa va ma'lumotlarni tahlil qiladigan fan.",
                "Asosiy tushunchalar: ehtimollik, o'rtacha qiymat, mediana, moda, dispersiya.",
                "Mustaqil hodisalar uchun P(A va B)=P(A)*P(B).",
                "Bayes formulasi yangi ma'lumot kelganda ehtimollikni yangilaydi.",
            ],
            "formulas": [
                "O'rtacha qiymat = qiymatlar yig'indisi / soni",
                "Dispersiya = o'rtachadan og'ishlar kvadratlarining o'rtachasi",
                "Standart og'ish = sqrt(dispersiya)",
            ],
            "applications": [
                "So'rovnoma va data tahlili",
                "Risk va prognozlash",
                "ML modellarini baholash",
            ],
        },
        "faq": [
            {
                "keywords": ["ehtimollik nima", "probability nima"],
                "answer": "Ehtimollik hodisaning yuz berish darajasini 0 va 1 oralig'ida ifodalaydi.",
            },
            {
                "keywords": ["matematik kutilma", "expected value", "kutilma"],
                "answer": (
                    "Matematik kutilma tasodifiy miqdorning o'rtacha kutiladigan qiymatidir. "
                    "Diskret holatda u qiymatlar va ularning ehtimolliklari ko'paytmalari yig'indisiga teng."
                ),
            },
            {
                "keywords": ["dispersiya", "variance"],
                "answer": (
                    "Dispersiya ma'lumot yoki tasodifiy miqdorning o'rtacha qiymat atrofida "
                    "qanchalik tarqalganini ko'rsatadi."
                ),
            },
            {
                "keywords": ["standart ogish", "standart og'ish", "standard deviation"],
                "answer": "Standart og'ish dispersiyaning kvadrat ildizi bo'lib, tarqalishni asl birliklarda ko'rsatadi.",
            },
            {
                "keywords": ["median", "mediana"],
                "answer": "Mediana tartiblangan ma'lumotning o'rtadagi qiymati bo'lib, chet qiymatlarga kamroq sezgir.",
            },
            {
                "keywords": ["moda", "mode"],
                "answer": "Moda eng ko'p uchraydigan qiymatdir.",
            },
            {
                "keywords": ["bayes", "bayes formulasi"],
                "answer": (
                    "Bayes formulasi yangi ma'lumot kelganda ehtimollikni yangilashga xizmat qiladi: "
                    "P(A|B)=P(B|A)P(A)/P(B)."
                ),
            },
            {
                "keywords": ["normal taqsimot", "gauss taqsimoti", "normal distribution"],
                "answer": (
                    "Normal taqsimot qo'ng'iroqsimon ko'rinishga ega bo'lib, ko'plab tabiiy va o'lchovli jarayonlarni yaxshi ifodalaydi."
                ),
            },
        ],
        "quiz": [
            {
                "question": "Ehtimollik qiymati qaysi oraliqda bo'ladi?",
                "options": {
                    "A": "-1 dan 1 gacha",
                    "B": "0 dan 1 gacha",
                    "C": "0 dan 100 gacha",
                    "D": "Faqat musbat butun son",
                },
                "answer": "B",
                "explanation": "Ehtimollik 0 va 1 oralig'ida yotadi.",
            },
            {
                "question": "Tanga adolatli bo'lsa, gerb tushish ehtimolligi nechaga teng?",
                "options": {
                    "A": "1/4",
                    "B": "1/3",
                    "C": "1/2",
                    "D": "1",
                },
                "answer": "C",
                "explanation": "Adolatli tangada ikki natija teng ehtimollikka ega.",
            },
            {
                "question": "O'rtacha qiymat nimani bildiradi?",
                "options": {
                    "A": "Eng katta qiymatni",
                    "B": "Qiymatlar yig'indisini ularning soniga bo'lish natijasini",
                    "C": "Eng kichik qiymatni",
                    "D": "Faqat medianani",
                },
                "answer": "B",
                "explanation": "Mean yoki arifmetik o'rta shu tarzda hisoblanadi.",
            },
            {
                "question": "Mediana qaysi ta'rifga mos?",
                "options": {
                    "A": "Eng ko'p takrorlangan qiymat",
                    "B": "Tartiblangan ma'lumotning o'rtadagi qiymati",
                    "C": "Barcha qiymatlar yig'indisi",
                    "D": "Dispersiyaning kvadrati",
                },
                "answer": "B",
                "explanation": "Median data markazining barqaror o'lchovi hisoblanadi.",
            },
            {
                "question": "Moda nimani bildiradi?",
                "options": {
                    "A": "Eng ko'p uchraydigan qiymatni",
                    "B": "Eng kichik qiymatni",
                    "C": "O'rtacha qiymatni",
                    "D": "Tasodifiy tanlangan qiymatni",
                },
                "answer": "A",
                "explanation": "Moda chastotasi eng katta bo'lgan qiymatdir.",
            },
            {
                "question": "Dispersiya nimani o'lchaydi?",
                "options": {
                    "A": "Ma'lumotning tarqalishini",
                    "B": "Faqat maksimal qiymatni",
                    "C": "Faqat minimal qiymatni",
                    "D": "Faqat ehtimollik yig'indisini",
                },
                "answer": "A",
                "explanation": "Variance ma'lumotlarning markaz atrofida yoyilishini ifodalaydi.",
            },
            {
                "question": "Standart og'ish nimaga teng?",
                "options": {
                    "A": "Dispersiyaning kvadratiga",
                    "B": "Dispersiyaning kvadrat ildiziga",
                    "C": "Medianaga",
                    "D": "Modaga",
                },
                "answer": "B",
                "explanation": "Standart og'ish = sqrt(dispersiya).",
            },
            {
                "question": "Mustaqil hodisalar uchun P(A va B) nima bo'ladi?",
                "options": {
                    "A": "P(A)+P(B)",
                    "B": "P(A)-P(B)",
                    "C": "P(A) * P(B)",
                    "D": "Har doim 1",
                },
                "answer": "C",
                "explanation": "Independent events uchun birgalikdagi ehtimollik ko'paytma bilan topiladi.",
            },
            {
                "question": "Normal taqsimotning shakli qanday bo'ladi?",
                "options": {
                    "A": "Uchburchak",
                    "B": "Qo'ng'iroqsimon",
                    "C": "To'rtburchak",
                    "D": "Tasodifiy",
                },
                "answer": "B",
                "explanation": "Gaussian distribution bell-shaped ko'rinishga ega.",
            },
            {
                "question": "Bayes formulasi qachon foydali?",
                "options": {
                    "A": "Yangi ma'lumot kelganda ehtimollikni yangilashda",
                    "B": "Faqat tenglama yechishda",
                    "C": "Faqat grafik chizishda",
                    "D": "Faqat integrallashda",
                },
                "answer": "A",
                "explanation": "Bayes yondashuvi posterior ehtimollikni hisoblashda ishlatiladi.",
            },
        ],
    },
    "diff": {
        "title": "Differensial tenglamalar",
        "keywords": [
            "differensial tenglama",
            "differensial tenglamalar",
            "differential equation",
            "hosila tenglama",
        ],
        "intro": (
            "Differensial tenglamalar noma'lum funksiya va uning hosilalari orasidagi bog'lanishni ifodalaydi. "
            "Ular fizika, biologiya, iqtisod va muhandislikda keng qo'llanadi."
        ),
        "summary": {
            "core": [
                "Ta'rif: noma'lum funksiya va hosilalari orasidagi bog'lanish.",
                "Turlari: ODE va PDE.",
                "Tartib: eng yuqori hosila tartibi bilan aniqlanadi.",
                "Boshlang'ich shart xususiy yechimni topishga yordam beradi.",
            ],
            "formulas": [
                "y'=ky -> yechim odatda eksponensial ko'rinishga ega",
                "Ajraluvchi tenglama: o'zgaruvchilar ajratilib integrallanadi",
            ],
            "applications": [
                "Harakat va tebranish modellari",
                "Issiqlik va diffuziya jarayonlari",
                "Populyatsiya o'sishi va kamayishi",
            ],
        },
        "faq": [
            {
                "keywords": ["oddiy differensial tenglama", "ode"],
                "answer": "Oddiy differensial tenglamada noma'lum funksiya bitta o'zgaruvchiga bog'liq bo'ladi.",
            },
            {
                "keywords": ["xususiy hosilali tenglama", "pde"],
                "answer": "Xususiy hosilali tenglamada funksiya bir nechta o'zgaruvchiga bog'liq va xususiy hosilalar qatnashadi.",
            },
            {
                "keywords": ["tartib", "order"],
                "answer": "Differensial tenglamaning tartibi undagi eng yuqori hosila tartibi bilan aniqlanadi.",
            },
            {
                "keywords": ["umumiy yechim", "general solution"],
                "answer": "Umumiy yechim ixtiyoriy konstantalarni o'z ichiga olgan yechimlar oilasidir.",
            },
            {
                "keywords": ["xususiy yechim", "particular solution"],
                "answer": "Xususiy yechim boshlang'ich yoki chegaraviy shartlardan keyin aniq topilgan bitta yechimdir.",
            },
            {
                "keywords": ["ajraluvchi", "separable"],
                "answer": (
                    "Ajraluvchi tenglamada o'zgaruvchilarni ikki tomonga ajratib, integrallash orqali yechim topish mumkin."
                ),
            },
            {
                "keywords": ["chiziqli differensial tenglama", "linear differential equation"],
                "answer": (
                    "Chiziqli differensial tenglamada noma'lum funksiya va uning hosilalari birinchi darajada qatnashadi."
                ),
            },
            {
                "keywords": ["boshlangich shart", "boshlang'ich shart", "initial condition"],
                "answer": (
                    "Boshlang'ich shart yechimning ma'lum nuqtadagi qiymatini beradi va xususiy yechimni aniqlashga yordam beradi."
                ),
            },
        ],
        "quiz": [
            {
                "question": "Differensial tenglama nimani bog'laydi?",
                "options": {
                    "A": "Faqat sonlar ro'yxatini",
                    "B": "Noma'lum funksiya va uning hosilalarini",
                    "C": "Faqat matnlarni",
                    "D": "Faqat ehtimolliklarni",
                },
                "answer": "B",
                "explanation": "Differensial tenglamada funksiya va hosilalar orasidagi munosabat beriladi.",
            },
            {
                "question": "y' = 3x tenglamaning tartibi nechanchi?",
                "options": {
                    "A": "1-tartibli",
                    "B": "2-tartibli",
                    "C": "3-tartibli",
                    "D": "Tartibsiz",
                },
                "answer": "A",
                "explanation": "Eng yuqori hosila y' bo'lgani uchun u 1-tartibli tenglama.",
            },
            {
                "question": "Quyidagilardan qaysi biri ODE ga misol?",
                "options": {
                    "A": "du/dx + u = 0",
                    "B": "u_x + u_y = 0 va u ikki o'zgaruvchili",
                    "C": "Faqat jadval",
                    "D": "Faqat matritsa",
                },
                "answer": "A",
                "explanation": "ODE bitta mustaqil o'zgaruvchili tenglamadir.",
            },
            {
                "question": "Ajraluvchi tenglamada asosiy usul nima?",
                "options": {
                    "A": "Matritsaga aylantirish",
                    "B": "O'zgaruvchilarni ajratib integrallash",
                    "C": "Faqat son qo'yish",
                    "D": "Grafikni bo'yash",
                },
                "answer": "B",
                "explanation": "Separable equations odatda variables separation bilan yechiladi.",
            },
            {
                "question": "Umumiy yechim nimani o'z ichiga oladi?",
                "options": {
                    "A": "Ixtiyoriy konstantalarni",
                    "B": "Faqat bitta sonni",
                    "C": "Faqat grafikni",
                    "D": "Hech narsani",
                },
                "answer": "A",
                "explanation": "General solution yechimlar oilasini bildiradi.",
            },
            {
                "question": "Boshlang'ich shart nima uchun kerak?",
                "options": {
                    "A": "Yechimlar oilasidan aniq bitta yechimni tanlash uchun",
                    "B": "Faqat rasm chizish uchun",
                    "C": "Faqat matn yozish uchun",
                    "D": "Tenglamani bekor qilish uchun",
                },
                "answer": "A",
                "explanation": "Initial condition particular solution ni aniqlaydi.",
            },
            {
                "question": "Quyidagilardan qaysi biri 2-tartibli tenglamaga misol?",
                "options": {
                    "A": "y' + y = 0",
                    "B": "y'' - 4y = 0",
                    "C": "x + y = 0",
                    "D": "2x = 10",
                },
                "answer": "B",
                "explanation": "Eng yuqori hosila y'' bo'lgani uchun 2-tartibli.",
            },
            {
                "question": "PDE nima?",
                "options": {
                    "A": "Faqat bitta o'zgaruvchili oddiy tenglama",
                    "B": "Bir nechta o'zgaruvchili xususiy hosilali tenglama",
                    "C": "Faqat statistik formula",
                    "D": "Faqat geometrik shakl",
                },
                "answer": "B",
                "explanation": "PDE partial derivatives bilan yoziladi.",
            },
            {
                "question": "y' = ky ko'rinishidagi tenglama odatda nimani ifodalaydi?",
                "options": {
                    "A": "Eksponensial o'sish yoki kamayishni",
                    "B": "Faqat doimiy funksiyani",
                    "C": "Faqat sinusni",
                    "D": "Faqat ehtimollikni",
                },
                "answer": "A",
                "explanation": "Bu model ko'pincha o'sish va parchalanish jarayonlarida uchraydi.",
            },
            {
                "question": "Chiziqli differensial tenglamada noma'lum funksiya qanday qatnashadi?",
                "options": {
                    "A": "Faqat kvadratda",
                    "B": "Faqat kubda",
                    "C": "Birinchi darajada",
                    "D": "Faqat ildiz ostida",
                },
                "answer": "C",
                "explanation": "Linear equation da y va hosilalari birinchi darajada bo'ladi.",
            },
        ],
    },
}
