from pydantic import BaseModel, HttpUrl


class SearchResult(BaseModel):
    title: str
    url: str
    content: str


class SearchResponse(BaseModel):
    research_plan: str
    sources: list[SearchResult]