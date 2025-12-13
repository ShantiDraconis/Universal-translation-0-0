# Harappan Datasets

This directory contains datasets related to the Harappan (Indus Valley) script.

## Available Datasets

See the main repository at `harappan-00-universal/data/harappan_signs/` for the primary datasets:

- `harappan_417_signs.csv` - 417 Mahadevan signs
- `harappan_417_signs.json` - JSON format
- `wells_694_signs.csv` - 694 Wells variants

## Images

The `images/` subdirectory can contain sign images for OCR and visual reference.

## Data Format

CSV files use UTF-8 encoding with the following standard columns:
- `sign_id` - Unique identifier (M-001 to M-417)
- `description` - Sign description
- `category` - Classification category
- `unicode` - Unicode representation (if available)
- `variants` - Alternative forms

## Sources

- Mahadevan, I. (1977). *The Indus Script: Texts, Concordance and Tables*
- Wells, B. (2006). *Indus Signs: A List of Sign Types*
