import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(
    query: str,
    max_results: int = 10
):
    """
    Perform web search using Tavily.
    """

    try:

        response = client.search(
            query=query,
            max_results=max_results,
            search_depth="advanced"
        )

        return response

    except Exception as e:

        raise Exception(
            f"Search Error: {str(e)}"
        )