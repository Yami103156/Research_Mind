from dataclasses import dataclass

@dataclass
class ResearchState:

    topic: str

    plan: object

    documents: list

    report: str

    feedback: str

    score: float