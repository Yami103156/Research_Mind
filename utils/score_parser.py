import re


def extract_score(feedback: str) -> float:
    """
    Extract numerical score from Critic feedback.

    Example:

    Score: 8.7/10

    Returns:
        8.7
    """

    match = re.search(
        r"Score:\s*([0-9]+(?:\.[0-9]+)?)",
        feedback,
        re.IGNORECASE,
    )

    if match:
        return float(match.group(1))

    return 0.0