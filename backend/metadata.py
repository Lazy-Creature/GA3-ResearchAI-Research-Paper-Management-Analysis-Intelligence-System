import re

def extract_metadata(text):

    # Break into readable candidate lines
    lines = [l.strip() for l in text.split(".") if 10 < len(l.strip()) < 200]

    title = "Unknown Title"

    # ---- Title must look like a real research paper title ----
    for l in lines[:15]:
        # Reject affiliations / addresses / institutes
        if any(x in l.lower() for x in [
            "university","department","institute","laboratory",
            "cnrs","inria","lille","india","france","school","center"
        ]):
            continue

        # Title length heuristic (real titles are 6–16 words)
        wc = len(l.split())
        if 6 <= wc <= 16:
            title = l
            break

    # ---- Authors (optional, often missing in PDFs) ----
    authors = ["Unknown Author"]
    for l in lines[:20]:
        if "," in l and not re.search(r"\d", l):
            authors = [a.strip() for a in l.split(",")]
            break

    # ---- Year ----
    year_match = re.search(r"(19|20)\d{2}", text)
    year = int(year_match.group()) if year_match else 2024

    return title, authors, year
