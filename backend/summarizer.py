from backend.config import GROQ_API_KEY
from langchain_groq import ChatGroq

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile", temperature=0.2)

def summarize(text):
    prompt = f"""
You are an academic research assistant.
Write a clean, readable, human academic summary.

Format exactly like:

Research Problem:
...
Proposed Method:
...
Key Contributions:
...
Results:
...
Limitations:
...

Paper:
{text[:12000]}
"""
    return llm.invoke(prompt).content
