# API Documentation - Universal Translation Engine 0/0

This document describes the API for the Universal Translation Engine.

## Overview

The Universal Translation Engine provides multiple interfaces:

1. **Python API** - Direct function calls
2. **REST API** - HTTP endpoints via FastAPI
3. **CLI** - Command-line interface

## Python API

### Basic Usage

```python
from universal_translation.api.translate import translate

# Standard translation
result = translate("Hello world")
print(result)

# Full 10-stage pipeline
result = translate("Om mani padme hum", mode="full")
print(result["stage_10_universal"])

# Simple mode (tokenization + phonemes only)
result = translate("Test", mode="simple")
```

### Core Functions

#### `translate(text, mode="standard")`

Translate text using the Universal Translation Engine.

**Parameters:**
- `text` (str): Input text to translate
- `mode` (str): Translation mode
  - `"standard"`: Basic translation with all stages (default)
  - `"full"`: Complete 10-stage pipeline with inversions
  - `"simple"`: Quick tokenization and phoneme analysis only

**Returns:** `Dict[str, Any]` with translation results

**Example:**
```python
result = translate("fire water earth")
print(result["tokens"])      # ['fire', 'water', 'earth']
print(result["synthesis"])   # {'dominant_elements': ['fire', 'water', 'earth'], ...}
```

#### `decode_harappan(sign_ids)`

Decode a sequence of Harappan sign IDs.

**Parameters:**
- `sign_ids` (List[int]): List of Mahadevan sign indices (1-417)

**Returns:** `Dict[str, Any]` with decoded signs and analysis

**Example:**
```python
from universal_translation.api.translate import decode_harappan

result = decode_harappan([1, 8, 15])
print(result["decoded_signs"])
```

#### `analyze_numerology(text)`

Perform numerological analysis on text.

**Parameters:**
- `text` (str): Input text

**Returns:** `Dict[str, Any]` with numerological analysis

**Example:**
```python
from universal_translation.api.translate import analyze_numerology

result = analyze_numerology("Universal")
print(result["total_root"])  # Root digit (1-9)
```

#### `get_symbolic_meaning(text)`

Get symbolic/archetypal meanings for text.

**Parameters:**
- `text` (str): Input text

**Returns:** `Dict[str, Any]` with symbolic analysis

#### `get_universal_phrase(text)`

Generate the Universal 0/0 phrase for text.

**Parameters:**
- `text` (str): Input text

**Returns:** `str` in format "Universal Translation 0/0: ..."

## REST API

### Starting the Server

```bash
# Using uvicorn directly
uvicorn universal_translation.api.server_fastapi:app --reload

# Or with the module
python -m uvicorn universal_translation.api.server_fastapi:app --host 0.0.0.0 --port 8000
```

### Endpoints

#### `GET /`

Root endpoint with API information.

**Response:**
```json
{
  "name": "Universal Translation Engine 0/0",
  "version": "0.1.0",
  "endpoints": ["/translate", "/harappan/decode", ...]
}
```

#### `POST /translate`

Translate text using the Universal Translation Engine.

**Request:**
```json
{
  "text": "Hello world",
  "mode": "standard"
}
```

**Response:**
```json
{
  "input": "Hello world",
  "tokens": ["Hello", "world"],
  "phonemes": [...],
  "symbolic": [...],
  "numerology": {...},
  "synthesis": {...}
}
```

#### `POST /harappan/decode`

Decode a sequence of Harappan sign IDs.

**Request:**
```json
{
  "sign_ids": [1, 8, 15]
}
```

**Response:**
```json
{
  "input_ids": [1, 8, 15],
  "decoded_signs": [
    {"mahadevan_id": 1, "universal_code": "00-HUM-001", ...},
    ...
  ],
  "sign_text": "SIGN_1 SIGN_8 SIGN_15",
  "analysis": {...}
}
```

#### `POST /harappan/search`

Search for Harappan signs matching a query.

**Request:**
```json
{
  "query": "fish"
}
```

**Response:**
```json
{
  "query": "fish",
  "results": [...],
  "count": 5
}
```

