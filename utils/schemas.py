from typing import List
from pydantic import BaseModel, Field


class SearchItem(BaseModel):
    title: str
    url: str
    snippet: str


class SearchResult(BaseModel):
    query: str
    results: List[SearchItem]


class ResearchPlan(BaseModel):
    goal: str = Field(description="Research goal")
    queries: List[str]
    focus_areas: List[str]