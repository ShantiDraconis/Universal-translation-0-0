# Harappan Sign List

This document provides a comprehensive list of Harappan (Indus Valley) script signs
based on the Mahadevan corpus (1977).

## Overview

The Harappan script contains approximately 417 distinct signs in the Mahadevan
classification system, plus 694 variants in the Wells system.

## Sign Categories

| Category | Range | Count | Description |
|----------|-------|-------|-------------|
| Anthropomorphic | M-001 to M-007 | 7 | Human figures and deities |
| Zoomorphic | M-008 to M-023 | 16 | Animals (fish, bull, elephant) |
| Objects | M-024 to M-040 | 17 | Tools, vessels, weapons |
| Numerals | M-041 to M-050 | 10 | Numerical strokes and markers |
| Geometric | M-051 to M-070 | 20 | Shapes (circles, squares, triangles) |
| Botanical | M-071 to M-080 | 10 | Plants, trees, flowers |
| Architecture | M-081 to M-089 | 9 | Buildings, gates, walls |
| Transport | M-090 to M-094 | 5 | Boats, carts, vehicles |
| Tools | M-095 to M-100 | 6 | Nets, hooks, ropes |
| Body Parts | M-101 to M-108 | 8 | Hands, feet, eyes |
| Celestial | M-109 to M-112 | 4 | Sun, moon, stars |
| Weather | M-113 to M-116 | 4 | Rain, clouds, wind |
| Geography | M-117 to M-128 | 12 | Mountains, rivers, seas |
| Titles | M-129 to M-140 | 12 | Occupations, ranks |
| Compound | M-141 to M-416 | 276 | Combined signs |
| Markers | M-417 | 1 | Terminal and special signs |

## Key Signs

### Anthropomorphic Signs (M-001 to M-007)

| Sign ID | Description | Universal Code |
|---------|-------------|----------------|
| M-001 | Standing human figure | 00-HUM-001 |
| M-002 | Seated human figure | 00-HUM-002 |
| M-003 | Human with raised arms | 00-HUM-003 |
| M-004 | Human in ritual pose | 00-HUM-004 |
| M-005 | Divine/horned figure | 00-HUM-005 |
| M-006 | Human with object | 00-HUM-006 |
| M-007 | Composite human figure | 00-HUM-007 |

### Zoomorphic Signs (M-008 to M-023)

| Sign ID | Description | Universal Code | Cross-linguistic |
|---------|-------------|----------------|------------------|
| M-008 | Fish | 00-ANI-008 | Sanskrit: matsya, Tamil: meen, Tupi: pirá |
| M-009 | Fish with mark | 00-ANI-009 | |
| M-010 | Fish with stroke | 00-ANI-010 | |
| M-011 | Double fish | 00-ANI-011 | |
| M-012 | Bird | 00-ANI-012 | |
| M-013 | Bull/Bovine | 00-ANI-013 | Sanskrit: vṛṣabha |
| M-014 | Elephant | 00-ANI-014 | |
| M-015 | Tiger/Feline | 00-ANI-015 | |
| M-016 | Rhinoceros | 00-ANI-016 | |
| M-017 | Antelope/Deer | 00-ANI-017 | |
| M-018 | Goat | 00-ANI-018 | |
| M-019 | Hare | 00-ANI-019 | |
| M-020 | Crocodile | 00-ANI-020 | |
| M-021 | Snake/Serpent | 00-ANI-021 | |
| M-022 | Scorpion | 00-ANI-022 | |
| M-023 | Insect/Bee | 00-ANI-023 | |

### Numeral Signs (M-041 to M-050)

| Sign ID | Description | Value |
|---------|-------------|-------|
| M-041 | Single stroke | 1 |
| M-042 | Double stroke | 2 |
| M-043 | Triple stroke | 3 |
| M-044 | Four strokes | 4 |
| M-045 | Five strokes | 5 |
| M-046 | Six strokes | 6 |
| M-047 | Seven strokes | 7 |
| M-048 | Curved numeral | 10? |
| M-049 | Circle numeral | 100? |
| M-050 | Complex numeral | ? |

### Botanical Signs (M-071 to M-080)

| Sign ID | Description | Universal Code | Cross-linguistic |
|---------|-------------|----------------|------------------|
| M-071 | Tree | 00-BOT-071 | |
| M-072 | Branch | 00-BOT-072 | |
| M-073 | Leaf | 00-BOT-073 | |
| M-074 | Flower | 00-BOT-074 | |
| M-075 | Lotus | 00-BOT-075 | Sanskrit: padma, Tamil: tāmarai |
| M-076 | Pipal tree | 00-BOT-076 | |
| M-077 | Grain/wheat | 00-BOT-077 | |
| M-078 | Plant with roots | 00-BOT-078 | |
| M-079 | Fruit | 00-BOT-079 | |
| M-080 | Seed | 00-BOT-080 | |

### Celestial Signs (M-109 to M-112)

| Sign ID | Description | Universal Code |
|---------|-------------|----------------|
| M-109 | Sun/Wheel | 00-CEL-109 |
| M-110 | Moon/Crescent | 00-CEL-110 |
| M-111 | Star | 00-CEL-111 |
| M-112 | Celestial body | 00-CEL-112 |

## Sign Frequency

The most frequent signs in the corpus:

| Rank | Sign ID | Occurrences | Description |
|------|---------|-------------|-------------|
| 1 | M-008 | 1,500+ | Fish |
| 2 | M-041 | 1,200+ | Single stroke |
| 3 | M-042 | 800+ | Double stroke |
| 4 | M-013 | 700+ | Bull |
| 5 | M-075 | 500+ | Lotus |

## Sign Combinations

Common sign sequences:

| Sequence | Frequency | Interpretation |
|----------|-----------|----------------|
| M-008 + M-041 | High | Fish + numeral |
| M-013 + M-008 | Medium | Bull + fish |
| M-075 + M-001 | Medium | Lotus + human |

## Universal 0/0 Integration

Each Harappan sign maps to a Universal 0/0 code:

```
00-[CATEGORY]-[NUMBER]
```

Where CATEGORY is:
- `HUM` - Human/Anthropomorphic
- `ANI` - Animal/Zoomorphic
- `OBJ` - Object
- `NUM` - Numeral
- `GEO` - Geometric
- `BOT` - Botanical
- `ARC` - Architecture
- `TRN` - Transport
- `TOL` - Tool
- `BOD` - Body Part
- `CEL` - Celestial
- `WEA` - Weather
- `GEG` - Geography
- `TTL` - Title
- `CMP` - Compound
- `MRK` - Marker

## References

1. Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*. Archaeological Survey of India.
2. Wells, B. (2006). *Indus Signs: A List of Sign Types*. Available at harappa.com
3. Parpola, A. (1994). *Deciphering the Indus Script*. Cambridge University Press.

## Data Files

Full sign data available in:
- `harappan-00-universal/data/harappan_signs/harappan_417_signs.csv`
- `harappan-00-universal/data/harappan_signs/harappan_417_signs.json`
- `harappan-00-universal/data/harappan_signs/wells_694_signs.csv`
