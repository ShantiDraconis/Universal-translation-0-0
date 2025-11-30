"""
universal_translation/core/ocr_signs.py

Placeholder module for Harappan sign OCR and image processing.

This module will handle:
- Image-based sign recognition
- Sign variant detection
- Image preprocessing for analysis

Example:
    >>> from universal_translation.core.ocr_signs import list_sign_images
    >>> from pathlib import Path
    >>> images = list_sign_images(Path("./datasets/harappan/images"))
    >>> print(len(images))
"""

from pathlib import Path
from typing import List, Dict, Any, Optional

# Supported image formats
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"}


def list_sign_images(root: Path) -> List[Path]:
    """
    List all image files under a given directory.

    Parameters
    ----------
    root : Path
        Root directory to search.

    Returns
    -------
    List[Path]
        List of image file paths.
    """
    if not root.exists():
        return []

    return [
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    ]


def get_image_info(image_path: Path) -> Dict[str, Any]:
    """
    Get basic information about an image file.

    Parameters
    ----------
    image_path : Path
        Path to the image file.

    Returns
    -------
    Dict[str, Any]
        Dictionary with image metadata.
    """
    if not image_path.exists():
        return {"error": "File not found"}

    stat = image_path.stat()

    return {
        "path": str(image_path),
        "name": image_path.name,
        "extension": image_path.suffix.lower(),
        "size_bytes": stat.st_size,
    }


def extract_sign_id_from_filename(filename: str) -> Optional[int]:
    """
    Extract a sign ID from a filename.

    Assumes filenames follow patterns like:
    - M-001.png
    - sign_15.jpg
    - harappan_42.png

    Parameters
    ----------
    filename : str
        The filename to parse.

    Returns
    -------
    Optional[int]
        Extracted sign ID or None if not found.
    """
    import re

    # Try different patterns
    patterns = [
        r"M-?(\d+)",  # Mahadevan format: M-001, M001
        r"W-?(\d+)",  # Wells format: W-001, W001
        r"sign_?(\d+)",  # Generic: sign_1, sign1
        r"harappan_?(\d+)",  # Specific: harappan_1
        r"(\d+)",  # Just a number
    ]

    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            return int(match.group(1))

    return None


def create_image_catalog(root: Path) -> List[Dict[str, Any]]:
    """
    Create a catalog of all sign images in a directory.

    Parameters
    ----------
    root : Path
        Root directory to catalog.

    Returns
    -------
    List[Dict[str, Any]]
        List of image entries with metadata.
    """
    images = list_sign_images(root)
    catalog = []

    for img_path in images:
        info = get_image_info(img_path)
        sign_id = extract_sign_id_from_filename(img_path.name)

        entry = {
            **info,
            "sign_id": sign_id,
            "has_sign_id": sign_id is not None,
        }
        catalog.append(entry)

    return catalog


# Placeholder for future OCR functionality
def recognize_sign(image_path: Path) -> Dict[str, Any]:
    """
    Placeholder for sign recognition functionality.

    This function will eventually use image processing/ML
    to identify Harappan signs in images.

    Parameters
    ----------
    image_path : Path
        Path to the image file.

    Returns
    -------
    Dict[str, Any]
        Recognition results (placeholder).
    """
    return {
        "status": "not_implemented",
        "message": "Sign recognition requires additional dependencies (PIL, OpenCV, etc.)",
        "image": str(image_path),
    }
