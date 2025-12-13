"""
universal_translation/core/numerology_engine.py

Numerology and 0/0-based symbolic mappings.

This module implements numerological analysis based on:
- Pythagorean numerology
- Kabalistic gematria
- 0/0 indeterminate symbolic system

The 0/0 constant represents creative indeterminacy - the point
where origin and end converge.

Example:
    >>> from universal_translation.core.numerology_engine import word_value
    >>> value = word_value("hello")
    >>> print(value)  # Sum of letter values
    52
"""

from typing import Dict, Any, Optional, List

# Pythagorean numerology mapping (A=1, B=2, ..., I=9, J=1, ...)
PYTHAGOREAN_MAP = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
    "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9,
    "s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6, "y": 7, "z": 8,
}

# Hebrew Gematria mapping
HEBREW_GEMATRIA = {
    "א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8, "ט": 9,
    "י": 10, "כ": 20, "ל": 30, "מ": 40, "נ": 50, "ס": 60, "ע": 70, "פ": 80, "צ": 90,
    "ק": 100, "ר": 200, "ש": 300, "ת": 400,
}

# Universal symbolic values (0/0 system)
SYMBOLIC_VALUES = {
    1: {"archetype": "Unity/Beginning", "element": "Fire", "planet": "Sun"},
    2: {"archetype": "Duality/Balance", "element": "Water", "planet": "Moon"},
    3: {"archetype": "Creation/Growth", "element": "Fire", "planet": "Jupiter"},
    4: {"archetype": "Stability/Foundation", "element": "Earth", "planet": "Uranus"},
    5: {"archetype": "Change/Freedom", "element": "Air", "planet": "Mercury"},
    6: {"archetype": "Harmony/Love", "element": "Earth", "planet": "Venus"},
    7: {"archetype": "Mystery/Wisdom", "element": "Water", "planet": "Neptune"},
    8: {"archetype": "Power/Karma", "element": "Earth", "planet": "Saturn"},
    9: {"archetype": "Completion/Universal", "element": "Fire", "planet": "Mars"},
}


def word_value(word: str, system: str = "pythagorean") -> int:
    """
    Calculate the numerological value of a word.

    Parameters
    ----------
    word : str
        The word to analyze.
    system : str
        Numerology system: 'pythagorean', 'hebrew', or 'ordinal'.

    Returns
    -------
    int
        The numerological value.
    """
    word_lower = word.lower()

    if system == "pythagorean":
        return sum(PYTHAGOREAN_MAP.get(c, 0) for c in word_lower)
    elif system == "hebrew":
        return sum(HEBREW_GEMATRIA.get(c, 0) for c in word)
    else:  # ordinal
        return sum(ord(c) - ord("a") + 1 for c in word_lower if c.isalpha())


def reduce_to_root(value: int) -> int:
    """
    Reduce a number to its root digit (1-9).

    Master numbers (11, 22, 33) are preserved in some traditions,
    but this function reduces all numbers for simplicity.

    Parameters
    ----------
    value : int
        The number to reduce.

    Returns
    -------
    int
        Root digit (1-9) or 0 if input is 0.
    """
    if value == 0:
        return 0

    while value > 9:
        value = sum(int(d) for d in str(value))

    return value


def normalize_to_zero_over_zero(value: int) -> float:
    """
    Map an integer value into a symbolic 0/0-inspired scale.

    The 0/0 indeterminate represents infinite potential.
    This function maps values to a [0, 1] scale representing
    the degree of manifestation from potential (0) to actualized (1).

    Parameters
    ----------
    value : int
        Input value.

    Returns
    -------
    float
        Normalized value in [0, 1] range.
    """
    if value == 0:
        return 0.0

    # Map to 0-1 using the root digit
    root = reduce_to_root(value)
    return root / 9.0


def get_symbolic_meaning(value: int) -> Dict[str, Any]:
    """
    Get the symbolic meaning associated with a numerological value.

    Parameters
    ----------
    value : int
        The numerological value (will be reduced to root).

    Returns
    -------
    Dict[str, Any]
        Symbolic associations including archetype, element, planet.
    """
    root = reduce_to_root(value)

    if root == 0:
        return {
            "root": 0,
            "archetype": "Void/Potential",
            "element": "Ether",
            "planet": "None",
            "description": "The indeterminate 0/0 - pure potential before manifestation",
        }

    base = SYMBOLIC_VALUES.get(root, {})
    return {
        "root": root,
        "original_value": value,
        **base,
    }


def analyze_word(word: str) -> Dict[str, Any]:
    """
    Perform complete numerological analysis of a word.

    Parameters
    ----------
    word : str
        The word to analyze.

    Returns
    -------
    Dict[str, Any]
        Complete analysis including all systems and symbolism.
    """
    pythagorean = word_value(word, "pythagorean")
    ordinal = word_value(word, "ordinal")

    return {
        "word": word,
        "pythagorean_value": pythagorean,
        "pythagorean_root": reduce_to_root(pythagorean),
        "ordinal_value": ordinal,
        "ordinal_root": reduce_to_root(ordinal),
        "zero_over_zero_scale": normalize_to_zero_over_zero(pythagorean),
        "symbolic_meaning": get_symbolic_meaning(pythagorean),
    }


def analyze_phrase(phrase: str) -> Dict[str, Any]:
    """
    Perform numerological analysis of a complete phrase.

    Parameters
    ----------
    phrase : str
        The phrase to analyze.

    Returns
    -------
    Dict[str, Any]
        Analysis of each word and the phrase total.
    """
    words = phrase.split()
    word_analyses = [analyze_word(w) for w in words]

    total = sum(a["pythagorean_value"] for a in word_analyses)

    return {
        "phrase": phrase,
        "word_analyses": word_analyses,
        "total_value": total,
        "total_root": reduce_to_root(total),
        "phrase_meaning": get_symbolic_meaning(total),
    }
