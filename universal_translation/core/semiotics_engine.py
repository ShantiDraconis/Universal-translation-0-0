"""
universal_translation/core/semiotics_engine.py

Symbolic and semiotic layer for the Universal Translation Engine 0/0.

This module handles:
- Symbol tagging and classification
- Archetypal category mapping
- Integration with the indeterminate constant I = 0/0
- Mappings between linguistic units and symbolic structures

The semiotic layer connects phonetic/lexical analysis to deeper
symbolic and archetypal meanings.

Example:
    >>> from universal_translation.core.semiotics_engine import annotate_symbols
    >>> annotations = annotate_symbols(["fire", "water"])
    >>> print(annotations[0])
    {'token': 'fire', 'symbolic_tags': ['element:fire'], ...}
"""

from typing import Any, Dict, List, Optional

# Universal archetypal categories
ARCHETYPES = {
    "elements": ["fire", "water", "earth", "air", "ether", "void"],
    "celestial": ["sun", "moon", "star", "sky", "cosmos", "light", "dark"],
    "life": ["birth", "death", "growth", "decay", "seed", "fruit", "tree"],
    "human": ["father", "mother", "child", "elder", "warrior", "healer", "sage"],
    "sacred": ["god", "goddess", "spirit", "soul", "prayer", "ritual", "temple"],
    "nature": ["river", "mountain", "sea", "forest", "desert", "rain", "wind"],
    "animals": ["fish", "bird", "snake", "bull", "lion", "elephant", "horse"],
    "body": ["eye", "hand", "heart", "head", "foot", "mouth", "breath"],
}

# Element keyword mappings
ELEMENT_KEYWORDS = {
    "fire": ["fire", "flame", "burn", "hot", "sun", "light", "energy", "passion"],
    "water": ["water", "river", "sea", "ocean", "rain", "flow", "emotion", "moon"],
    "earth": ["earth", "ground", "stone", "mountain", "stable", "solid", "material"],
    "air": ["air", "wind", "breath", "sky", "thought", "mind", "spirit", "sound"],
    "ether": ["void", "space", "cosmos", "infinite", "eternal", "potential", "zero"],
}

# Symbolic polarity
POLARITY_WORDS = {
    "positive": ["light", "day", "sun", "fire", "active", "masculine", "yang", "create"],
    "negative": ["dark", "night", "moon", "water", "passive", "feminine", "yin", "dissolve"],
    "neutral": ["balance", "center", "middle", "equal", "harmony", "zero", "void"],
}


def annotate_symbols(tokens: List[str]) -> List[Dict[str, Any]]:
    """
    Attach symbolic metadata to each token.

    Parameters
    ----------
    tokens : List[str]
        List of textual tokens or sign identifiers.

    Returns
    -------
    List[Dict[str, Any]]
        Each entry contains:
        - token: original token
        - symbolic_tags: list of symbolic labels
        - archetype: detected archetype category
        - element: associated element
        - polarity: symbolic polarity (positive/negative/neutral)
        - numerological_value: optional mapping to 0/0 numerology
    """
    annotated = []
    for t in tokens:
        tags = get_symbolic_tags(t)
        archetype = detect_archetype(t)
        element = detect_element(t)
        polarity = detect_polarity(t)

        annotated.append(
            {
                "token": t,
                "symbolic_tags": tags,
                "archetype": archetype,
                "element": element,
                "polarity": polarity,
                "numerological_value": None,  # Filled by numerology engine
            }
        )
    return annotated


def get_symbolic_tags(token: str) -> List[str]:
    """
    Generate symbolic tags for a token.

    Parameters
    ----------
    token : str
        Input token.

    Returns
    -------
    List[str]
        List of symbolic tag strings.
    """
    token_lower = token.lower()
    tags = []

    # Check archetypes
    for category, words in ARCHETYPES.items():
        if token_lower in words:
            tags.append(f"archetype:{category}")

    # Check elements
    for element, keywords in ELEMENT_KEYWORDS.items():
        if token_lower in keywords:
            tags.append(f"element:{element}")

    # Check polarity
    for polarity, words in POLARITY_WORDS.items():
        if token_lower in words:
            tags.append(f"polarity:{polarity}")

    return tags if tags else ["unclassified"]


