# Methodology for Universal Phonemic Kernel Analysis

## Overview

This document outlines the methodology used to analyze and validate the Universal Phonemic Kernel Hypothesis (0/0). It covers phonetic similarity criteria, semantic similarity criteria, and statistical procedures.

---

## 1. Phonetic Similarity Criteria

### 1.1 Phonetic Distance Metric

We use a modified Levenshtein distance with phonetic feature weighting to measure similarity between phonemic tokens across languages.

**Formula:**
```
d(s₁, s₂) = edit_distance(s₁, s₂) / max(|s₁|, |s₂|)
```

Where edit operations are weighted by phonetic similarity:

| Operation | Cost |
|-----------|------|
| Vowel ↔ Vowel (same height/frontness) | 0.3 |
| Vowel ↔ Vowel (different features) | 0.5 |
| Consonant ↔ Consonant (same class) | 0.4 |
| Consonant ↔ Consonant (different class) | 0.7 |
| Vowel ↔ Consonant | 1.0 |
| Insertion/Deletion | 1.0 |

### 1.2 Phonetic Feature Classes

**Vowels:**
- Front: /i/, /e/, /ɪ/, /ɛ/, /æ/
- Back: /u/, /o/, /ʊ/, /ɔ/, /a/, /ʌ/
- Central: /ə/

**Consonants:**
- Stops: /p/, /b/, /t/, /d/, /k/, /g/, /ʔ/
- Fricatives: /f/, /v/, /s/, /z/, /ʃ/, /ʒ/, /θ/, /ð/, /x/, /h/
- Nasals: /m/, /n/, /ŋ/, /ɲ/
- Liquids: /l/, /r/, /ɾ/, /ɹ/, /ʎ/
- Glides: /w/, /j/, /ʋ/

### 1.3 Similarity Threshold

- **High Similarity**: d < 0.3 (strong potential cognate)
- **Medium Similarity**: 0.3 ≤ d < 0.5 (possible cognate)
- **Low Similarity**: 0.5 ≤ d < 0.7 (weak relationship)
- **No Relationship**: d ≥ 0.7

---

## 2. Semantic Similarity Criteria

### 2.1 Semantic Field Categories

Tokens are assigned to semantic fields based on their core meanings:

| Category | Description | Examples |
|----------|-------------|----------|
| Cosmological | Universal principles | primordial, celestial, chthonic |
| Archetypal | Psychological universals | mother, father, hero, shadow |
| Ontological | Existence/being | creation, destruction, transformation |
| Temporal | Time-related | cycle, beginning, end, eternal |
| Elemental | Natural elements | fire, water, earth, air, ether |
| Social | Human relations | king, servant, community |
| Divine | Sacred/spiritual | deity, spirit, sacred |

### 2.2 Semantic Similarity Measure

We use Jaccard similarity on semantic tags:

```
sim(A, B) = |A ∩ B| / |A ∪ B|
```

Where A and B are sets of semantic descriptors for each term.

**Interpretation:**
- sim ≥ 0.5: Strong semantic alignment
- 0.3 ≤ sim < 0.5: Moderate alignment
- sim < 0.3: Weak or no alignment

### 2.3 Cross-Domain Mapping

Semantic connections across domains are identified through:

1. **Direct equivalence**: Same core meaning (e.g., "mother" = "mother")
2. **Metaphorical extension**: Related meaning (e.g., "source" → "mother")
3. **Archetype mapping**: Jung's archetypes as bridge concepts

---

## 3. Statistical Procedures

### 3.1 Hypothesis Testing Framework

**Null Hypothesis (H₀):** Observed phonetic-semantic correspondences are due to chance.

**Alternative Hypothesis (H₁):** Correspondences exceed chance expectation, indicating genuine cross-linguistic patterns.

### 3.2 Statistical Test

We use a normal approximation to the binomial distribution:

```
Z = (X - μ) / σ
```

Where:
- X = observed number of matches
- μ = n × p (expected matches under H₀)
- σ = √(n × p × (1-p))
- n = total comparisons
- p = probability of random match (1/syllable_inventory)

**Validation conditions for normal approximation:**
- n × p ≥ 5
- n × (1-p) ≥ 5

### 3.3 Multiple Comparisons Correction

When comparing across multiple language pairs, we apply:

1. **Bonferroni correction**: α_adjusted = α / number_of_tests
2. **False Discovery Rate (FDR)**: Benjamini-Hochberg procedure

### 3.4 Effect Size

Cohen's h for proportions:
```
h = 2 × arcsin(√p_observed) - 2 × arcsin(√p_expected)
```

**Interpretation:**
- h < 0.2: Small effect
- 0.2 ≤ h < 0.5: Medium effect
- h ≥ 0.5: Large effect

---

## 4. Data Collection Standards

### 4.1 Token Selection Criteria

Universal tokens are selected based on:

1. **Cross-linguistic presence**: Found in 3+ unrelated language families
2. **Semantic stability**: Core meaning preserved across attestations
3. **Phonetic consistency**: Recognizable phonetic form with documented variants
4. **Documentary evidence**: Attested in reliable linguistic sources

### 4.2 Cognate Verification

Each claimed cognate is evaluated for:

1. **Phonetic plausibility**: Follows known sound change patterns
2. **Semantic plausibility**: Meaning relationship is documented
3. **Geographic/temporal plausibility**: Contact or common ancestry possible
4. **Alternative explanations**: Borrowing, coincidence ruled out

### 4.3 Harappan Sign Assignment

Phonetic values assigned to Harappan signs based on:

1. **Frequency patterns**: Common signs for common phonemes
2. **Contextual analysis**: Distribution in inscriptions
3. **Iconographic interpretation**: Visual form suggests meaning
4. **Cross-reference**: Consistency with universal token system

---

## 5. Reproducibility

### 5.1 Data Availability

All data files are available in the `/data/` directory:
- `universal_dictionary_00.csv`: Token definitions and cognates
- `harappan_signs.csv`: Sign catalog with proposed values

### 5.2 Code Availability

Analysis code is available in `/src/analysis.py` with:
- Phonetic distance functions
- Semantic similarity functions
- Statistical testing functions
- Report generation

### 5.3 Running the Analysis

```bash
cd src
python analysis.py
```

Output is saved to `data/analysis_report.txt`.

---

## 6. Limitations

### 6.1 Known Limitations

1. **Sample size**: Current dictionary (200 tokens) is subset of target (1000)
2. **Harappan uncertainty**: Phonetic values are provisional proposals
3. **Cognate verification**: Not all cognates independently verified
4. **Statistical assumptions**: Normal approximation may not hold for all cases

### 6.2 Future Improvements

1. Expand dictionary to 500, then 1000 tokens
2. Implement more sophisticated phonetic distance (distinctive features)
3. Add semantic ontology from established databases
4. Conduct permutation tests for statistical robustness
5. Seek external validation from linguists

---

## References

1. Levenshtein, V.I. (1966). Binary codes capable of correcting deletions, insertions, and reversals.
2. Jaccard, P. (1912). The distribution of the flora in the alpine zone.
3. Cohen, J. (1988). Statistical power analysis for the behavioral sciences.
4. Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate.

---

*Document prepared as part of the Universal Translation Project*

*Last updated: 2025*
