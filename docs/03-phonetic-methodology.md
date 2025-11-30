# 03-phonetic-methodology

## Phonetic Methodology

### Overview

This document describes the phonetic analysis methodology used for mapping Harappan signs to the 00 Universal Dictionary.

### Approach

1. **Phoneme Extraction**: Extract potential phonetic values from sign shape and comparative analysis
2. **Cross-linguistic Comparison**: Compare with phonemes from Tupi-Guarani, Dravidian, Hebrew, Sanskrit, etc.
3. **Distance Calculation**: Use phonetic distance metrics to score similarity

### Phonetic Distance Algorithm

The current implementation uses a simple character intersection heuristic:

```python
def simple_phonetic_distance(a: str, b: str) -> float:
    common = len(set(a) & set(b))
    max_len = max(len(a), len(b))
    return common / max_len if max_len > 0 else 0.0
```

### Future Improvements

- Implement IPA-based phonetic distance
- Add weighted consonant/vowel matching
- Include prosodic features
