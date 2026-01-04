from backend.config import GROQ_API_KEY
from langchain_groq import ChatGroq

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile", temperature=0.1)

def extract_topics(text):
    prompt = f"""
You are analyzing a scientific research paper.

Extract 5–7 high-level research topics (not keywords, but conceptual topics).
Use clean academic English.

Paper:
{text[:6000]}

Return ONLY a comma-separated list.
"""
    result = llm.invoke(prompt).content
    return [t.strip() for t in result.split(",") if len(t.strip()) > 3]
