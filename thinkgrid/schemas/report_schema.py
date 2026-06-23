from pydantic import BaseModel


class ResearchReport(BaseModel):
    topic: str
    research_plan: str
    summary: str
    report: str
    review: str
    saved_path: str | None = None