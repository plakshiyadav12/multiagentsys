from app.tools.web_search import search_web
from app.tools.webpage_reader import read_webpage
from app.tools.source_ranker import calculate_source_score
from app.agents.evidence import extract_evidence


def research_subquestion(
    question: str,
    max_results: int = 3,
    max_evidence_sources: int = 2,
) -> dict:
    """
    Research a single sub-question using web sources.
    """

    sources = search_web(
        query=question,
        max_results=max_results,
    )

    for source in sources:

        print(
            f"\nReading: {source['title']}"
        )

        webpage_content = read_webpage(
            source["url"]
        )

        if webpage_content:

            source["content"] = webpage_content

            print(
                "✓ Full webpage extracted"
            )

        else:

            print(
                "⚠ Using search snippet"
            )

        source["quality_score"] = calculate_source_score(
            source=source,
            question=question,
        )

        print(
            f"Quality score: "
            f"{source['quality_score']:.2f}"
        )

    sources.sort(
        key=lambda source: source["quality_score"],
        reverse=True,
    )

    selected_sources = sources[
        :max_evidence_sources
    ]

    print(
        f"\nSelected "
        f"{len(selected_sources)} "
        f"sources for evidence extraction."
    )

    evidence = []

    if selected_sources:

        try:

            evidence_bundle = extract_evidence(
                question=question,
                sources=selected_sources,
            )

            evidence = evidence_bundle.evidence

        except Exception as error:

            print(
                f"Warning: evidence extraction failed: "
                f"{error}"
            )

    return {
        "question": question,
        "sources": sources,
        "evidence": evidence,
    }