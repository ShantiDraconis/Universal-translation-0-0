"""
universal_translation/evaluation/metrics.py

Evaluation metrics for translations and symbolic mappings.

This module provides metrics for:
- Translation accuracy
- Symbol recognition
- Numerological consistency
- Human evaluation scoring

Example:
    >>> from universal_translation.evaluation.metrics import simple_accuracy
    >>> pred = ["a", "b", "c"]
    >>> gold = ["a", "b", "d"]
    >>> print(simple_accuracy(pred, gold))
    0.6666666666666666
"""

from typing import Sequence, List, Dict, Any, Optional
import math


def simple_accuracy(pred: Sequence[str], gold: Sequence[str]) -> float:
    """
    Compute a simple token-level accuracy metric.

    Parameters
    ----------
    pred : Sequence[str]
        Predicted tokens.
    gold : Sequence[str]
        Gold standard tokens.

    Returns
    -------
    float
        Accuracy score (0.0 to 1.0).
    """
    if not gold:
        return 0.0

    correct = sum(p == g for p, g in zip(pred, gold))
    return correct / len(gold)


def precision_recall_f1(
    pred: Sequence[str],
    gold: Sequence[str],
) -> Dict[str, float]:
    """
    Calculate precision, recall, and F1 score.

    Parameters
    ----------
    pred : Sequence[str]
        Predicted items.
    gold : Sequence[str]
        Gold standard items.

    Returns
    -------
    Dict[str, float]
        Dictionary with precision, recall, and f1 scores.
    """
    pred_set = set(pred)
    gold_set = set(gold)

    if not pred_set:
        precision = 0.0
    else:
        precision = len(pred_set & gold_set) / len(pred_set)

    if not gold_set:
        recall = 0.0
    else:
        recall = len(pred_set & gold_set) / len(gold_set)

    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)

    return {"precision": precision, "recall": recall, "f1": f1}


def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculate the Levenshtein (edit) distance between two strings.

    Parameters
    ----------
    s1 : str
        First string.
    s2 : str
        Second string.

    Returns
    -------
    int
        Number of edits needed to transform s1 into s2.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def normalized_edit_distance(s1: str, s2: str) -> float:
    """
    Calculate normalized edit distance (0.0 to 1.0).

    Parameters
    ----------
    s1 : str
        First string.
    s2 : str
        Second string.

    Returns
    -------
    float
        Normalized distance (0.0 = identical, 1.0 = completely different).
    """
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 0.0

    return levenshtein_distance(s1, s2) / max_len


def phoneme_accuracy(
    pred_phonemes: List[str],
    gold_phonemes: List[str],
) -> float:
    """
    Calculate phoneme-level accuracy.

    Parameters
    ----------
    pred_phonemes : List[str]
        Predicted phonemes.
    gold_phonemes : List[str]
        Gold standard phonemes.

    Returns
    -------
    float
        Phoneme accuracy score.
    """
    return simple_accuracy(pred_phonemes, gold_phonemes)


def symbol_recognition_score(
    pred_symbols: List[Dict[str, Any]],
    gold_symbols: List[Dict[str, Any]],
    key: str = "symbolic_tags",
) -> float:
    """
    Calculate symbol recognition score.

    Parameters
    ----------
    pred_symbols : List[Dict[str, Any]]
        Predicted symbol annotations.
    gold_symbols : List[Dict[str, Any]]
        Gold standard annotations.
    key : str
        Key to compare in the dictionaries.

    Returns
    -------
    float
        Recognition score.
    """
    if not gold_symbols:
        return 0.0

    scores = []
    for pred, gold in zip(pred_symbols, gold_symbols):
        pred_tags = set(pred.get(key, []))
        gold_tags = set(gold.get(key, []))

        if not gold_tags:
            continue

        overlap = len(pred_tags & gold_tags)
        score = overlap / len(gold_tags) if gold_tags else 0.0
        scores.append(score)

    return sum(scores) / len(scores) if scores else 0.0


