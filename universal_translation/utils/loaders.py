"""
universal_translation/utils/loaders.py

Data loading utilities (CSV/JSON) for the Universal Translation Engine.

This module provides standardized loading functions for:
- CSV datasets (Harappan signs, mappings, phonemes)
- JSON configuration and mapping files
- YAML configuration files

Example:
    >>> from universal_translation.utils.loaders import load_csv
    >>> from pathlib import Path
    >>> data = load_csv(Path("./data/harappan_signs.csv"))
    >>> print(len(data))
"""

from pathlib import Path
from typing import Any, Dict, List, Optional
import csv
import json


def load_csv(path: Path, encoding: str = "utf-8") -> List[Dict[str, Any]]:
    """
    Load a CSV file into a list of dictionaries.

    Parameters
    ----------
    path : Path
        Path to the CSV file.
    encoding : str
        File encoding (default: utf-8).

    Returns
    -------
    List[Dict[str, Any]]
        List of rows as dictionaries.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open(encoding=encoding) as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_json(path: Path, encoding: str = "utf-8") -> Any:
    """
    Load a JSON file.

    Parameters
    ----------
    path : Path
        Path to the JSON file.
    encoding : str
        File encoding (default: utf-8).

    Returns
    -------
    Any
        Parsed JSON content.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")

    with path.open(encoding=encoding) as f:
        return json.load(f)


def load_yaml(path: Path, encoding: str = "utf-8") -> Any:
    """
    Load a YAML file.

    Requires PyYAML to be installed.

    Parameters
    ----------
    path : Path
        Path to the YAML file.
    encoding : str
        File encoding (default: utf-8).

    Returns
    -------
    Any
        Parsed YAML content.
    """
    try:
        import yaml
    except ImportError:
        raise ImportError("PyYAML is required for YAML loading. Install with: pip install pyyaml")

    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")

    with path.open(encoding=encoding) as f:
        return yaml.safe_load(f)


def save_csv(
    data: List[Dict[str, Any]],
    path: Path,
    encoding: str = "utf-8",
    fieldnames: Optional[List[str]] = None,
) -> None:
    """
    Save a list of dictionaries to a CSV file.

    Parameters
    ----------
    data : List[Dict[str, Any]]
        Data to save.
    path : Path
        Output file path.
    encoding : str
        File encoding (default: utf-8).
    fieldnames : Optional[List[str]]
        Column names. If None, uses keys from first row.
    """
    if not data:
        return

    if fieldnames is None:
        fieldnames = list(data[0].keys())

    with path.open("w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def save_json(data: Any, path: Path, encoding: str = "utf-8", indent: int = 2) -> None:
    """
    Save data to a JSON file.

    Parameters
    ----------
    data : Any
        Data to save.
    path : Path
        Output file path.
    encoding : str
        File encoding (default: utf-8).
    indent : int
        JSON indentation level.
    """
    with path.open("w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def get_datasets_path() -> Path:
    """
    Get the path to the datasets directory.

    Returns
    -------
    Path
        Path to the datasets directory.
    """
    return Path(__file__).parent.parent / "datasets"


def get_mappings_path() -> Path:
    """
    Get the path to the mappings directory.

    Returns
    -------
    Path
        Path to the mappings directory.
    """
    return Path(__file__).parent.parent / "mappings"


def list_available_datasets(dataset_type: str = "all") -> List[str]:
    """
    List available datasets.

    Parameters
    ----------
    dataset_type : str
        Type of datasets: 'harappan', 'universal', or 'all'.

    Returns
    -------
    List[str]
        List of available dataset names.
    """
    datasets_path = get_datasets_path()
    available = []

    if dataset_type in ("harappan", "all"):
        harappan_path = datasets_path / "harappan"
        if harappan_path.exists():
            available.extend([f"harappan/{f.name}" for f in harappan_path.glob("*.csv")])
            available.extend([f"harappan/{f.name}" for f in harappan_path.glob("*.json")])

    if dataset_type in ("universal", "all"):
        universal_path = datasets_path / "universal"
        if universal_path.exists():
            available.extend([f"universal/{f.name}" for f in universal_path.glob("*.csv")])
            available.extend([f"universal/{f.name}" for f in universal_path.glob("*.json")])

    return sorted(available)
