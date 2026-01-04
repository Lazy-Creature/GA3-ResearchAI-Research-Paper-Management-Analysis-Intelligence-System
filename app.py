import streamlit as st
import uuid, os

from backend.pdf_parser import extract_sections
from backend.metadata import extract_metadata
from backend.keyword_extractor import extract_keywords
from backend.chunker import chunk_sections
from backend.vector_store import index_papers
from backend.summarizer import summarize
from backend.rag_engine import answer
from backend.trend_engine import emerging_topics
from backend.models import ResearchPaper
from backend.topic_extractor import extract_topics


st.set_page_config("Research AI", layout="wide")
st.title("📚 Research Paper Intelligence System")

if "papers" not in st.session_state:
    st.session_state.papers = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = set()

# ---------------- UPLOAD ----------------
st.header("Upload Research Paper")
uploaded = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded and uploaded.name not in st.session_state.uploaded_files:

    os.makedirs("data/papers", exist_ok=True)
    path = f"data/papers/{uploaded.name}"

    with open(path, "wb") as f:
        f.write(uploaded.read())

    sections = extract_sections(path)
    full_text = sections["full_text"]

    title, authors, year = extract_metadata(full_text)
    keywords = extract_keywords(full_text)
    topics = extract_topics(full_text)

    paper = ResearchPaper(
        paper_id=str(uuid.uuid4()),
        title=title,
        authors=authors,
        abstract=full_text[:1500],
        full_text=full_text,
        year=year,
        venue="Unknown",
        keywords=keywords,
        topics=topics,
        references=[],
        citations=[]
    )

    st.session_state.papers.append(paper)
    st.session_state.uploaded_files.add(uploaded.name)

    docs = chunk_sections(sections, paper.paper_id, paper.year)
    index_papers(docs)

    st.success("Paper indexed successfully!")

# ---------------- LIBRARY ----------------
st.header("Paper Library")

for p in st.session_state.papers:
    st.markdown(f"### {p.title}")
    st.markdown(f"**Paper ID:** {p.paper_id}")
    st.markdown(f"**Authors:** {', '.join(p.authors)}")
    st.markdown(f"**Year:** {p.year}")
    st.markdown(f"**Venue:** {p.venue}")
    st.markdown(f"**Abstract:** {p.abstract}")

    if p.keywords:
        st.markdown(f"**Keywords:** {', '.join(p.keywords)}")

    if st.button("Generate Summary", key=p.paper_id):
        st.markdown(summarize(p.full_text))

# ---------------- CHAT ----------------
st.header("Ask Research Assistant")
q = st.text_input("Ask question")
if st.button("Ask"):
    st.markdown(answer(q))

# ---------------- TRENDS ----------------
st.header("Emerging Topics")
if st.session_state.papers:
    for t in emerging_topics(st.session_state.papers):
        st.markdown(f"• {t}")
    

