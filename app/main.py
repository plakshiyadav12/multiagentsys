from app.graph.workflow import build_research_graph


def main():

    question = input(
        "\nResearch question: "
    )

    print("\n" + "=" * 70)
    print("STARTING RESEARCH")
    print("=" * 70)

    graph = build_research_graph()

    initial_state = {
        "question": question
    }

    result = graph.invoke(
        initial_state
    )

    # --------------------------------
    # Research Plan
    # --------------------------------

    print("\n\n" + "=" * 70)
    print("RESEARCH PLAN")
    print("=" * 70)

    plan = result["plan"]

    print(
        f"\nMain question:\n"
        f"{plan['main_question']}"
    )

    for i, sub_question in enumerate(
        plan["sub_questions"],
        start=1,
    ):
        print(
            f"\n{i}. {sub_question['question']}"
        )

        print(
            f"   Purpose: "
            f"{sub_question['purpose']}"
        )

    # --------------------------------
    # Web Results
    # --------------------------------

    print("\n\n" + "=" * 70)
    print("WEB RESEARCH")
    print("=" * 70)

    for research in result.get(
        "web_results",
        [],
    ):

        print(
            f"\nQUESTION: "
            f"{research['question']}"
        )

        print(
            f"Sources found: "
            f"{len(research['sources'])}"
        )

        print(
            f"Evidence extracted: "
            f"{len(research['evidence'])}"
        )

        for evidence in research["evidence"]:

            print(
                f"\n  Claim: "
                f"{evidence.claim}"
            )

            print(
                f"  Confidence: "
                f"{evidence.confidence}"
            )

            print(
                f"  Source: "
                f"{evidence.source_url}"
            )

    # --------------------------------
    # Academic Results
    # --------------------------------

    print("\n\n" + "=" * 70)
    print("ACADEMIC RESEARCH")
    print("=" * 70)

    for research in result.get(
        "academic_results",
        [],
    ):

        print(
            f"\nQUESTION: "
            f"{research['question']}"
        )

        print(
            f"Papers found: "
            f"{len(research['papers'])}"
        )

        print(
            f"Evidence extracted: "
            f"{len(research['evidence'])}"
        )

        for paper in research["papers"]:

            print(
                f"\n  Paper: "
                f"{paper['title']}"
            )

            print(
                f"  Year: "
                f"{paper['year']}"
            )

            print(
                f"  Citations: "
                f"{paper['citation_count']}"
            )

            print(
                f"  URL: "
                f"{paper['url']}"
            )

    # --------------------------------
    # News Results
    # --------------------------------

    print("\n\n" + "=" * 70)
    print("NEWS RESEARCH")
    print("=" * 70)

    for research in result.get(
        "news_results",
        [],
    ):

        print(
            f"\nQUESTION: "
            f"{research['question']}"
        )

        print(
            f"Articles found: "
            f"{len(research['articles'])}"
        )

        print(
            f"Evidence extracted: "
            f"{len(research['evidence'])}"
        )

        for article in research["articles"]:

            print(
                f"\n  Article: "
                f"{article['title']}"
            )

            print(
                f"  URL: "
                f"{article['url']}"
            )

    print("\n\n" + "=" * 70)
    print("RESEARCH COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()