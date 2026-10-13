from app.tools.academic_search import search_academic
from app.agents.evidence import extract_evidence


def research_academic(
    question: str,
    max_results: int = 3,
    max_evidence_sources: int = 2,
) -> dict:
    """
    Research a question using academic papers.
    """

    papers = search_academic(
        query=question,
        max_results=max_results,
    )

    print(
        f"\nFound {len(papers)} academic papers."
    )

    papers.sort(
        key=lambda paper: paper.get(
            "citation_count",
            0,
        ),
        reverse=True,
    )

    selected_papers = papers[
        :max_evidence_sources
    ]

    evidence = []

    if selected_papers:

        try:

            evidence_bundle = extract_evidence(
                question=question,
                sources=selected_papers,
            )

            evidence = evidence_bundle.evidence

        except Exception as error:

            print(
                f"Warning: academic evidence extraction "
                f"failed: {error}"
            )

    return {
        "question": question,
        "papers": papers,
        "evidence": evidence,
    }