# parser/extractors.py

import re
from typing import List, Optional


# -------------------------------------------------------------------
# Ticket ID extraction
# -------------------------------------------------------------------

TICKET_PATTERNS = [
    r"INC-\d{8}-\d{8}",      # INC-20251012-00003346
    r"\b\d{10,12}\b",       # internal refs like 2510O06813
]


def extract_ticket_ids(text: str) -> List[str]:
    tickets = set()

    if not text:
        return []

    for pattern in TICKET_PATTERNS:
        for match in re.findall(pattern, text):
            tickets.add(match)

    return list(tickets)


# -------------------------------------------------------------------
# Priority extraction
# -------------------------------------------------------------------

def extract_priority(text: str) -> Optional[str]:
    if not text:
        return None

    match = re.search(r"\bP[1-3]\b", text)
    return match.group(0) if match else None


# -------------------------------------------------------------------
# RuralStar site extraction (URH sites)
# -------------------------------------------------------------------

RURAL_SITE_PATTERN = r"\b[A-Z]{2,3}_\d{2,4}_URH_[A-Z0-9_]+\b"


def extract_rural_sites(text: str) -> List[str]:
    if not text:
        return []

    sites = re.findall(RURAL_SITE_PATTERN, text)
    return list(set(sites))


# -------------------------------------------------------------------
# Update number extraction
# -------------------------------------------------------------------

def extract_update_number(text: str) -> Optional[int]:
    if not text:
        return None

    match = re.search(r"UPDATE\s*(\d+)", text)
    return int(match.group(1)) if match else None


# -------------------------------------------------------------------
# Start time extraction (Début)
# -------------------------------------------------------------------

def extract_start_time(text: str) -> Optional[str]:
    """
    Extract start time string.

    Example accepted formats:
    - DEBUT: 12/10/2025 A 05:03 UTC
    - DEBUT: 2025-10-12 10:20:54 UTC
    """

    if not text:
        return None

    match = re.search(
        r"DEBUT\s*:\s*([0-9:/\- ]+UTC)",
        text
    )

    return match.group(1).strip() if match else None
