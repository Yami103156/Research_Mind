from typing import List
from pydantic import BaseModel, Field


class SearchItem(BaseModel):
    title: str
    url: str
    snippet: str


class SearchResult(BaseModel):
    query: str
    results: List[SearchItem]


class ResearchDocument(BaseModel):
    """
    Represents one fully scraped webpage.
    """

    title: str

    url: str

    content: str


class ResearchPlan(BaseModel):

    goal: str = Field(
        description="Research Goal"
    )

    queries: List[str]

    focus_areas: List[str]