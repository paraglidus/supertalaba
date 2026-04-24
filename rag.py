from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import PyPDF2

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []
index = None

def load_pdf(path):
    text = ""
    reader = PyPDF2.PdfReader(path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_text(text, chunk_size=300):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def build_index():
    global documents, index
    
    text = load_pdf("data/kitob.pdf")
    documents = split_text(text)

    embeddings = model.encode(documents)
    
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

def search(query, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    results = [documents[i] for i in indices[0]]
    return "\n".join(results)