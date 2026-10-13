import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


def search_news(
    query: str,
    max_results: int = 5,
) -> list[dict]:
    """
    Search recent news sources for a research question.
    """

    client = TavilyClient(
        api_key=os.environ["TAVILY_API_KEY"]
    )

    response = client.search(
        query=query,
        search_depth="advanced",
        topic="news",
        max_results=max_results,
        include_answer=False,
    )

    results = []

    for result in response["results"]:
        results.append(
            {
                "title": result.get("title"),
                "url": result.get("url"),
                "content": result.get("content"),
                "score": result.get("score"),
                "source_type": "news",
            }
        )

    return results