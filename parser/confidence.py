# parser/confidence.py

from typing import Dict, Any


def compute_confidence(parsed: Dict[str, Any]) -> float:
    """
    Compute confidence score for a parsed incident message.

    Scoring logic:
    - Ticket ID present        → +0.30
    - Rural sites present      → +0.30
    - Start time present       → +0.20
    - Priority present         → +0.20
    """

    score = 0.0

    if parsed.get("ticket_ids"):
        score += 0.30

    if parsed.get("affected_rural_sites"):
        score += 0.30

    if parsed.get("start_time"):
        score += 0.20

    if parsed.get("priority"):
        score += 0.20

    return round(min(score, 1.0), 2)
