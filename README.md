# Universal Translation 0/0 - Harappan Universal Language Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the research framework for the **Universal Phonemic Kernel Hypothesis (0/0)**, a theoretical proposal that a finite set of primordial phonemic tokens are shared across linguistically distant traditions worldwide.

The project specifically applies this framework to the undeciphered **Indus Valley (Harappan) script**, proposing systematic correspondences between Harappan signs and universal phonemic tokens.

## The Hypothesis

> **There exists a finite set of primordial phonemic tokens, shared transversally by distant linguistic traditions (Harappan, Tupi-Guarani, Dravidian, Indo-European, Afro-Atlantic, Semitic, etc.), which encode:**
> 
> 1. Cosmological categories (primordial water, ritual fire, light, time, sky, earth)
> 2. Archetypal roles (mother-matrix, hero, serpent, lord, child, sacred city)
> 3. Ontological operations (create, cut the void, serve, open portal)
> 4. Numerical/temporal structures (cycles, seven, nine, unity, plurality)

The symbolic operator **I = 0/0** represents the indeterminate nucleus from which these units emerge—the "collapse point" between language, consciousness, body, and cosmos.

## Repository Structure

```
├── data/
│   ├── harappan_signs.csv         # Catalog of 50 core Harappan signs
│   └── universal_dictionary_00.csv # 100 universal phonemic tokens
├── src/
│   └── analysis.py                # Analysis framework (Python)
├── docs/
│   ├── harappan-00-main-paper.tex # Main academic article (LaTeX)
│   ├── thesis-foundation.md       # Historical/social/psychological foundation
│   └── academic-checklist.md      # Academic requirements checklist
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- LaTeX distribution (for compiling the paper)

### Running the Analysis

```bash
cd src
python analysis.py
```

This generates an analysis report showing:
- Token statistics by cosmological category
- Cognate pattern analysis across language families
- Cross-linguistic patterns with strong evidence
- Harappan sign linkage statistics
- Statistical significance estimates

### Building the Paper

```bash
cd docs
pdflatex harappan-00-main-paper.tex
bibtex harappan-00-main-paper
pdflatex harappan-00-main-paper.tex
pdflatex harappan-00-main-paper.tex
```

## Data Files

### harappan_signs.csv

Catalog of 50 core Harappan signs with fields:
- `sign_id`: Unique identifier (H001-H050)
- `unicode_approx`: Unicode approximation
- `variants`: Variant forms
- `phonetic_value_proposed`: Proposed phonetic value
- `semantic_category`: Semantic category
- `universal_token_link`: Link to universal dictionary
- `frequency`: High/medium/low
- `contexts`: Where sign appears (seals, tablets, etc.)

### universal_dictionary_00.csv

100 universal phonemic tokens with fields:
- `token_id`: Unique identifier (T001-T100)
- `token`: The phonemic token
- `phonetic_ipa`: IPA transcription
- `semantic_core`: Core semantic meaning
- `cosmological_category`: Cosmological category
- `archetype`: Archetypal association
- `tupi_cognate`: Tupi-Guarani cognate
- `sanskrit_cognate`: Sanskrit cognate
- `hebrew_cognate`: Hebrew cognate
- `tamil_cognate`: Tamil cognate
- `yoruba_cognate`: Yoruba cognate
- `harappan_link`: Link to Harappan sign
- `notes`: Additional notes

## Key Findings

### Cross-Linguistic Patterns

Analysis reveals significant cross-linguistic patterns:

| Language Family | Cognates Found | Percentage |
|-----------------|----------------|------------|
| Sanskrit/Indo-Aryan | 68 | 68% |
| Tamil/Dravidian | 52 | 52% |
| Tupi-Guarani | 24 | 24% |
| Yoruba/Niger-Congo | 22 | 22% |
| Hebrew/Semitic | 18 | 18% |

### Tokens with Strong Evidence

18 tokens show cognates in 3 or more language families, including:
- **AMA** (mother/source) - Sanskrit, Tamil, Hebrew, Yoruba
- **BABA** (father/elder) - Sanskrit, Tamil, Yoruba
- **AGNI** (fire/divine) - Sanskrit, Tamil, Hebrew, Yoruba
- **RA** (sun/light) - Sanskrit, Tamil, Hebrew

### Statistical Significance

- Total comparisons: 500
- Observed matches: 184
- Expected random: ~10
- **p-value: < 0.0001**

Patterns are highly unlikely to occur by chance.

## Documentation

- [Thesis Foundation](docs/thesis-foundation.md) - Historical, social, and psychological analysis supporting the thesis
- [Academic Checklist](docs/academic-checklist.md) - Requirements for academic formalization and major prize consideration
- [Main Paper](docs/harappan-00-main-paper.tex) - Full academic article in LaTeX

## Contributing

Contributions are welcome. Areas particularly needing development:

1. **Data Expansion**: Add more tokens to the Universal Dictionary (target: 1000)
2. **Cognate Verification**: Verify and expand cognate mappings
3. **Statistical Methods**: Refine statistical significance testing
4. **Harappan Mapping**: Expand Harappan sign catalog to full 417 signs
5. **Visualization**: Create visualizations of cross-linguistic patterns

## Citation

If you use this work, please cite:

```bibtex
@misc{universal_translation_00,
  author = {Universal Translation Project},
  title = {Harappan 00: A Universal Symbolic Kernel of Language},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/harappan-00-universal}
}
```

## Related Work

- Parpola, A. (1994). *Deciphering the Indus Script*. Cambridge University Press.
- Ruhlen, M. (1994). *On the Origin of Languages*. Stanford University Press.
- Hinton, L., et al. (1994). *Sound Symbolism*. Cambridge University Press.
- Bomhard, A.R. (2008). *Reconstructing Proto-Nostratic*. Brill.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or collaboration inquiries, please open an issue in this repository.

---

*Part of the Universal Translation Project*
