# Benchmark Dataset

This directory contains benchmark datasets for evaluating the Universal Translation Engine 0/0.

## Dataset Structure

Each benchmark dataset should include:

1. **Input data** (CSV or JSON)
   - Text samples or sign sequences
   - Metadata (source, type, difficulty)

2. **Gold standard annotations**
   - Expected tokenization
   - Expected phoneme analysis
   - Expected symbolic annotations
   - Expected numerological values

3. **Human evaluations** (when available)
   - Reviewer scores
   - Comments
   - Consensus decisions

## Planned Datasets

### 1. basic_translation_benchmark.csv
- Simple word and phrase translations
- Expected outputs for standard pipeline

### 2. harappan_sequence_benchmark.csv
- Harappan sign sequences
- Documented interpretations
- Academic references

### 3. numerology_benchmark.csv
- Words with known numerological significance
- Traditional interpretations
- System-specific values (Pythagorean, Hebrew, etc.)

### 4. cross_linguistic_benchmark.csv
- Words from multiple language families
- Expected phoneme mappings
- Language family detection ground truth

### 5. symbolic_interpretation_benchmark.csv
- Texts with clear archetypal content
- Expected element associations
- Expected polarity analysis

## Contributing Benchmarks

To contribute new benchmark data:

1. Follow the existing format
2. Include source citations
3. Provide clear gold standard annotations
4. Document any assumptions or conventions
5. Submit via pull request

## Format Specifications

### CSV Format
```csv
id,input,expected_tokens,expected_root,source,notes
1,"hello world","hello world",7,test,basic test case
```

### JSON Format
```json
{
  "id": 1,
  "input": "hello world",
  "expected": {
    "tokens": ["hello", "world"],
    "numerology": {"total_root": 7}
  },
  "metadata": {
    "source": "test",
    "notes": "basic test case"
  }
}
```

## Evaluation Scripts

Use the metrics module to evaluate against benchmarks:

```python
from universal_translation.evaluation.metrics import benchmark_report

report = benchmark_report(predictions, gold_standard)
print(report)
```
