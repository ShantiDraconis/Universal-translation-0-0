"""
universal_translation/core/pipeline.py

High-level translation pipeline for the Universal Translation Engine.

This module orchestrates the complete 10-stage translation pipeline:
1. Segmentation + Inversion
2. Dictionary 00 mapping
3. Harappan projection
4. 12 Language families
5. Symbolic 0/0 decoding
6. Archaeo-cosmological analysis
7. Numerology
8. Multiple translation
9. Final diagram
10. Universal phrase

Example:
    >>> from universal_translation.core.pipeline import translate_text
    >>> result = translate_text("Hello world")
    >>> print(result.keys())
    dict_keys(['tokens', 'phonemes', 'symbolic', 'numerology', 'synthesis'])
"""

from typing import Dict, Any, List, Optional

from universal_translation.core.tokenizer import basic_tokenize, syllable_tokenize
from universal_translation.core.phoneme_engine import to_universal_phonemes
from universal_translation.core.semiotics_engine import annotate_symbols, collapse_to_universal
from universal_translation.core.numerology_engine import analyze_phrase


def translate_text(text: str, stages: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Run the full symbolic translation pipeline on a text string.

    Parameters
    ----------
    text : str
        Input text to translate.
    stages : Optional[List[str]]
        List of stages to run. If None, runs all stages.
        Valid stages: 'tokenize', 'phonemes', 'symbolic', 'numerology', 'synthesis'

    Returns
    -------
    Dict[str, Any]
        Translation results including:
        - tokens: word-level tokens
        - syllables: syllable-level tokens
        - phonemes: phonetic analysis
        - symbolic: semiotic annotations
        - numerology: numerological analysis
        - synthesis: unified interpretation
    """
    if stages is None:
        stages = ["tokenize", "phonemes", "symbolic", "numerology", "synthesis"]

    result = {
        "input": text,
        "stages_applied": stages,
    }

    # Stage 1: Tokenization
    if "tokenize" in stages:
        tokens = basic_tokenize(text)
        syllables = syllable_tokenize(text)
        result["tokens"] = tokens
        result["syllables"] = syllables

    # Stage 2: Phoneme analysis
    if "phonemes" in stages:
        tokens = result.get("tokens", basic_tokenize(text))
        phonemes = to_universal_phonemes(tokens)
        result["phonemes"] = phonemes

    # Stage 3: Symbolic annotation
    if "symbolic" in stages:
        tokens = result.get("tokens", basic_tokenize(text))
        symbolic = annotate_symbols(tokens)
        result["symbolic"] = symbolic

    # Stage 4: Numerological analysis
    if "numerology" in stages:
        numerology = analyze_phrase(text)
        result["numerology"] = numerology

    # Stage 5: Synthesis
    if "synthesis" in stages:
        symbolic = result.get("symbolic", annotate_symbols(basic_tokenize(text)))
        synthesis = collapse_to_universal(symbolic)
        result["synthesis"] = synthesis

    return result


def translate_harappan(sign_ids: List[int]) -> Dict[str, Any]:
    """
    Translate a sequence of Harappan sign IDs.

    Parameters
    ----------
    sign_ids : List[int]
        List of Mahadevan sign indices.

    Returns
    -------
    Dict[str, Any]
        Translation results including decoded signs and analysis.
    """
    from universal_translation.core.harappan_engine import decode_to_universal

    decoded = decode_to_universal(sign_ids)

    # Create text from decoded signs for further analysis
    sign_text = " ".join(d["symbolic"] for d in decoded)

    return {
        "input_ids": sign_ids,
        "decoded_signs": decoded,
        "sign_text": sign_text,
        "analysis": translate_text(sign_text),
    }


def full_pipeline(
    text: str,
    include_inversions: bool = False,
    include_harappan_projection: bool = False,
) -> Dict[str, Any]:
    """
    Run the complete 10-stage Universal Translation pipeline.

    Parameters
    ----------
    text : str
        Input text.
    include_inversions : bool
        Whether to include inverted (reversed) analysis.
    include_harappan_projection : bool
        Whether to attempt Harappan sign projection.

    Returns
    -------
    Dict[str, Any]
        Complete pipeline results.
    """
    result = {
        "input": text,
        "pipeline_version": "0.1.0",
    }

    # Stage 1: Segmentation
    tokens = basic_tokenize(text)
    syllables = syllable_tokenize(text)
    result["stage_1_segmentation"] = {
        "tokens": tokens,
        "syllables": syllables,
    }

    if include_inversions:
        result["stage_1_segmentation"]["inverted"] = {
            "horizontal": text[::-1],
            "tokens_reversed": tokens[::-1],
        }

    # Stage 2: Phonemes / Universal mapping
    phonemes = to_universal_phonemes(tokens)
    result["stage_2_phonemes"] = phonemes

    # Stage 3: Harappan projection (placeholder)
    if include_harappan_projection:
        result["stage_3_harappan"] = {
            "status": "placeholder",
            "message": "Harappan projection requires trained mapping model",
        }

    # Stage 4: Language families (from phoneme analysis)
    families_detected = set(p["family"] for p in phonemes if p["family"] != "unknown")
    result["stage_4_families"] = list(families_detected) if families_detected else ["universal"]

    # Stage 5: Symbolic 0/0
    symbolic = annotate_symbols(tokens)
    result["stage_5_symbolic"] = symbolic

    # Stage 6: Archaeo-cosmological (synthesis of symbolic)
    synthesis = collapse_to_universal(symbolic)
    result["stage_6_archaeo"] = synthesis

    # Stage 7: Numerology
    numerology = analyze_phrase(text)
    result["stage_7_numerology"] = numerology

    # Stage 8: Multiple translations (placeholder)
    result["stage_8_translations"] = {
        "literal": text,
        "archetypal": synthesis.get("symbolic_synthesis", text),
        "energetic": f"Energy signature: {numerology.get('total_root', 0)}",
    }

    # Stage 9: Diagram data
    result["stage_9_diagram"] = {
        "token_count": len(tokens),
        "syllable_count": len(syllables),
        "phoneme_families": result["stage_4_families"],
        "dominant_elements": synthesis.get("dominant_elements", []),
        "dominant_archetypes": synthesis.get("dominant_archetypes", []),
        "numerological_root": numerology.get("total_root", 0),
    }

    # Stage 10: Universal phrase
    elements = ", ".join(synthesis.get("dominant_elements", ["universal"]))
    archetypes = ", ".join(synthesis.get("dominant_archetypes", ["essence"]))
    root = numerology.get("total_root", 0)

    result["stage_10_universal"] = (
        f"Universal Translation 0/0: {elements} | {archetypes} | Root {root}"
    )

    return result
