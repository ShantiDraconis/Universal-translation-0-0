"""
universal_translation/utils/validators.py

Validation helpers for datasets and mappings.

This module provides validation functions for:
- CSV format and structure validation
- Data uniqueness checks
- UTF-8 encoding validation
- Sign ID format validation

Example:
    >>> from universal_translation.utils.validators import ensure_unique
    >>> values = ["a", "b", "c"]
    >>> print(ensure_unique(values))
    True
"""

from typing import Sequence, List, Dict, Any, Optional, Tuple
from pathlib import Path


def ensure_unique(values: Sequence[str]) -> bool:
    """
    Check if all values in a sequence are unique.

    Parameters
    ----------
    values : Sequence[str]
        Sequence of values to check.

    Returns
    -------
    bool
        True if all values are unique, False otherwise.
    """
    return len(set(values)) == len(values)


def find_duplicates(values: Sequence[str]) -> List[str]:
    """
    Find duplicate values in a sequence.

    Parameters
    ----------
    values : Sequence[str]
        Sequence of values to check.

    Returns
    -------
    List[str]
        List of duplicate values.
    """
    seen = set()
    duplicates = []

    for v in values:
        if v in seen:
            if v not in duplicates:
                duplicates.append(v)
        else:
            seen.add(v)

    return duplicates


def validate_csv_format(
    data: List[Dict[str, Any]],
    required_columns: Optional[List[str]] = None,
) -> Tuple[bool, List[str]]:
    """
    Validate that CSV data has the expected format.

    Parameters
    ----------
    data : List[Dict[str, Any]]
        Loaded CSV data.
    required_columns : Optional[List[str]]
        List of required column names.

    Returns
    -------
    Tuple[bool, List[str]]
        (is_valid, list of error messages)
    """
    errors = []

    if not data:
        errors.append("CSV is empty")
        return False, errors

    # Check for required columns
    if required_columns:
        actual_columns = set(data[0].keys())
        missing = set(required_columns) - actual_columns
        if missing:
            errors.append(f"Missing required columns: {missing}")

    # Check for consistent columns across rows
    first_row_cols = set(data[0].keys())
    for i, row in enumerate(data[1:], start=2):
        row_cols = set(row.keys())
        if row_cols != first_row_cols:
            extra = row_cols - first_row_cols
            missing = first_row_cols - row_cols
            if extra:
                errors.append(f"Row {i} has extra columns: {extra}")
            if missing:
                errors.append(f"Row {i} has missing columns: {missing}")

    return len(errors) == 0, errors


def validate_utf8_file(path: Path) -> Tuple[bool, Optional[str]]:
    """
    Validate that a file is properly encoded as UTF-8.

    Parameters
    ----------
    path : Path
        Path to the file.

    Returns
    -------
    Tuple[bool, Optional[str]]
        (is_valid, error message if invalid)
    """
    try:
        with path.open("r", encoding="utf-8") as f:
            f.read()
        return True, None
    except UnicodeDecodeError as e:
        return False, f"UTF-8 decoding error: {e}"
    except FileNotFoundError:
        return False, f"File not found: {path}"


def validate_sign_id(sign_id: str) -> Tuple[bool, Optional[str]]:
    """
    Validate a Harappan sign ID format.

    Valid formats:
    - M-001 to M-417 (Mahadevan)
    - W-001 to W-694 (Wells)
    - Numeric only (1-417 or 1-694)

    Parameters
    ----------
    sign_id : str
        Sign ID to validate.

    Returns
    -------
    Tuple[bool, Optional[str]]
        (is_valid, error message if invalid)
    """
    import re

    # Pattern for M-xxx or W-xxx
    pattern_prefixed = r"^[MW]-(\d{1,3})$"
    # Pattern for just numbers
    pattern_numeric = r"^\d{1,3}$"

    if re.match(pattern_prefixed, sign_id):
        prefix = sign_id[0]
        number = int(sign_id[2:])

        if prefix == "M" and 1 <= number <= 417:
            return True, None
        elif prefix == "W" and 1 <= number <= 694:
            return True, None
        else:
            return False, f"Sign number out of range: {sign_id}"

    elif re.match(pattern_numeric, sign_id):
        number = int(sign_id)
        if 1 <= number <= 694:
            return True, None
        else:
            return False, f"Sign number out of range: {sign_id}"

    else:
        return False, f"Invalid sign ID format: {sign_id}"


def validate_mapping_entry(entry: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validate a mapping entry.

    Parameters
    ----------
    entry : Dict[str, Any]
        Mapping entry to validate.

    Returns
    -------
    Tuple[bool, List[str]]
        (is_valid, list of error messages)
    """
    errors = []

    # Check for required fields
    required = ["source", "target"]
    for field in required:
        if field not in entry:
            errors.append(f"Missing required field: {field}")

    # Check probability if present
    if "probability_match" in entry:
        try:
            prob = float(entry["probability_match"])
            if not 0 <= prob <= 1:
                errors.append(f"Probability out of range [0,1]: {prob}")
        except (ValueError, TypeError):
            errors.append(f"Invalid probability value: {entry['probability_match']}")

    return len(errors) == 0, errors


def validate_dataset(
    path: Path,
    dataset_type: str = "generic",
) -> Dict[str, Any]:
    """
    Perform comprehensive validation of a dataset file.

    Parameters
    ----------
    path : Path
        Path to the dataset file.
    dataset_type : str
        Type of dataset: 'harappan_signs', 'mapping', or 'generic'.

    Returns
    -------
    Dict[str, Any]
        Validation report.
    """
    report = {
        "path": str(path),
        "type": dataset_type,
        "valid": True,
        "errors": [],
        "warnings": [],
    }

    # Check UTF-8
    utf8_valid, utf8_error = validate_utf8_file(path)
    if not utf8_valid:
        report["valid"] = False
        report["errors"].append(utf8_error)
        return report

    # Load and validate based on type
    from universal_translation.utils.loaders import load_csv

    try:
        data = load_csv(path)
    except Exception as e:
        report["valid"] = False
        report["errors"].append(f"Failed to load CSV: {e}")
        return report

    report["row_count"] = len(data)

    # Type-specific validation
    if dataset_type == "harappan_signs":
        valid, errors = validate_csv_format(
            data, required_columns=["sign_id", "description", "category"]
        )
        if not valid:
            report["valid"] = False
            report["errors"].extend(errors)

    elif dataset_type == "mapping":
        valid, errors = validate_csv_format(
            data, required_columns=["source", "target"]
        )
        if not valid:
            report["valid"] = False
            report["errors"].extend(errors)

    else:
        valid, errors = validate_csv_format(data)
        if not valid:
            report["warnings"].extend(errors)

    return report
