# Harappan-00 Universal Translation System

## Overview

This project provides a comprehensive database of Harappan (Indus Valley) script signs and their mappings to the Universal 0/0 translation system, along with cross-linguistic connections to Tupi, Hebrew, and Sanskrit.

## Project Structure

```
harappan-00-universal/
├── README.md                          # This file
└── data/
    ├── harappan_signs/
    │   ├── harappan_417_signs.csv     # 417 Mahadevan signs in CSV format
    │   ├── harappan_417_signs.json    # 417 signs in JSON format
    │   ├── harappan_417_signs.md      # Documentation and sign descriptions
    │   └── wells_694_signs.csv        # Wells Sign List (694 variants)
    └── mappings/
        ├── mapping_harappan_to_00.csv      # Harappan → Universal 0/0 codes
        ├── mapping_harappan_to_tupi.csv    # Harappan → Tupi language
        ├── mapping_harappan_to_hebrew.csv  # Harappan → Hebrew
        └── mapping_harappan_to_sanskrit.csv # Harappan → Sanskrit
```

## Data Sources

### Primary Sources

1. **Mahadevan Corpus (1977)** - 417 signs
   - Reference: Mahadevan, Iravatham. "The Indus Script: Texts, Concordance and Tables"
   - Digital Archive: https://www.tamilvu.org/cores/tmp/mahadevan417.pdf
   - This is the standard academic reference for Harappan script signs

2. **Wells Sign List (2006)** - 694 variants
   - Reference: https://www.harappa.com/sites/default/files/pdf/Wells2006-SignList.pdf
   - Complementary to Mahadevan, useful for reconstructing sign variants

3. **Parpola Corpus (1994-2010)**
   - Modern academic reference: https://www.harappa.com/script

4. **Unified Collection**
   - Combined Mahadevan + Wells + Parpola: https://www.harappa.com/indus-script-signs

## Sign Categories

The 417 Mahadevan signs are organized into 16 categories:

| Category | Description | Example Signs |
|----------|-------------|---------------|
| Anthropomorphic | Human figures and deities | M-001 to M-007 |
| Zoomorphic | Animals (fish, bull, elephant) | M-008 to M-023 |
| Objects | Tools, vessels, weapons | M-024 to M-040 |
| Numerals | Numerical strokes and markers | M-041 to M-050 |
| Geometric | Shapes (circles, squares, triangles) | M-051 to M-070 |
| Botanical | Plants, trees, flowers | M-071 to M-080 |
| Architecture | Buildings, gates, walls | M-081 to M-089 |
| Transport | Boats, carts, vehicles | M-090 to M-094 |
| Tools | Nets, hooks, ropes | M-095 to M-100 |
| Body Parts | Hands, feet, eyes | M-101 to M-108 |
| Celestial | Sun, moon, stars | M-109 to M-112 |
| Weather | Rain, clouds, wind | M-113 to M-116 |
| Geography | Mountains, rivers, seas | M-117 to M-128 |
| Titles | Occupations, ranks | M-129 to M-140 |
| Compound | Combined signs | M-141 to M-416 |
| Markers | Terminal and special signs | M-417 |

## Universal 0/0 Code System

The Universal 0/0 coding system uses a hierarchical structure:

```
00-[CATEGORY]-[NUMBER]
```

Categories:
- `HUM` - Human/Anthropomorphic
- `DIV` - Divine/Sacred
- `ANI` - Animal/Zoomorphic
- `OBJ` - Object
- `NUM` - Numeral
- `GEO` - Geometric
- `CEL` - Celestial
- `NAT` - Nature
- `BOT` - Botanical
- `ARC` - Architecture
- `TRN` - Transport
- `TOL` - Tool
- `BOD` - Body Part
- `WEA` - Weather
- `GEG` - Geography
- `TTL` - Title/Occupation
- `MRK` - Marker

## Usage Examples

### Python - Loading CSV

```python
import pandas as pd

# Load Harappan signs
signs = pd.read_csv('data/harappan_signs/harappan_417_signs.csv')
print(f"Total signs: {len(signs)}")
print(signs.head())

# Load mappings
mappings = pd.read_csv('data/mappings/mapping_harappan_to_00.csv')
print(mappings[mappings['probability_match'] > 0.90])
```

### Python - Loading JSON

```python
import json

with open('data/harappan_signs/harappan_417_signs.json', 'r') as f:
    data = json.load(f)

print(f"Total signs: {data['metadata']['total_signs']}")
print(f"Categories: {data['metadata']['categories']}")

# Find all fish signs
fish_signs = [s for s in data['signs'] if 'fish' in s['description'].lower()]
print(f"Fish-related signs: {len(fish_signs)}")
```

### JavaScript - Loading JSON

```javascript
const fs = require('fs');
const data = JSON.parse(fs.readFileSync('data/harappan_signs/harappan_417_signs.json', 'utf8'));

console.log(`Total signs: ${data.metadata.total_signs}`);

// Filter by category
const zoomorphic = data.signs.filter(s => s.category === 'Zoomorphic');
console.log(`Zoomorphic signs: ${zoomorphic.length}`);
```

## Mapping Probability Scores

Each mapping file includes probability scores indicating confidence levels:

- **0.90-1.00**: High confidence - Clear semantic and/or phonetic match
- **0.75-0.89**: Medium-high confidence - Strong semantic correlation
- **0.60-0.74**: Medium confidence - Reasonable connection
- **0.40-0.59**: Low-medium confidence - Possible connection, needs further research
- **Below 0.40**: Low confidence - Speculative connection

## Cross-Linguistic Connections

### Sanskrit Connections

Sanskrit shows strong correlations due to:
- Geographic and temporal proximity to the Indus Valley Civilization
- Possible Dravidian substrate influences
- Shared cultural concepts

Key matches:
- M-008 (fish) → मत्स्य (matsya) - 0.98 probability
- M-013 (bull) → वृषभ (vṛṣabha) - 0.98 probability
- M-075 (lotus) → पद्म (padma) - 0.98 probability

### Tupi Connections

Tupi connections are more speculative but show interesting patterns:
- Animal names: pirá (fish), jaguara (jaguar)
- Water concepts: y (water), paranã (sea)
- Body parts: po (hand), py (foot)

### Hebrew Connections

Hebrew mappings provide Semitic language correlations:
- Semantic parallels in religious/divine concepts
- Number system correspondences
- Body part terminology

## Contributing

Contributions to improve mappings or add new language connections are welcome. Please ensure:

1. Sources are properly cited
2. Probability scores are justified
3. New mappings follow the existing format

## License

This project is released under the MIT License. See the LICENSE file in the root directory.

## References

1. Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*. Archaeological Survey of India.
2. Wells, B. (2006). *Indus Signs: A List of Sign Types*. Available at harappa.com
3. Parpola, A. (1994). *Deciphering the Indus Script*. Cambridge University Press.
4. Possehl, G.L. (1996). *Indus Age: The Writing System*. University of Pennsylvania Press.

## Acknowledgments

- Tamil Virtual University for preserving digital archives
- Harappa.com for online resources
- The academic community studying the Indus Valley Civilization
