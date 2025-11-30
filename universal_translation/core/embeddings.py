"""
universal_translation/core/embeddings.py

Vector representations (embeddings) for symbols and tokens.

This module provides embedding utilities for:
- Creating dense vector representations of tokens
- Semantic similarity calculations
- Future integration with neural models

Example:
    >>> from universal_translation.core.embeddings import dummy_embedding
    >>> vec = dummy_embedding("hello")
    >>> print(vec)
    [0.9092974268256817, -0.4161468365471424]
"""

from typing import List, Dict, Any, Optional
import math


def dummy_embedding(token: str, dim: int = 2) -> List[float]:
    """
    Return a trivial deterministic embedding for demonstration.

    This creates a simple embedding based on the token's length
    and character values. For real applications, use pre-trained
    embeddings or learned representations.

    Parameters
    ----------
    token : str
        Input token.
    dim : int
        Embedding dimension (default: 2).

    Returns
    -------
    List[float]
        Embedding vector.
    """
    # Simple deterministic embedding based on token properties
    base = len(token) + sum(ord(c) for c in token)

    embedding = []
    for i in range(dim):
        val = math.sin(base * (i + 1) / 10.0)
        embedding.append(val)

    return embedding


def phoneme_embedding(ipa: str, dim: int = 8) -> List[float]:
    """
    Create an embedding for a phoneme based on its IPA representation.

    This uses phonetic features to create a more meaningful embedding
    than pure character-based methods.

    Parameters
    ----------
    ipa : str
        IPA transcription of the phoneme.
    dim : int
        Embedding dimension (default: 8).

    Returns
    -------
    List[float]
        Phoneme embedding vector.
    """
    # Phonetic feature encoding
    vowels = set("aeiouɑɛɪɔʊæəɐʌɒɜɞɘɤɯɨʉ")
    nasals = set("mnɲŋɴ")
    plosives = set("pbtdkgʔ")
    fricatives = set("fvθðszʃʒxɣhɦ")

    features = [
        1.0 if any(c in vowels for c in ipa) else 0.0,  # Is vowel
        1.0 if any(c in nasals for c in ipa) else 0.0,  # Is nasal
        1.0 if any(c in plosives for c in ipa) else 0.0,  # Is plosive
        1.0 if any(c in fricatives for c in ipa) else 0.0,  # Is fricative
        len(ipa) / 3.0,  # Normalized length
        sum(ord(c) for c in ipa) / 1000.0,  # Character value feature
    ]

    # Pad or truncate to desired dimension
    while len(features) < dim:
        features.append(math.sin(len(features) * sum(features)))

    return features[:dim]


def symbol_embedding(sign_id: int, category: str, dim: int = 16) -> List[float]:
    """
    Create an embedding for a Harappan sign or symbol.

    Parameters
    ----------
    sign_id : int
        The sign identifier (e.g., Mahadevan index).
    category : str
        The sign category (e.g., "Zoomorphic").
    dim : int
        Embedding dimension (default: 16).

    Returns
    -------
    List[float]
        Symbol embedding vector.
    """
    # Category encoding
    categories = [
        "Anthropomorphic", "Zoomorphic", "Objects", "Numerals",
        "Geometric", "Botanical", "Architecture", "Transport",
        "Tools", "Body Parts", "Celestial", "Weather",
        "Geography", "Titles", "Compound", "Markers",
    ]

    # One-hot for category
    category_vec = [1.0 if c == category else 0.0 for c in categories]

    # Position encoding for sign_id
    position = [
        math.sin(sign_id / 100.0),
        math.cos(sign_id / 100.0),
        sign_id / 417.0,  # Normalized position
    ]

    embedding = category_vec + position

    # Pad or truncate to desired dimension
    while len(embedding) < dim:
        embedding.append(0.0)

    return embedding[:dim]


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Calculate cosine similarity between two vectors.

    Parameters
    ----------
    vec1 : List[float]
        First vector.
    vec2 : List[float]
        Second vector.

    Returns
    -------
    float
        Cosine similarity (-1 to 1).
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same dimension")

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def find_similar(
    target: List[float],
    candidates: Dict[str, List[float]],
    top_k: int = 5,
) -> List[Dict[str, Any]]:
    """
    Find the most similar embeddings to a target.

    Parameters
    ----------
    target : List[float]
        Target embedding vector.
    candidates : Dict[str, List[float]]
        Dictionary mapping labels to embedding vectors.
    top_k : int
        Number of top results to return.

    Returns
    -------
    List[Dict[str, Any]]
        List of top matches with labels and similarity scores.
    """
    similarities = []

    for label, vec in candidates.items():
        sim = cosine_similarity(target, vec)
        similarities.append({"label": label, "similarity": sim})

    # Sort by similarity descending
    similarities.sort(key=lambda x: x["similarity"], reverse=True)

    return similarities[:top_k]


def create_embedding_index(
    items: List[Dict[str, Any]],
    embedding_fn: callable,
    label_key: str = "token",
) -> Dict[str, List[float]]:
    """
    Create an embedding index from a list of items.

    Parameters
    ----------
    items : List[Dict[str, Any]]
        List of items to embed.
    embedding_fn : callable
        Function that takes an item and returns an embedding.
    label_key : str
        Key to use as label in the index.

    Returns
    -------
    Dict[str, List[float]]
        Dictionary mapping labels to embeddings.
    """
    index = {}

    for item in items:
        label = item.get(label_key, str(item))
        embedding = embedding_fn(item)
        index[label] = embedding

    return index
