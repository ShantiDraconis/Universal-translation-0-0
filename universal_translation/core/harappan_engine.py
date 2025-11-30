"""
universal_translation/core/harappan_engine.py

Harappan sign decoding and encoding utilities.

This module provides functionality for:
- Decoding Harappan sign sequences to symbolic representations
- Encoding symbolic representations to sign IDs
- Loading and querying the Harappan sign database

Example:
    >>> from universal_translation.core.harappan_engine import decode_sequence
    >>> result = decode_sequence([1, 8, 15])
    >>> print(result)
    'SIGN_1 SIGN_8 SIGN_15'
"""

from typing import List, Dict, Optional, Any
from pathlib import Path
import json

# Default sign categories based on Mahadevan classification
SIGN_CATEGORIES = {
    (1, 7): "Anthropomorphic",
    (8, 23): "Zoomorphic",
    (24, 40): "Objects",
    (41, 50): "Numerals",
    (51, 70): "Geometric",
    (71, 80): "Botanical",
    (81, 89): "Architecture",
    (90, 94): "Transport",
    (95, 100): "Tools",
    (101, 108): "Body Parts",
    (109, 112): "Celestial",
    (113, 116): "Weather",
    (117, 128): "Geography",
    (129, 140): "Titles",
    (141, 416): "Compound",
    (417, 417): "Markers",
}


def decode_sequence(sign_ids: List[int]) -> str:
    """
    Decode a sequence of Harappan sign IDs into a symbolic string.

    Parameters
    ----------
    sign_ids : List[int]
        Numeric identifiers (e.g., Wells or Mahadevan indices).

    Returns
    -------
    str
        A symbolic representation of the sign sequence.
    """
    return " ".join(f"SIGN_{sid}" for sid in sign_ids)


def encode_sequence(symbols: str) -> List[int]:
    """
    Encode a symbolic representation into Harappan sign IDs.

    Parameters
    ----------
    symbols : str
        A symbolic string representation.

    Returns
    -------
    List[int]
        List of sign IDs.
    """
    # Extract numbers from SIGN_X patterns
    import re

    pattern = r"SIGN_(\d+)"
    matches = re.findall(pattern, symbols)
    return [int(m) for m in matches]


def get_sign_category(sign_id: int) -> str:
    """
    Get the category of a Harappan sign by its ID.

    Parameters
    ----------
    sign_id : int
        The Mahadevan sign index (1-417).

    Returns
    -------
    str
        Category name or 'Unknown'.
    """
    for (start, end), category in SIGN_CATEGORIES.items():
        if start <= sign_id <= end:
            return category
    return "Unknown"


def get_universal_code(sign_id: int) -> str:
    """
    Convert a Harappan sign ID to Universal 0/0 code format.

    The Universal 0/0 coding system uses: 00-[CATEGORY]-[NUMBER]

    Parameters
    ----------
    sign_id : int
        The Mahadevan sign index.

    Returns
    -------
    str
        Universal 0/0 code.
    """
    category_map = {
        "Anthropomorphic": "HUM",
        "Zoomorphic": "ANI",
        "Objects": "OBJ",
        "Numerals": "NUM",
        "Geometric": "GEO",
        "Botanical": "BOT",
        "Architecture": "ARC",
        "Transport": "TRN",
        "Tools": "TOL",
        "Body Parts": "BOD",
        "Celestial": "CEL",
        "Weather": "WEA",
        "Geography": "GEG",
        "Titles": "TTL",
        "Compound": "CMP",
        "Markers": "MRK",
    }

    category = get_sign_category(sign_id)
    code = category_map.get(category, "UNK")
    return f"00-{code}-{sign_id:03d}"


def decode_to_universal(sign_ids: List[int]) -> List[Dict[str, Any]]:
    """
    Decode Harappan sign IDs to detailed Universal 0/0 format.

    Parameters
    ----------
    sign_ids : List[int]
        List of Mahadevan sign indices.

    Returns
    -------
    List[Dict[str, Any]]
        List of decoded sign information.
    """
    return [
        {
            "mahadevan_id": sid,
            "universal_code": get_universal_code(sid),
            "category": get_sign_category(sid),
            "symbolic": f"SIGN_{sid}",
        }
        for sid in sign_ids
    ]


def load_sign_database(data_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Load the Harappan sign database from JSON file.

    Parameters
    ----------
    data_path : Optional[Path]
        Path to the JSON file. If None, uses the default location.

    Returns
    -------
    Dict[str, Any]
        The sign database with metadata and signs.
    """
    if data_path is None:
        # Default path relative to this module
        module_dir = Path(__file__).parent.parent
        data_path = module_dir / "datasets" / "harappan" / "harappan_417_signs.json"

    if not data_path.exists():
        # Try alternative location
        alt_path = (
            Path(__file__).parent.parent.parent
            / "harappan-00-universal"
            / "data"
            / "harappan_signs"
            / "harappan_417_signs.json"
        )
        if alt_path.exists():
            data_path = alt_path
        else:
            return {"metadata": {}, "signs": []}

    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


def search_signs(query: str, database: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Search for signs matching a query string.

    Parameters
    ----------
    query : str
        Search query (matches against description and category).
    database : Optional[Dict[str, Any]]
        Sign database. If None, loads the default database.

    Returns
    -------
    List[Dict[str, Any]]
        List of matching signs.
    """
    if database is None:
        database = load_sign_database()

    query_lower = query.lower()
    results = []

    for sign in database.get("signs", []):
        description = sign.get("description", "").lower()
        category = sign.get("category", "").lower()

        if query_lower in description or query_lower in category:
            results.append(sign)

    return results
