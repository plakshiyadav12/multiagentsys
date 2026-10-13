import httpx


def search_academic(
    query: str,
    max_results: int = 5,
) -> list[dict]:
    """
    Search Semantic Scholar for academic papers.
    """

    url = "https://api.semanticscholar.org/graph/v1/paper/search"

    params = {
        "query": query,
        "limit": max_results,
        "fields": (
            "title,"
            "abstract,"
            "url,"
            "year,"
            "authors,"
            "citationCount"
        ),
    }

    try:
        response = httpx.get(
            url,
            params=params,
            timeout=15,
        )

        response.raise_for_status()

        data = response.json()

        results = []

        for paper in data.get("data", []):
            results.append(
                {
                    "title": paper.get("title"),
                    "url": paper.get("url"),
                    "content": paper.get("abstract") or "",
                    "year": paper.get("year"),
                    "authors": [
                        author.get("name")
                        for author in paper.get("authors", [])
                    ],
                    "citation_count": paper.get(
                        "citationCount", 0
                    ),
                }
            )

        return results

    except Exception as error:
        print(
            f"Academic search failed: {error}"
        )

        return []