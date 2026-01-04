from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_sections(sections, paper_id, year):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    docs = []

    for name, text in sections.items():
        for chunk in splitter.split_text(text):
            docs.append(Document(
                page_content=chunk,
                metadata={"paper_id": paper_id, "section": name, "year": year}
            ))
    return docs
