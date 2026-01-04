from backend.vector_store import semantic_search
from langchain_groq import ChatGroq
from backend.config import GROQ_API_KEY

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")

def answer(question):
    docs = semantic_search(question)
    if not docs:
        return "⚠️ No papers indexed."

    context = "\n".join(d.page_content for d in docs)

    return llm.invoke(f"Use only this context:\n{context}\nQ:{question}").content
