# parser/parser.py

from typing import Dict, Any

from parser.normalizer import normalize_text
from parser.classifier import classify_event, EVENT_IGNORE
from parser.extractors import (
    extract_ticket_ids,
    extract_priority,
    extract_rural_sites,
    extract_update_number,
    extract_start_time,
)
from parser.confidence import compute_confidence


def parse_message(raw_text: str) -> Dict[str, Any]:
    """
    Parse a raw WhatsApp incident message into structured data.
    """

    normalized = normalize_text(raw_text)
    event_type = classify_event(normalized)

    # Base structure (always returned)
    parsed: Dict[str, Any] = {
        "event_type": event_type,
        "raw_text": raw_text,
        "normalized_text": normalized,
        "ticket_ids": [],
        "priority": None,
        "start_time": None,
        "affected_rural_sites": [],
        "update_number": None,
        "confidence": 0.0,
    }

    # Ignore early if not an incident-related message
    if event_type == EVENT_IGNORE:
        return parsed

    # Field extraction
    parsed["ticket_ids"] = extract_ticket_ids(normalized)
    parsed["priority"] = extract_priority(normalized)
    parsed["start_time"] = extract_start_time(normalized)
    parsed["affected_rural_sites"] = extract_rural_sites(normalized)
    parsed["update_number"] = extract_update_number(normalized)

    # Confidence scoring
    parsed["confidence"] = compute_confidence(parsed)

    return parsed
