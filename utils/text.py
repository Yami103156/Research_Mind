def clean_text(text: str) -> str:
    """
    Normalize whitespace.
    """

    return " ".join(text.split())