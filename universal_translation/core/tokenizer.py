"""
universal_translation/core/tokenizer.py

Basic tokenizer for the Universal Translation Engine 0/0.

This module provides tokenization utilities for:
- Multilingual text tokenization
- Harappan sign segmentation
- Phoneme-level segmentation
- Symbolic markers for 0/0-based transformations

Example:
    >>> from universal_translation.core.tokenizer import basic_tokenize
    >>> tokens = basic_tokenize("Hello world")
    >>> print(tokens)
    ['Hello', 'world']
"""

from typing import List
import re


def basic_tokenize(text: str) -> List[str]:
    """
    Split text into basic tokens using whitespace.

    This is a placeholder implementation. The Copilot agent should
    refine this function over time to support:

    - multilingual tokenization,
    - Harappan sign segmentation,
    - phoneme-level segmentation,
    - symbolic markers for 0/0-based transformations.

    Parameters
    ----------
    text : str
        Input text to tokenize.

    Returns
    -------
    List[str]
        List of tokens.
    """
    return text.split()


def syllable_tokenize(text: str) -> List[str]:
    """
    Tokenize text into syllable-like units.

    This is a simplified syllable detection that splits on
    vowel boundaries. For accurate syllabification, language-specific
    rules should be applied.

    Parameters
    ----------
    text : str
        Input text to tokenize.

    Returns
    -------
    List[str]
        List of syllable-like tokens.
    """
    # Simple pattern: split after vowels followed by consonants
    vowels = "aeiouAEIOUáéíóúàèìòùâêîôûãẽĩõũäëïöü"
    syllables = []
    current = ""

    for char in text:
        current += char
        if char in vowels:
            syllables.append(current)
            current = ""

    if current:
        if syllables:
            syllables[-1] += current
        else:
            syllables.append(current)

    return [s for s in syllables if s.strip()]


def phoneme_tokenize(text: str) -> List[str]:
    """
    Tokenize text into phoneme-like units.

    This is a basic implementation that treats each character
    as a potential phoneme. For accurate phoneme extraction,
    IPA transcription should be used.

    Parameters
    ----------
    text : str
        Input text to tokenize.

    Returns
    -------
    List[str]
        List of phoneme-like tokens.
    """
    # Remove non-letter characters for phoneme analysis
    clean_text = re.sub(r"[^a-zA-ZáéíóúàèìòùâêîôûãẽĩõũäëïöüçñÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃẼĨÕŨÄËÏÖÜÇÑ]", " ", text)
    phonemes = []

    for word in clean_text.split():
        for char in word:
            phonemes.append(char.lower())
        phonemes.append(" ")  # Word boundary marker

    return [p for p in phonemes if p != " " or phonemes.count(" ") > 0][:-1] if phonemes else []


def harappan_sign_tokenize(sequence: str) -> List[str]:
    """
    Tokenize a Harappan sign sequence.

    Harappan sign sequences typically use delimiters like hyphens
    or commas between sign identifiers.

    Parameters
    ----------
    sequence : str
        A string of Harappan sign identifiers (e.g., "M-001-M-008-M-015").

    Returns
    -------
    List[str]
        List of individual sign identifiers.
    """
    # Split by common delimiters
    signs = re.split(r"[-,\s]+", sequence)
    # Filter out empty strings and reconstruct sign IDs
    result = []
    i = 0
    while i < len(signs):
        if signs[i].upper() in ("M", "W"):  # Mahadevan or Wells prefix
            if i + 1 < len(signs) and signs[i + 1].isdigit():
                result.append(f"{signs[i].upper()}-{signs[i + 1]}")
                i += 2
                continue
        if signs[i]:
            result.append(signs[i])
        i += 1

    return result
