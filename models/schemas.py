from pydantic import BaseModel
from typing import List


class Paper(BaseModel):
    title: str
    authors: List[str]
    publication_year: int
    abstract: str
    research_problem: str
    methodology: str
    dataset: str
    key_findings: str
    limitations: str