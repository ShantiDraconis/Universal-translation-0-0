# Data Standards - Universal Translation Engine 0/0

This document defines the data formats, encoding standards, and conventions
used throughout the Universal Translation Engine.

## Encoding Standards

### Character Encoding

All text files MUST use **UTF-8** encoding without BOM (Byte Order Mark).

```bash
# Verify UTF-8 encoding
file -i yourfile.csv
# Should output: text/plain; charset=utf-8
```

### Line Endings

- Unix-style line endings (LF, `\n`) are preferred
- Windows-style (CRLF, `\r\n`) is acceptable but not recommended

## File Formats

### CSV Files

CSV files follow RFC 4180 with these conventions:

| Aspect | Standard |
|--------|----------|
| Delimiter | Comma (`,`) |
| Quote character | Double quote (`"`) |
| Header row | Required |
| Encoding | UTF-8 |
| Line ending | LF or CRLF |

**Example:**
```csv
sign_id,description,category,unicode
M-001,Standing human figure,Anthropomorphic,
M-008,Fish sign,Zoomorphic,𒄩
```

**Required columns by dataset type:**

| Dataset Type | Required Columns |
|--------------|------------------|
| Harappan signs | `sign_id`, `description`, `category` |
| Mappings | `source`, `target` |
| Phonemes | `phoneme_id`, `ipa`, `category` |
| Symbols | `symbol_id`, `name`, `category` |

### JSON Files

JSON files follow standard JSON specification (RFC 8259):

- UTF-8 encoding
- 2-space indentation for readability
- No trailing commas
- No comments (use separate documentation)

**Example structure for mappings:**
```json
{
  "metadata": {
    "name": "Mapping Name",
    "version": "1.0",
    "description": "Description of the mapping"
  },
  "mappings": [
    {
      "source": "value",
      "target": "value",
      "probability": 0.95
    }
  ]
}
```

### YAML Files

YAML files (configuration, scoring) follow YAML 1.2:

- UTF-8 encoding
- 2-space indentation
- No tabs
- Use explicit quotes for strings containing special characters

**Example:**
```yaml
version: "1.0"
dimensions:
  - name: linguistic_plausibility
    scale: 0-5
```

## Phonetic Notation

### IPA (International Phonetic Alphabet)

Primary notation for phonetic transcription:

| Symbol | Description | Example |
|--------|-------------|---------|
| `p` | Voiceless bilabial plosive | **p**at |
| `b` | Voiced bilabial plosive | **b**at |
| `t` | Voiceless alveolar plosive | **t**op |
| `ʃ` | Voiceless postalveolar fricative | **sh**ip |
| `ŋ` | Velar nasal | si**ng** |
| `ə` | Mid central vowel (schwa) | **a**bout |

### IPA to X-SAMPA Conversion

For ASCII-only environments, X-SAMPA notation is supported:

| IPA | X-SAMPA |
|-----|---------|
| `ʃ` | `S` |
| `ʒ` | `Z` |
| `θ` | `T` |
| `ð` | `D` |
| `ŋ` | `N` |
| `ə` | `@` |

## Sign Identification

### Mahadevan System (M-xxx)

Primary system for Harappan signs:

- Format: `M-001` to `M-417`
- Zero-padded to 3 digits
- Uppercase M prefix

### Wells System (W-xxx)

Alternative system for sign variants:

- Format: `W-001` to `W-694`
- Zero-padded to 3 digits
- Uppercase W prefix

### Universal 0/0 Codes

Internal coding system:

- Format: `00-CAT-NNN`
- `00` - Universal system prefix
- `CAT` - 3-letter category code
- `NNN` - Zero-padded number

**Category codes:**

| Code | Category |
|------|----------|
| `HUM` | Human/Anthropomorphic |
| `ANI` | Animal/Zoomorphic |
| `OBJ` | Object |
| `NUM` | Numeral |
| `GEO` | Geometric |
| `BOT` | Botanical |
| `ARC` | Architecture |
| `TRN` | Transport |
| `TOL` | Tool |
| `BOD` | Body Part |
| `CEL` | Celestial |
| `WEA` | Weather |
| `GEG` | Geography |
| `TTL` | Title/Occupation |
| `CMP` | Compound |
| `MRK` | Marker |
| `ELE` | Element |
| `SAC` | Sacred |
| `NAT` | Nature |
| `LIF` | Life |

## Symbolic Notation

### 0/0 Constant

The indeterminate constant `I = 0/0` represents:
- Infinite potential
- Source of manifestation
- Union of opposites

### Numerological Values

Root digits (1-9) follow Pythagorean tradition:

| Root | Archetype | Element | Planet |
|------|-----------|---------|--------|
| 1 | Unity | Fire | Sun |
| 2 | Duality | Water | Moon |
| 3 | Creation | Fire | Jupiter |
| 4 | Foundation | Earth | Uranus |
| 5 | Change | Air | Mercury |
| 6 | Harmony | Earth | Venus |
| 7 | Mystery | Water | Neptune |
| 8 | Power | Earth | Saturn |
| 9 | Completion | Fire | Mars |

### Element Codes

| Element | Symbol | Polarity |
|---------|--------|----------|
| Fire | 🔥 | Positive |
| Water | 💧 | Negative |
| Earth | 🌍 | Neutral |
| Air | 💨 | Positive |
| Ether | ✨ | Neutral |

### Polarity Values

| Polarity | Meaning |
|----------|---------|
| `positive` | Active, masculine, yang |
| `negative` | Passive, feminine, yin |
| `neutral` | Balanced, center |

## Probability Scores

Mapping confidence levels:

| Range | Confidence | Description |
|-------|------------|-------------|
| 0.90-1.00 | High | Clear semantic/phonetic match |
| 0.75-0.89 | Medium-high | Strong correlation |
| 0.60-0.74 | Medium | Reasonable connection |
| 0.40-0.59 | Low-medium | Possible connection |
| 0.00-0.39 | Low | Speculative |

## Validation Rules

### CSV Validation

1. All rows must have same number of columns
2. No empty rows (except end of file)
3. Header row required
4. UTF-8 encoding required
5. ID columns should be unique

### JSON Validation

1. Valid JSON syntax
2. Required `metadata` section for data files
3. UTF-8 encoding
4. No duplicate keys

### Sign ID Validation

1. Must match pattern `^[MW]-\d{1,3}$` or `^\d{1,3}$`
2. Numeric portion within valid range
3. Unique within dataset

## API Data Formats

### Request Format

```json
{
  "text": "string to translate",
  "mode": "standard|full|simple"
}
```

### Response Format

```json
{
  "input": "original input",
  "tokens": ["list", "of", "tokens"],
  "phonemes": [{"token": "...", "ipa": "...", "family": "..."}],
  "symbolic": [{"token": "...", "symbolic_tags": [...]}],
  "numerology": {"total_value": 0, "total_root": 0},
  "synthesis": {"dominant_elements": [], "symbolic_synthesis": "..."}
}
```

## Version Control

### Semantic Versioning

Data files use semantic versioning in metadata:

- `MAJOR.MINOR.PATCH`
- Major: Breaking changes to structure
- Minor: New fields, backward compatible
- Patch: Corrections, no structure change

### Change Documentation

Changes to data standards should be documented in:
1. This document
2. CHANGELOG.md
3. Commit messages
