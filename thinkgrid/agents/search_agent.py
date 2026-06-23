from thinkgrid.tools.web_search import search_web
from thinkgrid.prompts.search_prompt import SEARCH_PROMPT
from thinkgrid.models.llm import llm


class SearchAgent:

    def run(self, topic: str):

        research_plan = llm.invoke(
            SEARCH_PROMPT.format(topic=topic)
        ).content

        results = search_web(topic)

        formatted_results = []

        for item in results.get("results", []):

            formatted_results.append(
                {
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "content": item.get("content", ""),
                }
            )

        return {
            "research_plan": research_plan,
            "sources": formatted_results
        }