from urllib.parse import urlparse


# Domains that are generally useful for research.
TRUSTED_DOMAINS = {
    "gov",
    "edu",
    "org",
}


def calculate_source_score(
    source: dict,
    question: str,
) -> float:
    """
    Calculate a heuristic quality score for a source.

    This is NOT an absolute measure of truth.
    It is used to prioritize potentially useful sources.
    """

    score = 0.0

    url = source.get("url", "")
    title = source.get("title", "")
    content = source.get("content", "")

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    # --------------------------------
    # 1. Domain quality
    # --------------------------------

    if domain.endswith(".gov"):
        score += 0.30

    elif domain.endswith(".edu"):
        score += 0.25

    elif domain.endswith(".org"):
        score += 0.15

    else:
        score += 0.05

    # --------------------------------
    # 2. Content availability
    # --------------------------------

    if len(content) > 500:
        score += 0.20

    elif len(content) > 200:
        score += 0.10

    # --------------------------------
    # 3. Title relevance
    # --------------------------------

    question_words = set(
        question.lower().split()
    )

    title_words = set(
        title.lower().split()
    )

    overlap = question_words & title_words

    if len(overlap) >= 4:
        score += 0.30

    elif len(overlap) >= 2:
        score += 0.20

    elif len(overlap) >= 1:
        score += 0.10

    return min(score, 1.0)