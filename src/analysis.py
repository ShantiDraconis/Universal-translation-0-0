#!/usr/bin/env python3
"""
Harappan 00 Universal Language Analysis Framework

This module provides tools for phonetic and statistical analysis
of the Universal 0/0 Language Hypothesis, comparing phonemic tokens
across multiple language families.

Part of the harappan-00-universal research project.
"""

import csv
import math
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Token:
    """Represents a universal phonemic token."""
    token_id: str
    token: str
    phonetic_ipa: str
    semantic_core: str
    cosmological_category: str
    archetype: str
    harappan_link: str
    cognates: Dict[str, str]


@dataclass
class HarappanSign:
    """Represents a Harappan script sign."""
    sign_id: str
    unicode_approx: str
    variants: List[str]
    phonetic_value_proposed: str
    semantic_category: str
    universal_token_link: str
    frequency: str


def load_dictionary(filepath: str) -> List[Token]:
    """Load the universal dictionary from CSV."""
    tokens = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cognates = {
                'tupi': row.get('tupi_cognate', ''),
                'sanskrit': row.get('sanskrit_cognate', ''),
                'hebrew': row.get('hebrew_cognate', ''),
                'tamil': row.get('tamil_cognate', ''),
                'yoruba': row.get('yoruba_cognate', '')
            }
            token = Token(
                token_id=row['token_id'],
                token=row['token'],
                phonetic_ipa=row['phonetic_ipa'],
                semantic_core=row['semantic_core'],
                cosmological_category=row['cosmological_category'],
                archetype=row['archetype'],
                harappan_link=row.get('harappan_link', ''),
                cognates=cognates
            )
            tokens.append(token)
    return tokens


def load_harappan_signs(filepath: str) -> List[HarappanSign]:
    """Load Harappan signs from CSV."""
    signs = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sign = HarappanSign(
                sign_id=row['sign_id'],
                unicode_approx=row['unicode_approx'],
                variants=row.get('variants', '').split(';'),
                phonetic_value_proposed=row['phonetic_value_proposed'],
                semantic_category=row['semantic_category'],
                universal_token_link=row['universal_token_link'],
                frequency=row['frequency']
            )
            signs.append(sign)
    return signs


