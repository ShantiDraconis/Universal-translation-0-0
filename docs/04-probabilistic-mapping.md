# 04-probabilistic-mapping

## Probabilistic Mapping Methodology

### Overview

This document describes the probabilistic approach used to map Harappan signs to Dictionary 00 tokens.

### Confidence Score Calculation

Each mapping candidate receives a confidence score based on:

1. **Phonetic similarity** (0-1 scale)
2. **Semantic correspondence** (0-1 scale)
3. **Symbolic pattern match** (0-1 scale)

### Normalization

Confidence scores are normalized within each sign group to produce relative rankings:

```python
sub["confidence_score"] = sub["confidence_score"] / max_score
```

### Statistics Generated

For each Harappan sign:
- Total number of candidates
- Top confidence score
- Average confidence score
- Best matching token

### Output Files

- `data/mappings/mapping_harappan_to_00.csv` - Full mapping with all candidates
- `data/mappings/mapping_harappan_to_00_stats.csv` - Statistical summary
