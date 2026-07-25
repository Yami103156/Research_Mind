from typing import List

from pydantic import BaseModel, Field


class ResearchPlan(BaseModel):
    """
    Represents the structured output generated
    by the Planner Agent.
    """

    goal: str = Field(
        description="Overall objective of the research."
    )

    queries: List[str] = Field(
        description="Search queries that should be executed."
    )

    focus_areas: List[str] = Field(
        description="Major concepts that the report must cover."
    )