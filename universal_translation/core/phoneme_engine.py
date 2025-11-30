"""
universal_translation/core/phoneme_engine.py

Phoneme engine for universal phonetic representation.

This module provides mappings between text tokens and universal phoneme
representations, supporting multiple language families including:
- Indo-European
- Dravidian
- Sino-Tibetan
- Afro-Asiatic
- Tupi-Guarani

Example:
    >>> from universal_translation.core.phoneme_engine import to_universal_phonemes
    >>> phonemes = to_universal_phonemes(["hello", "world"])
    >>> print(phonemes[0])
    {'token': 'hello', 'ipa': 'hello', 'family': 'unknown'}
"""

from typing import List, Dict, Any, Optional

# Basic IPA consonant mappings (simplified)
IPA_CONSONANTS = {
    "b": "b", "c": "k", "d": "d", "f": "f", "g": "g",
    "h": "h", "j": "dʒ", "k": "k", "l": "l", "m": "m",
    "n": "n", "p": "p", "q": "k", "r": "r", "s": "s",
    "t": "t", "v": "v", "w": "w", "x": "ks", "y": "j", "z": "z",
    "ch": "tʃ", "sh": "ʃ", "th": "θ", "ng": "ŋ", "ph": "f",
    "gh": "ɡ", "kh": "kʰ", "dh": "dʰ", "bh": "bʰ",
}

# Basic IPA vowel mappings (simplified)
IPA_VOWELS = {
    "a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
    "á": "aː", "é": "eː", "í": "iː", "ó": "oː", "ú": "uː",
    "ã": "ã", "ẽ": "ẽ", "ĩ": "ĩ", "õ": "õ", "ũ": "ũ",
    "ai": "aɪ", "ei": "eɪ", "oi": "ɔɪ", "au": "aʊ", "ou": "oʊ",
}

# Language family patterns
FAMILY_PATTERNS = {
    "indo_european": ["the", "is", "was", "be", "have", "do", "say", "go", "can", "will"],
    "dravidian": ["amma", "appa", "akka", "anna", "thambi", "thangai"],
    "tupi_guarani": ["pirá", "jaguara", "paranã", "ybyrá", "mboi", "guyrá"],
    "sino_tibetan": ["shi", "bu", "wo", "ni", "ta", "men", "zhe", "ge"],
    "afro_asiatic": ["shalom", "salaam", "akh", "el", "yod", "aleph"],
}


def to_universal_phonemes(tokens: List[str]) -> List[Dict[str, Any]]:
    """
    Map tokens to a universal phoneme representation.

    This is a placeholder implementation. The Copilot agent
    should extend this to support multiple language families.

    Parameters
    ----------
    tokens : List[str]
        List of text tokens.

    Returns
    -------
    List[Dict[str, Any]]
        Each entry contains:
        - token: original token
        - ipa: IPA transcription (approximate)
        - family: detected language family
    """
    return [
        {
            "token": t,
            "ipa": text_to_ipa(t),
            "family": detect_family(t),
        }
        for t in tokens
    ]


def text_to_ipa(text: str) -> str:
    """
    Convert text to approximate IPA transcription.

    This is a simplified conversion that maps individual characters.
    For accurate IPA transcription, language-specific rules and
    dictionaries should be used.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    str
        Approximate IPA transcription.
    """
    text_lower = text.lower()
    result = []
    i = 0

    while i < len(text_lower):
        # Check for digraphs first
        if i + 1 < len(text_lower):
            digraph = text_lower[i : i + 2]
            if digraph in IPA_CONSONANTS:
                result.append(IPA_CONSONANTS[digraph])
                i += 2
                continue
            if digraph in IPA_VOWELS:
                result.append(IPA_VOWELS[digraph])
                i += 2
                continue

        # Single character
        char = text_lower[i]
        if char in IPA_CONSONANTS:
            result.append(IPA_CONSONANTS[char])
        elif char in IPA_VOWELS:
            result.append(IPA_VOWELS[char])
        elif char.isalpha():
            result.append(char)
        i += 1

    return "".join(result)


def detect_family(token: str) -> str:
    """
    Detect the probable language family for a token.

    This is a heuristic-based detection using pattern matching.
    For accurate classification, more sophisticated methods should be used.

    Parameters
    ----------
    token : str
        Input token.

    Returns
    -------
    str
        Detected language family or 'unknown'.
    """
    token_lower = token.lower()

    for family, patterns in FAMILY_PATTERNS.items():
        if token_lower in patterns:
            return family

    # Heuristic based on character patterns
    if any(c in token_lower for c in "ãẽĩõũ"):
        return "tupi_guarani"
    if any(c in token_lower for c in "āīūṛḷṃḥ"):
        return "indo_european_indic"
    if any(c in token_lower for c in "אבגדהוזחטיכלמנסעפצקרשת"):
        return "afro_asiatic_semitic"

    return "unknown"


def get_phoneme_features(ipa: str) -> Dict[str, Any]:
    """
    Extract phonetic features from an IPA symbol.

    Parameters
    ----------
    ipa : str
        IPA symbol.

    Returns
    -------
    Dict[str, Any]
        Dictionary of phonetic features.
    """
    vowels = set("aeiouɑɛɪɔʊæəɐʌɒɜɞɘɤɯɨʉ")
    nasals = set("mnɲŋɴ")
    plosives = set("pbtdkgʔ")
    fricatives = set("fvθðszʃʒxɣhɦ")

    features = {
        "symbol": ipa,
        "is_vowel": ipa in vowels,
        "is_consonant": ipa not in vowels and ipa.isalpha(),
        "is_nasal": ipa in nasals,
        "is_plosive": ipa in plosives,
        "is_fricative": ipa in fricatives,
        "voiced": ipa in set("bdgvzʒmnɲŋɴ"),
    }

    return features