#### `POST /numerology`

Perform numerological analysis.

**Request:**
```json
{
  "text": "Universal"
}
```

**Response:**
```json
{
  "phrase": "Universal",
  "word_analyses": [...],
  "total_value": 136,
  "total_root": 1,
  "phrase_meaning": {...}
}
```

#### `POST /symbolic`

Get symbolic/archetypal meanings.

**Request:**
```json
{
  "text": "fire water"
}
```

**Response:**
```json
{
  "tokens": ["fire", "water"],
  "annotations": [...],
  "synthesis": {
    "dominant_elements": ["fire", "water"],
    "symbolic_synthesis": "..."
  }
}
```

#### `POST /universal-phrase`

Generate the Universal 0/0 phrase.

**Request:**
```json
{
  "text": "Sacred message"
}
```

**Response:**
```json
{
  "input": "Sacred message",
  "universal_phrase": "Universal Translation 0/0: sacred | ..."
}
```

#### `GET /health`

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Universal Translation Engine 0/0"
}
```

### Error Handling

All endpoints return standard HTTP error codes:

- `400 Bad Request`: Invalid input parameters
- `500 Internal Server Error`: Processing error

Error response format:
```json
{
  "detail": "Error message"
}
```

## CLI

### Installation

```bash
pip install -e .
```

### Usage

```bash
# Basic translation
universal-translate "Hello world"

# Full pipeline
universal-translate --mode full "Om mani padme hum"

# Harappan decoding
universal-translate --harappan 1 8 15

# Numerology only
universal-translate --numerology "Sacred text"

# Symbolic analysis
universal-translate --symbolic "fire water earth"

# Universal phrase only
universal-translate --phrase "Universal message"

# Output format
universal-translate --format simple "test"
universal-translate --format json "test"
```

### Options

| Option | Short | Description |
|--------|-------|-------------|
| `--mode` | `-m` | Translation mode (standard/full/simple) |
| `--harappan` | `-H` | Decode Harappan sign IDs |
| `--numerology` | `-n` | Numerological analysis only |
| `--symbolic` | `-s` | Symbolic meanings only |
| `--phrase` | `-p` | Universal phrase only |
| `--format` | `-f` | Output format (json/simple) |
| `--version` | `-v` | Show version |
| `--help` | `-h` | Show help |

## Response Structures

### Translation Result

```python
{
    "input": str,           # Original input
    "tokens": List[str],    # Word tokens
    "syllables": List[str], # Syllable tokens
    "phonemes": [           # Phoneme analysis
        {
            "token": str,
            "ipa": str,
            "family": str
        }
    ],
    "symbolic": [           # Symbolic annotations
        {
            "token": str,
            "symbolic_tags": List[str],
            "archetype": Optional[str],
            "element": Optional[str],
            "polarity": str,
            "numerological_value": Optional[int]
        }
    ],
    "numerology": {         # Numerological analysis
        "phrase": str,
        "word_analyses": List[Dict],
        "total_value": int,
        "total_root": int,
        "phrase_meaning": Dict
    },
    "synthesis": {          # Unified interpretation
        "dominant_elements": List[str],
        "dominant_archetypes": List[str],
        "overall_polarity": str,
        "symbolic_synthesis": str
    }
}
```

### Full Pipeline Result

Additional fields for `mode="full"`:

```python
{
    "stage_1_segmentation": {...},
    "stage_2_phonemes": [...],
    "stage_3_harappan": {...},  # When enabled
    "stage_4_families": [...],
    "stage_5_symbolic": [...],
    "stage_6_archaeo": {...},
    "stage_7_numerology": {...},
    "stage_8_translations": {
        "literal": str,
        "archetypal": str,
        "energetic": str
    },
    "stage_9_diagram": {
        "token_count": int,
        "syllable_count": int,
        "phoneme_families": List[str],
        "dominant_elements": List[str],
        "dominant_archetypes": List[str],
        "numerological_root": int
    },
    "stage_10_universal": str  # Final universal phrase
}
```
