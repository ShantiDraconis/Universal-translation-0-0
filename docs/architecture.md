# Architecture - Universal Translation Engine 0/0

This document describes the architecture of the Universal Translation Engine 0/0.

## Overview

The Universal Translation Engine is a modular framework for cross-linguistic and symbolic analysis. It implements a 10-stage pipeline that transforms input text through multiple analytical layers.

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Universal Translation Engine 0/0              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   API Layer   │    │   CLI Layer   │    │  REST Server  │      │
│  │  translate.py │    │    cli.py     │    │ server_fast   │      │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘      │
│         │                   │                   │               │
│         └───────────────────┼───────────────────┘               │
│                             │                                    │
│                     ┌───────▼───────┐                           │
│                     │   Pipeline     │                           │
│                     │  (Orchestrator)│                           │
│                     └───────┬───────┘                           │
│                             │                                    │
│  ┌──────────────────────────┼──────────────────────────┐       │
│  │                    Core Engines                      │       │
│  │                                                      │       │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │       │
│  │  │ Tokenizer  │  │  Phoneme   │  │  Harappan  │    │       │
│  │  │            │  │  Engine    │  │  Engine    │    │       │
│  │  └────────────┘  └────────────┘  └────────────┘    │       │
│  │                                                      │       │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │       │
│  │  │ Numerology │  │ Semiotics  │  │ Embeddings │    │       │
│  │  │ Engine     │  │ Engine     │  │            │    │       │
│  │  └────────────┘  └────────────┘  └────────────┘    │       │
│  │                                                      │       │
│  └──────────────────────────┬──────────────────────────┘       │
│                             │                                    │
│  ┌──────────────────────────┼──────────────────────────┐       │
│  │                   Data Layer                         │       │
│  │                                                      │       │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │       │
│  │  │  Mappings  │  │  Datasets  │  │  Utils     │    │       │
│  │  │  (JSON)    │  │  (CSV)     │  │  (Loaders) │    │       │
│  │  └────────────┘  └────────────┘  └────────────┘    │       │
│  │                                                      │       │
│  └──────────────────────────────────────────────────────┘       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Pipeline Module (`core/pipeline.py`)

The orchestrator that coordinates all translation stages:

- `translate_text()` - Standard translation with configurable stages
- `translate_harappan()` - Specialized Harappan sign decoding
- `full_pipeline()` - Complete 10-stage analysis

### 2. Tokenizer (`core/tokenizer.py`)

Text segmentation utilities:

- `basic_tokenize()` - Whitespace tokenization
- `syllable_tokenize()` - Syllable-level segmentation
- `phoneme_tokenize()` - Phoneme-level segmentation
- `harappan_sign_tokenize()` - Harappan sign sequence parsing

### 3. Phoneme Engine (`core/phoneme_engine.py`)

Universal phonetic representation:

- IPA transcription
- Language family detection
- Phonetic feature extraction

### 4. Harappan Engine (`core/harappan_engine.py`)

Harappan script processing:

- Sign sequence decoding/encoding
- Category classification
- Universal 0/0 code conversion

### 5. Numerology Engine (`core/numerology_engine.py`)

Numerical symbolic analysis:

- Pythagorean numerology
- Hebrew gematria
- Root reduction
- 0/0 normalization

### 6. Semiotics Engine (`core/semiotics_engine.py`)

Symbolic/archetypal analysis:

- Symbol annotation
- Archetype detection
- Element mapping
- Polarity analysis

### 7. Embeddings (`core/embeddings.py`)

Vector representations:

- Token embeddings
- Phoneme embeddings
- Symbol embeddings
- Similarity calculations

## The 10-Stage Pipeline

```
INPUT TEXT
    │
    ▼
┌───────────────────────────────┐
│ Stage 1: SEGMENTATION         │
│ - Word tokenization           │
│ - Syllable tokenization       │
│ - Optional inversion          │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 2: PHONEME MAPPING      │
│ - IPA transcription           │
│ - Universal phoneme codes     │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 3: HARAPPAN PROJECTION  │
│ - Sign mapping (when enabled) │
│ - Pictographic correlations   │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 4: LANGUAGE FAMILIES    │
│ - Family detection            │
│ - Cross-linguistic patterns   │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 5: SYMBOLIC 0/0         │
│ - Symbol annotation           │
│ - Archetype detection         │
│ - Element/polarity mapping    │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 6: ARCHAEO-COSMOLOGICAL │
│ - Synthesis of symbolic layer │
│ - Universal interpretation    │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 7: NUMEROLOGY           │
│ - Word values                 │
│ - Root reduction              │
│ - Symbolic meanings           │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 8: MULTIPLE TRANSLATION │
│ - Literal translation         │
│ - Archetypal translation      │
│ - Energetic translation       │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 9: DIAGRAM              │
│ - Metrics summary             │
│ - Visual representation data  │
└───────────────────────────────┘
    │
    ▼
┌───────────────────────────────┐
│ Stage 10: UNIVERSAL PHRASE    │
│ "Universal Translation 0/0:   │
│  [elements] | [archetypes] |  │
│  Root [N]"                    │
└───────────────────────────────┘
```

## Data Flow

### Input Processing

1. Text received via API, CLI, or direct function call
2. Pipeline orchestrator determines which stages to run
3. Each engine processes data and passes results forward

### Output Generation

Each stage produces structured output:

```python
{
    "input": "original text",
    "stage_1_segmentation": {...},
    "stage_2_phonemes": [...],
    # ...
    "stage_10_universal": "Universal Translation 0/0: ..."
}
```

## Extension Points

### Adding New Engines

1. Create module in `universal_translation/core/`
2. Implement required interface functions
3. Register in `core/__init__.py`
4. Integrate with pipeline

### Adding New Data

1. Place data files in appropriate `datasets/` or `mappings/` directory
2. Create loader functions in `utils/loaders.py`
3. Add validators in `utils/validators.py`

### Adding New API Endpoints

1. Define request/response models in `api/server_fastapi.py`
2. Create endpoint function
3. Wire to translation functions

## Configuration

### Environment Variables

- No required environment variables for core functionality
- API server configuration via standard FastAPI/Uvicorn options

### Data Paths

Default paths are relative to the package installation:
- Mappings: `universal_translation/mappings/`
- Datasets: `universal_translation/datasets/`

## Dependencies

### Core (Zero Dependencies)

The core package has no external dependencies for basic functionality.

### Optional Dependencies

- **API**: FastAPI, Uvicorn, Pydantic
- **Development**: pytest, black, mypy, ruff
- **Documentation**: MkDocs

## Security Considerations

- All input is sanitized through standard Python string handling
- No external network calls in core functionality
- File operations use safe path handling
