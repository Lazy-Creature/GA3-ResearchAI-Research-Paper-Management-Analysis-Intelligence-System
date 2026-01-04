import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDER = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def index_papers(docs):
    if not docs:
        return

    os.makedirs("data/vector_index", exist_ok=True)

    if os.path.exists("data/vector_index/index.faiss"):
        db = FAISS.load_local("data/vector_index", EMBEDDER, allow_dangerous_deserialization=True)
        db.add_documents(docs)
    else:
        db = FAISS.from_documents(docs, EMBEDDER)

    db.save_local("data/vector_index")

def semantic_search(query, k=5):
    if not os.path.exists("data/vector_index"):
        return []

    db = FAISS.load_local("data/vector_index", EMBEDDER, allow_dangerous_deserialization=True)
    return db.similarity_search(query, k=k)
