from pypdf import PdfReader
import re

def extract_sections(pdf_path):
    reader = PdfReader(pdf_path)
    pages = [(p.extract_text() or "") for p in reader.pages]
    text = " ".join(pages)

    # Remove latex/math/garbage
    text = re.sub(r"\$.*?\$", " ", text)
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9.,:;()\- ]+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return {"full_text": text}
