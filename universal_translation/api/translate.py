"""
universal_translation/api/translate.py

High-level translation interface functions.

This module provides the main API entry points for:
- Text translation
- Harappan decoding
- Batch translation

Example:
    >>> from universal_translation.api.translate import translate
    >>> result = translate("Hello world")
    >>> print(result["synthesis"]["symbolic_synthesis"])
"""

from typing import Dict, Any, List, Optional

from universal_translation.core.pipeline import translate_text, full_pipeline, translate_harappan


def translate(text: str, mode: str = "standard") -> Dict[str, Any]:
    """
    Translate a text using the Universal Translation Engine.

    Parameters
    ----------
    text : str
        Input text to translate.
    mode : str
        Translation mode:
        - "standard": Basic translation with all stages
        - "full": Complete 10-stage pipeline
        - "simple": Quick tokenization and phoneme analysis only

    Returns
    -------
    Dict[str, Any]
        Translation results.
    """
    if mode == "full":
        return full_pipeline(text, include_inversions=True)
    elif mode == "simple":
        return translate_text(text, stages=["tokenize", "phonemes"])
    else:  # standard
        return translate_text(text)


def translate_batch(texts: List[str], mode: str = "standard") -> List[Dict[str, Any]]:
    """
    Translate multiple texts.

    Parameters
    ----------
    texts : List[str]
        List of texts to translate.
    mode : str
        Translation mode (see translate() for options).

    Returns
    -------
    List[Dict[str, Any]]
        List of translation results.
    """
    return [translate(text, mode) for text in texts]


def decode_harappan(sign_ids: List[int]) -> Dict[str, Any]:
    """
    Decode a sequence of Harappan sign IDs.

    Parameters
    ----------
    sign_ids : List[int]
        List of Mahadevan sign indices (1-417).

    Returns
    -------
    Dict[str, Any]
        Decoded sign information and analysis.
    """
    return translate_harappan(sign_ids)


def analyze_numerology(text: str) -> Dict[str, Any]:
    """
    Perform numerological analysis on text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    Dict[str, Any]
        Numerological analysis results.
    """
    from universal_translation.core.numerology_engine import analyze_phrase

    return analyze_phrase(text)


def get_symbolic_meaning(text: str) -> Dict[str, Any]:
    """
    Get symbolic/archetypal meanings for text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    Dict[str, Any]
        Symbolic analysis including elements, archetypes, and polarity.
    """
    from universal_translation.core.tokenizer import basic_tokenize
    from universal_translation.core.semiotics_engine import annotate_symbols, collapse_to_universal

    tokens = basic_tokenize(text)
    annotations = annotate_symbols(tokens)
    synthesis = collapse_to_universal(annotations)

    return {
        "tokens": tokens,
        "annotations": annotations,
        "synthesis": synthesis,
    }


def search_harappan_signs(query: str) -> List[Dict[str, Any]]:
    """
    Search for Harappan signs matching a query.

    Parameters
    ----------
    query : str
        Search query.

    Returns
    -------
    List[Dict[str, Any]]
        Matching signs.
    """
    from universal_translation.core.harappan_engine import search_signs

    return search_signs(query)


def get_universal_phrase(text: str) -> str:
    """
    Generate the Universal 0/0 phrase for text.

    This is the final output of the 10-stage pipeline,
    summarizing the text's universal meaning.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    str
        Universal phrase in format: "Universal Translation 0/0: ..."
    """
    result = full_pipeline(text)
    return result.get("stage_10_universal", f"Universal Translation 0/0: {text}")
