"""
universal_translation/utils/converters.py

Converters between different symbol/phoneme formats.

This module provides conversion utilities for:
- Case transformations
- IPA to various phonetic notations
- Sign ID format conversions
- Unicode normalization

Example:
    >>> from universal_translation.utils.converters import to_upper
    >>> tokens = ["hello", "world"]
    >>> print(to_upper(tokens))
    ['HELLO', 'WORLD']
"""

from typing import List, Dict, Any, Optional
import unicodedata


def to_upper(tokens: List[str]) -> List[str]:
    """
    Convert tokens to uppercase.

    Parameters
    ----------
    tokens : List[str]
        List of tokens.

    Returns
    -------
    List[str]
        Uppercase tokens.
    """
    return [t.upper() for t in tokens]


def to_lower(tokens: List[str]) -> List[str]:
    """
    Convert tokens to lowercase.

    Parameters
    ----------
    tokens : List[str]
        List of tokens.

    Returns
    -------
    List[str]
        Lowercase tokens.
    """
    return [t.lower() for t in tokens]


def normalize_unicode(text: str, form: str = "NFC") -> str:
    """
    Normalize Unicode text.

    Parameters
    ----------
    text : str
        Input text.
    form : str
        Normalization form: 'NFC', 'NFD', 'NFKC', or 'NFKD'.

    Returns
    -------
    str
        Normalized text.
    """
    return unicodedata.normalize(form, text)


def remove_diacritics(text: str) -> str:
    """
    Remove diacritical marks from text.

    Parameters
    ----------
    text : str
        Input text with possible diacritics.

    Returns
    -------
    str
        Text with diacritics removed.
    """
    # Decompose to separate base characters from diacritics
    decomposed = unicodedata.normalize("NFD", text)
    # Keep only non-combining characters
    return "".join(c for c in decomposed if not unicodedata.combining(c))


def mahadevan_to_wells(sign_id: str) -> Optional[str]:
    """
    Convert Mahadevan sign ID to Wells format.

    Note: This is a placeholder. Actual conversion requires
    a proper mapping table.

    Parameters
    ----------
    sign_id : str
        Mahadevan sign ID (e.g., "M-001").

    Returns
    -------
    Optional[str]
        Wells format sign ID or None if not mappable.
    """
    import re

    match = re.match(r"M-?(\d+)", sign_id)
    if match:
        number = int(match.group(1))
        # Placeholder: assumes 1:1 mapping for low numbers
        if 1 <= number <= 417:
            return f"W-{number:03d}"

    return None


def wells_to_mahadevan(sign_id: str) -> Optional[str]:
    """
    Convert Wells sign ID to Mahadevan format.

    Note: This is a placeholder. Actual conversion requires
    a proper mapping table.

    Parameters
    ----------
    sign_id : str
        Wells sign ID (e.g., "W-001").

    Returns
    -------
    Optional[str]
        Mahadevan format sign ID or None if not mappable.
    """
    import re

    match = re.match(r"W-?(\d+)", sign_id)
    if match:
        number = int(match.group(1))
        # Placeholder: assumes 1:1 mapping for low numbers
        if 1 <= number <= 417:
            return f"M-{number:03d}"

    return None


def sign_id_to_universal(sign_id: str) -> str:
    """
    Convert any sign ID format to Universal 0/0 code.

    Parameters
    ----------
    sign_id : str
        Sign ID in any format (M-xxx, W-xxx, or numeric).

    Returns
    -------
    str
        Universal 0/0 code.
    """
    import re

    # Extract numeric part
    match = re.search(r"(\d+)", sign_id)
    if match:
        number = int(match.group(1))
        from universal_translation.core.harappan_engine import get_universal_code

        return get_universal_code(number)

    return f"00-UNK-{sign_id}"


def ipa_to_xsampa(ipa: str) -> str:
    """
    Convert IPA transcription to X-SAMPA notation.

    X-SAMPA (Extended Speech Assessment Methods Phonetic Alphabet)
    is an ASCII representation of IPA.

    Parameters
    ----------
    ipa : str
        IPA transcription.

    Returns
    -------
    str
        X-SAMPA notation.
    """
    # Basic IPA to X-SAMPA mapping
    mapping = {
        "ɑ": "A", "æ": "{", "ɐ": "6", "ɒ": "Q",
        "ɔ": "O", "ə": "@", "ɛ": "E", "ɜ": "3",
        "ɪ": "I", "ʊ": "U", "ʌ": "V", "ø": "2",
        "œ": "9", "ɤ": "7", "ɯ": "M",
        "ʃ": "S", "ʒ": "Z", "θ": "T", "ð": "D",
        "ŋ": "N", "ɲ": "J", "ʔ": "?", "ɹ": "r\\",
        "ɻ": "r\\`", "ʁ": "R", "ɾ": "4", "ɽ": "r`",
        "ʎ": "L", "ɬ": "K", "ɮ": "K\\",
        "ː": ":", "ˈ": "\"", "ˌ": "%",
    }

    result = []
    for char in ipa:
        result.append(mapping.get(char, char))

    return "".join(result)


def tokens_to_csv_row(tokens: List[str], analysis: Dict[str, Any]) -> Dict[str, str]:
    """
    Convert tokens and analysis to a CSV row format.

    Parameters
    ----------
    tokens : List[str]
        List of tokens.
    analysis : Dict[str, Any]
        Analysis results.

    Returns
    -------
    Dict[str, str]
        Dictionary suitable for CSV output.
    """
    return {
        "input": " ".join(tokens),
        "token_count": str(len(tokens)),
        "phonemes": str(analysis.get("phonemes", [])),
        "symbolic_tags": str(analysis.get("symbolic", [])),
        "numerology_root": str(analysis.get("numerology", {}).get("total_root", "")),
    }


def csv_row_to_sign(row: Dict[str, str]) -> Dict[str, Any]:
    """
    Convert a CSV row to a structured sign dictionary.

    Parameters
    ----------
    row : Dict[str, str]
        CSV row as dictionary.

    Returns
    -------
    Dict[str, Any]
        Structured sign data.
    """
    return {
        "sign_id": row.get("sign_id", row.get("id", "")),
        "description": row.get("description", ""),
        "category": row.get("category", "Unknown"),
        "variants": row.get("variants", "").split(";") if row.get("variants") else [],
        "unicode": row.get("unicode", ""),
    }