def detect_archetype(token: str) -> Optional[str]:
    """
    Detect the primary archetype category for a token.

    Parameters
    ----------
    token : str
        Input token.

    Returns
    -------
    Optional[str]
        Archetype category name or None.
    """
    token_lower = token.lower()

    for category, words in ARCHETYPES.items():
        if token_lower in words:
            return category

    return None


def detect_element(token: str) -> Optional[str]:
    """
    Detect the associated element for a token.

    Parameters
    ----------
    token : str
        Input token.

    Returns
    -------
    Optional[str]
        Element name or None.
    """
    token_lower = token.lower()

    for element, keywords in ELEMENT_KEYWORDS.items():
        if token_lower in keywords:
            return element

    return None


def detect_polarity(token: str) -> str:
    """
    Detect the symbolic polarity of a token.

    Parameters
    ----------
    token : str
        Input token.

    Returns
    -------
    str
        Polarity: 'positive', 'negative', or 'neutral'.
    """
    token_lower = token.lower()

    for polarity, words in POLARITY_WORDS.items():
        if token_lower in words:
            return polarity

    return "neutral"


def collapse_to_universal(annotations: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Collapse symbolic annotations into a unified universal interpretation.

    This implements the 0/0 semiotic operator, which transforms
    diverse symbolic elements into a coherent archetypal synthesis.

    Parameters
    ----------
    annotations : List[Dict[str, Any]]
        List of annotated tokens.

    Returns
    -------
    Dict[str, Any]
        Unified interpretation containing:
        - dominant_elements: most frequent elements
        - dominant_archetypes: most frequent archetypes
        - overall_polarity: net polarity
        - symbolic_synthesis: textual interpretation
    """
    elements = []
    archetypes = []
    polarities = []

    for ann in annotations:
        if ann.get("element"):
            elements.append(ann["element"])
        if ann.get("archetype"):
            archetypes.append(ann["archetype"])
        polarities.append(ann.get("polarity", "neutral"))

    # Count frequencies
    from collections import Counter

    element_counts = Counter(elements)
    archetype_counts = Counter(archetypes)
    polarity_counts = Counter(polarities)

    # Determine dominants
    dominant_elements = [e for e, _ in element_counts.most_common(2)]
    dominant_archetypes = [a for a, _ in archetype_counts.most_common(2)]

    # Calculate net polarity
    pos = polarity_counts.get("positive", 0)
    neg = polarity_counts.get("negative", 0)
    if pos > neg:
        overall_polarity = "positive"
    elif neg > pos:
        overall_polarity = "negative"
    else:
        overall_polarity = "balanced"

    # Generate synthesis
    synthesis = generate_synthesis(dominant_elements, dominant_archetypes, overall_polarity)

    return {
        "dominant_elements": dominant_elements,
        "dominant_archetypes": dominant_archetypes,
        "overall_polarity": overall_polarity,
        "element_distribution": dict(element_counts),
        "archetype_distribution": dict(archetype_counts),
        "symbolic_synthesis": synthesis,
    }


def generate_synthesis(
    elements: List[str], archetypes: List[str], polarity: str
) -> str:
    """
    Generate a textual synthesis of symbolic elements.

    Parameters
    ----------
    elements : List[str]
        Dominant elements.
    archetypes : List[str]
        Dominant archetypes.
    polarity : str
        Overall polarity.

    Returns
    -------
    str
        Textual interpretation.
    """
    parts = []

    if elements:
        parts.append(f"Elemental focus: {', '.join(elements)}")
    if archetypes:
        parts.append(f"Archetypal themes: {', '.join(archetypes)}")
    parts.append(f"Overall energy: {polarity}")

    return " | ".join(parts) if parts else "No distinct symbolic pattern detected"
