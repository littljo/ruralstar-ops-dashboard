# parser/normalizer.py

import unicodedata
import re


def normalize_text(text: str) -> str:
    """
    Normalize raw WhatsApp incident message text.

    Steps:
    - Ensure string
    - Uppercase
    - Remove accents
    - Normalize whitespace
    - Normalize time formats (05H03 -> 05:03)
    """

    if not text:
        return ""

    # 1. Ensure string & strip
    text = str(text).strip()

    # 2. Uppercase
    text = text.upper()

    # 3. Remove accents (é -> e, à -> a, etc.)
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")

    # 4. Normalize time formats: 05H03 → 05:03
    text = re.sub(r"(\d{1,2})H(\d{2})", r"\1:\2", text)

    # 5. Normalize spaces and line breaks
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()
