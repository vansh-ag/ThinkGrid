from pydantic import BaseModel


class ResearchSummary(BaseModel):
    key_facts: list[str]
    statistics: list[str]
    trends: list[str]
    opportunities: list[str]
    risks: list[str]
    expert_opinions: list[str]
    summary: str