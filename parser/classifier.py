# parser/classifier.py

import re


EVENT_NEW = "NEW"
EVENT_UPDATE = "UPDATE"
EVENT_RESTORED = "RESTORED"
EVENT_IGNORE = "IGNORE"


def classify_event(normalized_text: str) -> str:
    """
    Classify the incident event type based on normalized text.

    Returns one of:
    - NEW
    - UPDATE
    - RESTORED
    - IGNORE
    """

    if not normalized_text:
        return EVENT_IGNORE

    text = normalized_text

    # --- NEW incident ---
    if re.search(r"INCIDENT.*\bNEW\b", text):
        return EVENT_NEW

    # --- UPDATE ---
    if re.search(r"\bUPDATE\b\s*\d*", text):
        return EVENT_UPDATE

    # --- RESTORED ---
    if re.search(
        r"RETOUR A LA NORMALE|SERVICE RETABLI|RETABLISSEMENT|RESTORED",
        text,
    ):
        return EVENT_RESTORED

    return EVENT_IGNORE
