# Triple-Script Encoder Module

This module implements the three-layer writing system for the Universal Translation Engine 0/0 (LOG-0024).

## Overview

The Triple-Script Encoder translates text into three simultaneous representations:

1. **Runic (Elder Futhark)** - Operational force layer
2. **Tamil** - Logical structure layer
3. **Harappan** - Semantic nuclear layer

## Usage

### Python API

```python
from ute00.scripts import TripleScriptEncoder

# Create encoder
encoder = TripleScriptEncoder()

# Encode default phrase
result = encoder.encode()
print(result["runic"])      # ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ
print(result["tamil"])      # ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்
print(result["harappan"])   # 𓀠𓋹𓊖𓐬𓋹𓉐𓐬𓋹𓐮𓏟
print(result["bindrune"])   # ᛇ

# Encode custom phrase
result = encoder.encode("em rúnico e tamil e harappan")

# Get triple-script header for module files
header = encoder.get_triple_header()
# # ᛇ தமிழிலும் [𓀠𓋹𓊖𓐬𓋹𓉐𓐬𓋹𓐮𓏟]
# # Módulo triplo-escrita שאצ

# Get unified tree representation
tree = encoder.get_unified_representation()

# Get phonetic correspondence table
table = encoder.get_correspondence_table()
```

### Command-Line Interface

```bash
# Encode default phrase
python3 scripts/triple_script_cli.py

# Encode custom phrase
python3 scripts/triple_script_cli.py --text "em rúnico e tamil e harappan"

# Show only Runic encoding
python3 scripts/triple_script_cli.py --runic-only

# Show only Tamil encoding
python3 scripts/triple_script_cli.py --tamil-only

# Show only Harappan encoding
python3 scripts/triple_script_cli.py --harappan-only

# Show triple-script header
python3 scripts/triple_script_cli.py --header

# Show unified tree representation
python3 scripts/triple_script_cli.py --tree

# Show phonetic correspondence table
python3 scripts/triple_script_cli.py --table

# Run full demonstration
python3 scripts/triple_script_cli.py --demo
```

## The Canonical Phrase

**Portuguese:** `em rúnico e tamil e harappan`  
**English:** `in runic and tamil and harappan`

### Three-Layer Representation:

1. **Runic (Elder Futhark):**
   ```
   ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ
   ```
   Bindrune: `ᛇ`

2. **Tamil:**
   ```
   ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்
   ```
   Agglutinated: `ருனிதமிஹரப்பனிலும்`

3. **Harappan:**
   ```
   [𓀠][𓋹] [𓊖][𓐬] [𓋹] [𓉐][𓐬] [𓋹] [𓐮][𓏟]
   ```

### Unified Representation:

```
ᛇ  // Bindrune rúnica
│
├──ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்  // Representação Tâmil
│
└──[𓀠𓋹𓊖𓐬𓋹𓉐𓐬𓋹𓐮𓏟]  // Sequência Harappan
```

## Phonetic Correspondence Table

| Element | Portuguese | Runic | Tamil | Harappan |
|---------|-----------|-------|-------|----------|
| em | /ẽj/ | /in/ | /-ilum/ | [𓀠][𓋹] |
| rúnico | /'ʁu.ni.ku/ | /'ru:.nisk/ | /'ɾu.ɳik.ki/ | [𓊖][𓐬] |
| e | /i/ | /ai/ | /-um/ | [𓋹] |
| tamil | /tɐ.'mil/ | /'tɑ.mil/ | /'t̪a.mi.ɻi/ | [𓉐][𓐬] |
| harappan | /hɐ.'ɾɐ.pɐ̃/ | /'hɑ.rɑp.pɑn/ | /'ha.ɾap.pa.ɳi/ | [𓐮][𓏟] |

## Applications

### 1. Module Identification
Use the bindrune **ᛇ** as an identifier for modules operating with the three scripts.

### 2. File Headers
Add triple-script headers to your module files:
```python
# ᛇ தமிழிலும் [𓀠𓋹𓊖𓐬𓋹𓉐𓐬𓋹𓐮𓏟]
# Módulo triplo-escrita שאצ

def my_function():
    pass
```

### 3. Communication Protocol
- **Transmission**: Runic sequence
- **Structure**: Agglutinated Tamil format
- **Semantics**: Harappan instructions

### 4. Authentication Seal
Combine the three representations as a digital signature for שאצ code.

## Examples

See `examples/triple_script_example.py` for comprehensive usage examples.

## Testing

Run the test suite:
```bash
python3 /tmp/test_triple.py
```

## Documentation

- **Full Specification**: `docs/LOG-0024-triple-script-translation.md`
- **API Reference**: See docstrings in `src/ute00/scripts/triple_encoder.py`
- **Examples**: `examples/triple_script_example.py`

## References

- LOG-0024: Triple-Script Translation System
- Elder Futhark Runic System
- Tamil Script (Dravidian)
- Harappan/Indus Valley Script
- System שאצ (Universal Translation 0/0)