def numerology_consistency(values: List[int]) -> float:
    """
    Calculate consistency score for numerological values.

    Measures how consistent the root values are across multiple calculations.

    Parameters
    ----------
    values : List[int]
        List of numerological root values (1-9).

    Returns
    -------
    float
        Consistency score (higher = more consistent).
    """
    if not values:
        return 0.0

    from collections import Counter

    counts = Counter(values)
    most_common_count = counts.most_common(1)[0][1]

    return most_common_count / len(values)


def human_evaluation_score(
    evaluations: List[Dict[str, int]],
    dimensions: Optional[List[str]] = None,
) -> Dict[str, float]:
    """
    Aggregate human evaluation scores.

    Parameters
    ----------
    evaluations : List[Dict[str, int]]
        List of evaluation dictionaries with dimension scores.
    dimensions : Optional[List[str]]
        Dimensions to aggregate. If None, uses all found dimensions.

    Returns
    -------
    Dict[str, float]
        Average scores per dimension.
    """
    if not evaluations:
        return {}

    if dimensions is None:
        dimensions = list(evaluations[0].keys())

    scores = {d: [] for d in dimensions}

    for eval_dict in evaluations:
        for dim in dimensions:
            if dim in eval_dict:
                scores[dim].append(eval_dict[dim])

    return {
        dim: sum(vals) / len(vals) if vals else 0.0
        for dim, vals in scores.items()
    }


def inter_annotator_agreement(
    annotations: List[List[str]],
) -> float:
    """
    Calculate simple inter-annotator agreement (percentage agreement).

    Parameters
    ----------
    annotations : List[List[str]]
        List of annotation lists from different annotators.

    Returns
    -------
    float
        Agreement score (0.0 to 1.0).
    """
    if len(annotations) < 2:
        return 1.0

    # Compare pairwise
    agreements = []
    for i in range(len(annotations)):
        for j in range(i + 1, len(annotations)):
            ann1 = annotations[i]
            ann2 = annotations[j]
            min_len = min(len(ann1), len(ann2))
            if min_len == 0:
                continue
            agree = sum(a == b for a, b in zip(ann1[:min_len], ann2[:min_len]))
            agreements.append(agree / min_len)

    return sum(agreements) / len(agreements) if agreements else 0.0


def benchmark_report(
    predictions: List[Dict[str, Any]],
    gold: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Generate a comprehensive benchmark report.

    Parameters
    ----------
    predictions : List[Dict[str, Any]]
        Predicted results.
    gold : List[Dict[str, Any]]
        Gold standard results.

    Returns
    -------
    Dict[str, Any]
        Benchmark report with various metrics.
    """
    report = {
        "sample_count": len(gold),
        "metrics": {},
    }

    # Token accuracy
    pred_tokens = [" ".join(p.get("tokens", [])) for p in predictions]
    gold_tokens = [" ".join(g.get("tokens", [])) for g in gold]
    report["metrics"]["token_match"] = simple_accuracy(pred_tokens, gold_tokens)

    # Symbol recognition
    pred_symbolic = [p.get("symbolic", []) for p in predictions]
    gold_symbolic = [g.get("symbolic", []) for g in gold]
    flat_pred = [s for sublist in pred_symbolic for s in sublist]
    flat_gold = [s for sublist in gold_symbolic for s in sublist]
    report["metrics"]["symbol_recognition"] = symbol_recognition_score(flat_pred, flat_gold)

    # Numerology consistency
    pred_roots = [
        p.get("numerology", {}).get("total_root", 0)
        for p in predictions
    ]
    gold_roots = [
        g.get("numerology", {}).get("total_root", 0)
        for g in gold
    ]
    report["metrics"]["numerology_match"] = simple_accuracy(
        [str(r) for r in pred_roots],
        [str(r) for r in gold_roots],
    )

    return report