def phonetic_distance(ipa1: str, ipa2: str) -> float:
    """
    Calculate phonetic distance between two IPA representations.
    
    Uses a simplified Levenshtein-based approach with phonetic feature weighting.
    Returns a value between 0 (identical) and 1 (completely different).
    """
    if not ipa1 or not ipa2:
        return 1.0
    
    # Clean IPA strings
    ipa1 = ipa1.strip('/')
    ipa2 = ipa2.strip('/')
    
    if ipa1 == ipa2:
        return 0.0
    
    # Levenshtein distance
    m, n = len(ipa1), len(ipa2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if ipa1[i-1] == ipa2[j-1] else phonetic_substitution_cost(ipa1[i-1], ipa2[j-1])
            dp[i][j] = min(
                dp[i-1][j] + 1,      # deletion
                dp[i][j-1] + 1,      # insertion
                dp[i-1][j-1] + cost  # substitution
            )
    
    max_len = max(m, n)
    return dp[m][n] / max_len if max_len > 0 else 0.0


def phonetic_substitution_cost(char1: str, char2: str) -> float:
    """
    Calculate substitution cost based on phonetic features.
    
    Similar phonemes have lower substitution costs.
    """
    # Vowel groups
    vowels = {'a', 'e', 'i', 'o', 'u', 'ə', 'ɪ', 'ʊ', 'ɛ', 'ɔ', 'æ', 'ʌ'}
    front_vowels = {'i', 'e', 'ɪ', 'ɛ', 'æ'}
    back_vowels = {'u', 'o', 'ʊ', 'ɔ', 'a', 'ʌ'}
    
    # Consonant groups
    stops = {'p', 'b', 't', 'd', 'k', 'g', 'ʔ'}
    fricatives = {'f', 'v', 's', 'z', 'ʃ', 'ʒ', 'θ', 'ð', 'x', 'h'}
    nasals = {'m', 'n', 'ŋ', 'ɲ'}
    liquids = {'l', 'r', 'ɾ', 'ɹ', 'ʎ'}
    glides = {'w', 'j', 'ʋ'}
    
    # Same character
    if char1 == char2:
        return 0.0
    
    # Both vowels - lower cost
    if char1 in vowels and char2 in vowels:
        if (char1 in front_vowels and char2 in front_vowels) or \
           (char1 in back_vowels and char2 in back_vowels):
            return 0.3
        return 0.5
    
    # Both consonants of same type - lower cost
    for group in [stops, fricatives, nasals, liquids, glides]:
        if char1 in group and char2 in group:
            return 0.4
    
    # Vowel vs consonant - high cost
    if (char1 in vowels) != (char2 in vowels):
        return 1.0
    
    # Default consonant substitution
    return 0.7


def semantic_similarity(sem1: str, sem2: str) -> float:
    """
    Calculate semantic similarity between two semantic descriptions.
    
    Uses a simple overlap-based approach with semantic field matching.
    Returns a value between 0 (unrelated) and 1 (identical).
    """
    if not sem1 or not sem2:
        return 0.0
    
    # Normalize and split
    words1 = set(sem1.lower().replace(';', ' ').replace('_', ' ').split())
    words2 = set(sem2.lower().replace(';', ' ').replace('_', ' ').split())
    
    if not words1 or not words2:
        return 0.0
    
    # Jaccard similarity
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    
    return intersection / union if union > 0 else 0.0


def analyze_cognate_patterns(tokens: List[Token]) -> Dict[str, Dict[str, int]]:
    """
    Analyze cognate patterns across language families.
    
    Returns statistics about cognate presence by category.
    """
    results = defaultdict(lambda: defaultdict(int))
    languages = ['tupi', 'sanskrit', 'hebrew', 'tamil', 'yoruba']
    
    for token in tokens:
        category = token.cosmological_category
        for lang in languages:
            if token.cognates.get(lang) and token.cognates[lang].strip() and token.cognates[lang] != '-':
                results[category][lang] += 1
                results['total'][lang] += 1
        results[category]['total'] += 1
        results['total']['total'] += 1
    
    return dict(results)


def calculate_random_probability(
    observed_matches: int,
    total_comparisons: int,
    vocabulary_size: int = 1000,
    syllable_inventory: int = 50
) -> float:
    """
    Calculate the probability that observed phonetic matches occur by chance.
    
    Uses a simplified binomial model with normal approximation for large samples.
    """
    if total_comparisons == 0:
        return 1.0
    
    # Probability of random match given syllable inventory size
    p_random = 1 / syllable_inventory
    
    # Expected matches by chance
    expected_random = total_comparisons * p_random
    
    # If observed is much higher than expected, probability of chance is low
    if observed_matches <= expected_random:
        return 1.0
    
    # Use normal approximation for large samples (more numerically stable)
    # Mean = n * p, Variance = n * p * (1 - p)
    mean = expected_random
    variance = total_comparisons * p_random * (1 - p_random)
    
    if variance == 0:
        return 0.0
    
    std_dev = math.sqrt(variance)
    
    # Z-score for observed value
    z = (observed_matches - mean) / std_dev
    
    # Approximate p-value using error function
    # P(X >= observed) ≈ 0.5 * erfc(z / sqrt(2))
    p_value = 0.5 * math.erfc(z / math.sqrt(2))
    
    return p_value


def find_cross_linguistic_patterns(tokens: List[Token]) -> List[Dict]:
    """
    Find tokens with strong cross-linguistic evidence.
    
    Returns tokens that have cognates in 3+ language families.
    """
    strong_patterns = []
    
    for token in tokens:
        cognate_count = sum(
            1 for lang, cog in token.cognates.items()
            if cog and cog.strip() and cog != '-'
        )
        
        if cognate_count >= 3:
            strong_patterns.append({
                'token': token.token,
                'semantic_core': token.semantic_core,
                'cognate_count': cognate_count,
                'cognates': {k: v for k, v in token.cognates.items() if v and v.strip() and v != '-'},
                'archetype': token.archetype,
                'harappan_link': token.harappan_link
            })
    
    return sorted(strong_patterns, key=lambda x: x['cognate_count'], reverse=True)


def generate_similarity_matrix(tokens: List[Token], top_n: int = 20) -> List[List[float]]:
    """
    Generate a phonetic similarity matrix for the first N tokens.
    """
    subset = tokens[:top_n]
    matrix = []
    
    for t1 in subset:
        row = []
        for t2 in subset:
            distance = phonetic_distance(t1.phonetic_ipa, t2.phonetic_ipa)
            similarity = 1.0 - distance
            row.append(round(similarity, 3))
        matrix.append(row)
    
    return matrix


def link_harappan_to_universal(
    signs: List[HarappanSign],
    tokens: List[Token]
) -> List[Dict]:
    """
    Create linkage table between Harappan signs and universal tokens.
    """
    links = []
    token_map = {t.token_id: t for t in tokens}
    token_name_map = {t.token: t for t in tokens}
    
    for sign in signs:
        link_token = sign.universal_token_link
        token = token_name_map.get(link_token)
        
        if token:
            links.append({
                'harappan_id': sign.sign_id,
                'harappan_phonetic': sign.phonetic_value_proposed,
                'universal_token': token.token,
                'universal_phonetic': token.phonetic_ipa,
                'semantic_alignment': semantic_similarity(
                    sign.semantic_category,
                    token.semantic_core
                ),
                'archetype': token.archetype,
                'cognate_languages': sum(
                    1 for c in token.cognates.values()
                    if c and c.strip() and c != '-'
                )
            })
    
    return links


def generate_report(tokens: List[Token], signs: List[HarappanSign]) -> str:
    """Generate a comprehensive analysis report."""
    report = []
    report.append("=" * 70)
    report.append("HARAPPAN 00 UNIVERSAL LANGUAGE ANALYSIS REPORT")
    report.append("=" * 70)
    report.append("")
    
    # Token statistics
    report.append("1. TOKEN STATISTICS")
    report.append("-" * 40)
    report.append(f"   Total universal tokens: {len(tokens)}")
    
    categories = defaultdict(int)
    for t in tokens:
        categories[t.cosmological_category] += 1
    
    report.append("   Tokens by cosmological category:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        report.append(f"      {cat}: {count}")
    report.append("")
    
    # Cognate analysis
    report.append("2. COGNATE PATTERN ANALYSIS")
    report.append("-" * 40)
    cognate_stats = analyze_cognate_patterns(tokens)
    
    total_stats = cognate_stats.get('total', {})
    report.append("   Cognates by language family:")
    for lang in ['sanskrit', 'tupi', 'tamil', 'hebrew', 'yoruba']:
        count = total_stats.get(lang, 0)
        pct = (count / len(tokens) * 100) if tokens else 0
        report.append(f"      {lang.capitalize()}: {count} ({pct:.1f}%)")
    report.append("")
    
    # Strong patterns
    report.append("3. STRONG CROSS-LINGUISTIC PATTERNS")
    report.append("-" * 40)
    strong = find_cross_linguistic_patterns(tokens)
    report.append(f"   Tokens with 3+ language cognates: {len(strong)}")
    report.append("")
    report.append("   Top patterns:")
    for p in strong[:10]:
        report.append(f"      {p['token']} ({p['semantic_core']})")
        report.append(f"         Cognates in: {', '.join(p['cognates'].keys())}")
        report.append(f"         Archetype: {p['archetype']}")
    report.append("")
    
    # Harappan linkage
    report.append("4. HARAPPAN SIGN LINKAGE")
    report.append("-" * 40)
    report.append(f"   Total Harappan signs catalogued: {len(signs)}")
    
    links = link_harappan_to_universal(signs, tokens)
    linked_count = len(links)
    report.append(f"   Signs linked to universal tokens: {linked_count}")
    
    if links:
        avg_semantic = sum(l['semantic_alignment'] for l in links) / len(links)
        report.append(f"   Average semantic alignment: {avg_semantic:.3f}")
        
        strong_links = [l for l in links if l['cognate_languages'] >= 3]
        report.append(f"   Strong links (3+ cognate languages): {len(strong_links)}")
    report.append("")
    
    # Statistical significance
    report.append("5. STATISTICAL SIGNIFICANCE ESTIMATE")
    report.append("-" * 40)
    
    total_comparisons = len(tokens) * 5  # 5 language families
    total_matches = sum(
        1 for t in tokens
        for c in t.cognates.values()
        if c and c.strip() and c != '-'
    )
    
    p_value = calculate_random_probability(total_matches, total_comparisons)
    report.append(f"   Total cross-linguistic comparisons: {total_comparisons}")
    report.append(f"   Observed cognate matches: {total_matches}")
    report.append(f"   Estimated p-value (chance occurrence): {p_value:.6f}")
    
    if p_value < 0.01:
        report.append("   Interpretation: HIGHLY SIGNIFICANT - patterns unlikely to be random")
    elif p_value < 0.05:
        report.append("   Interpretation: SIGNIFICANT - patterns warrant further investigation")
    else:
        report.append("   Interpretation: NOT SIGNIFICANT - more data needed")
    report.append("")
    
    report.append("=" * 70)
    report.append("END OF REPORT")
    report.append("=" * 70)
    
    return "\n".join(report)


def main():
    """Main entry point for analysis."""
    import os
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(os.path.dirname(script_dir), 'data')
    
    dict_path = os.path.join(data_dir, 'universal_dictionary_00.csv')
    signs_path = os.path.join(data_dir, 'harappan_signs.csv')
    
    print("Loading data...")
    tokens = load_dictionary(dict_path)
    signs = load_harappan_signs(signs_path)
    
    print(f"Loaded {len(tokens)} universal tokens")
    print(f"Loaded {len(signs)} Harappan signs")
    print("")
    
    report = generate_report(tokens, signs)
    print(report)
    
    # Save report to file
    report_path = os.path.join(data_dir, 'analysis_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
