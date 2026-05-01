import re

TOXIC_KEYWORDS = ["kill", "hate", "idiot", "stupid"]
SEVERE_PATTERNS = [r"kill\s+yourself", r"i\s+will\s+hurt\s+you"]


def fast_path_filter(text: str):
    """
    Ultra-fast heuristic filtering (~milliseconds).
    Used to reduce load on ML models.
    """

    text_lower = text.lower()

    score = 0.0

    # Keyword scoring
    for word in TOXIC_KEYWORDS:
        if word in text_lower:
            score += 0.2

    # Regex detection (strong signals)
    for pattern in SEVERE_PATTERNS:
        if re.search(pattern, text_lower):
            score += 0.5

    score = min(score, 1.0)

    return {
        "confidence": score,
        "label": "toxic" if score > 0.5 else "neutral"
    }