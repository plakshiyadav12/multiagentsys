from app.tools.news_search import search_news
from app.agents.evidence import extract_evidence


def research_news(
    question: str,
    max_results: int = 3,
    max_evidence_sources: int = 2,
) -> dict:
    """
    Research a question using recent news sources.
    """

    articles = search_news(
        query=question,
        max_results=max_results,
    )

    print(
        f"\nFound {len(articles)} news articles."
    )

    selected_articles = articles[
        :max_evidence_sources
    ]

    evidence = []

    if selected_articles:

        try:

            evidence_bundle = extract_evidence(
                question=question,
                sources=selected_articles,
            )

            evidence = evidence_bundle.evidence

        except Exception as error:

            print(
                f"Warning: news evidence extraction "
                f"failed: {error}"
            )

    return {
        "question": question,
        "articles": articles,
        "evidence": evidence,
    }