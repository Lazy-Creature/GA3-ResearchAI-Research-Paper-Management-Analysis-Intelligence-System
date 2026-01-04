# 📚 ResearchAI – Research Paper Management & Analysis Intelligence System  

> An Enterprise-Grade GenAI Research Assistant for Academic Knowledge Discovery
<img width="1918" height="957" alt="image" src="https://github.com/user-attachments/assets/4cc2fb0d-c1c9-4d79-a0f2-a17fca5b2e79" />

---

## 🔬 Project Overview  

**ResearchAI** is an AI-powered research intelligence platform that helps students, researchers, and data scientists **organize, analyze, summarize, search, and discover research papers** using **Large Language Models (LLMs), semantic vector search, and research trend analytics**.

It transforms unstructured research PDFs into structured academic knowledge, enabling:

- Instant academic summaries  
- Semantic search across research libraries  
- Context-aware research Q&A  
- Conceptual topic mining  
- Emerging research trend discovery  

Inspired by real-world platforms such as **Google Scholar AI, Semantic Scholar, Elsevier Scopus AI, and Springer Nature AI**.

---

## 🚀 Key Features  

- Upload and manage research PDFs  
- Automatic metadata extraction  
- Clean academic summarization  
- FAISS-based semantic search (RAG)  
- Context-aware research Q&A  
- LLM-based conceptual topic extraction  
- Emerging research trend analytics  
- Interactive Streamlit dashboard  

---

## 🏗 System Architecture  

<img width="297" height="532" alt="image" src="https://github.com/user-attachments/assets/daba817c-aebe-4680-bad4-fa13bf308aee" />


---

## 🧩 Module Description  

| Module | Description |
|------|-------------|
| pdf_parser.py | Cleans raw PDFs |
| metadata.py | Extracts metadata |
| keyword_extractor.py | Keyword mining |
| topic_extractor.py | Conceptual topic extraction |
| chunker.py | Semantic chunking |
| vector_store.py | FAISS vector DB |
| summarizer.py | Academic summarization |
| rag_engine.py | RAG pipeline |
| trend_engine.py | Trend analytics |

---

## ⚙️ Working Principle  

1. Upload research PDF  
2. Clean and extract text  
3. Extract metadata, keywords, and topics  
4. Build FAISS semantic index  
5. Generate summaries and Q&A  
6. Detect emerging research trends  
7. Visualize in dashboard  

---

## 📈 Emerging Topic Intelligence  

Detects:

- Fast-growing research areas  
- Cross-domain convergence  
- Emerging scientific subfields  
- Dominant research paradigms  

---

## 🖥 Frontend  

Built with **Streamlit** featuring:

- Paper library  
- One-click summarization  
- Research chat assistant  
- Topic trend panel  

---

## 🛠 Tech Stack  

| Layer | Technology |
|------|------------|
Frontend | Streamlit |
LLM | Groq (LLaMA-3.3) |
Embeddings | HuggingFace |
Vector DB | FAISS |
Framework | LangChain |
Language | Python |

---

## 📦 Installation  

```bash
git clone <repository-url>
cd ResearchAI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

