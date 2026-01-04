from pydantic import BaseModel
from typing import List

class ResearchPaper(BaseModel):
    paper_id: str
    title: str
    authors: List[str]
    abstract: str
    full_text: str
    year: int
    venue: str
    keywords: List[str]
    topics: List[str]
    references: List[str]
    citations: List[str] = []
