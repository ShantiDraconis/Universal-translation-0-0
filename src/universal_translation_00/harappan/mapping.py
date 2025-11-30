"""
Harappan Sign Mapping for Universal Translation 0/0.

Maps phonemes to Harappan signs based on cross-linguistic
analysis of Tamil, Chinese, Norse, Latin, and Tupi roots.
"""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from universal_translation_00.config import HARAPPAN_417_CSV, SEMANTIC_GROUPS


@dataclass
class HarappanSign:
    """Represents a single Harappan sign with all metadata."""

    id: str  # H001-H417
    group: str  # Short group code (NUM, CON, etc.)
    group_full: str  # Full group name
    phoneme: str  # Assigned phoneme
    semantic_field: str  # Semantic category
    tamil_root: str  # Tamil cognate
    chinese_root: str  # Chinese cognate
    norse_root: str  # Old Norse cognate
    latin_root: str  # Latin cognate
    tupi_root: str  # Tupi cognate
    description: str  # Sign description

    def __repr__(self) -> str:
        return f"HarappanSign({self.id}, phoneme={self.phoneme!r}, group={self.group})"

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "group": self.group,
            "group_full": self.group_full,
            "phoneme": self.phoneme,
            "semantic_field": self.semantic_field,
            "tamil_root": self.tamil_root,
            "chinese_root": self.chinese_root,
            "norse_root": self.norse_root,
            "latin_root": self.latin_root,
            "tupi_root": self.tupi_root,
            "description": self.description,
        }

    def get_cognates(self) -> dict[str, str]:
        """Get all language cognates."""
        return {
            "tamil": self.tamil_root,
            "chinese": self.chinese_root,
            "norse": self.norse_root,
            "latin": self.latin_root,
            "tupi": self.tupi_root,
        }


class HarappanMapping:
    """
    Maps between phonemes and Harappan signs.

    Uses the 417 Harappan signs mapped to phonemes based on
    cross-linguistic analysis of multiple language families.
    """

    def __init__(self, data_file: Optional[Path] = None) -> None:
        """
        Initialize the Harappan mapping.

        Args:
            data_file: Path to CSV data file (uses default if None)
        """
        self.data_file = data_file or HARAPPAN_417_CSV
        self._signs_by_id: dict[str, HarappanSign] = {}
        self._signs_by_phoneme: dict[str, list[HarappanSign]] = {}
        self._signs_by_group: dict[str, list[HarappanSign]] = {}
        self._loaded = False

    def _ensure_loaded(self) -> None:
        """Ensure data is loaded."""
        if not self._loaded:
            self._load_data()

    def _load_data(self) -> None:
        """Load Harappan data from CSV."""
        if not self.data_file.exists():
            # Generate default data if file doesn't exist
            self._generate_default_data()
            return

        with open(self.data_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sign = HarappanSign(
                    id=row["id"],
                    group=row["group"],
                    group_full=row["group_full"],
                    phoneme=row["phoneme"],
                    semantic_field=row["semantic_field"],
                    tamil_root=row["tamil_root"],
                    chinese_root=row["chinese_root"],
                    norse_root=row["norse_root"],
                    latin_root=row["latin_root"],
                    tupi_root=row["tupi_root"],
                    description=row["description"],
                )
                self._add_sign(sign)

        self._loaded = True

    def _add_sign(self, sign: HarappanSign) -> None:
        """Add a sign to all indexes."""
        self._signs_by_id[sign.id] = sign

        if sign.phoneme not in self._signs_by_phoneme:
            self._signs_by_phoneme[sign.phoneme] = []
        self._signs_by_phoneme[sign.phoneme].append(sign)

        if sign.group not in self._signs_by_group:
            self._signs_by_group[sign.group] = []
        self._signs_by_group[sign.group].append(sign)

    def _generate_default_data(self) -> None:
        """Generate default mapping based on semantic groups."""
        for group_code, group_info in SEMANTIC_GROUPS.items():
            start, end = group_info["range"]
            phonemes = group_info["phonemes"]
            full_name = group_info["full_name"]
            semantic = group_info["semantic_field"]

            for i, num in enumerate(range(start, end + 1)):
                phoneme = phonemes[i % len(phonemes)]
                sign_id = f"H{num:03d}"
                sign = HarappanSign(
                    id=sign_id,
                    group=group_code,
                    group_full=full_name,
                    phoneme=phoneme,
                    semantic_field=semantic,
                    tamil_root="",
                    chinese_root="",
                    norse_root="",
                    latin_root="",
                    tupi_root="",
                    description=f"{full_name} sign {num}",
                )
                self._add_sign(sign)

        self._loaded = True

    def get_sign(self, sign_id: str) -> Optional[HarappanSign]:
        """
        Get a Harappan sign by ID.

        Args:
            sign_id: The sign ID (e.g., 'H001')

        Returns:
            HarappanSign or None if not found
        """
        self._ensure_loaded()
        # Normalize ID format
        if not sign_id.startswith("H"):
            sign_id = f"H{int(sign_id):03d}"
        return self._signs_by_id.get(sign_id)

    def phoneme_to_sign(self, phoneme: str) -> Optional[HarappanSign]:
        """
        Get the first Harappan sign for a phoneme.

        Args:
            phoneme: The phoneme (e.g., 'ta', 'ma')

        Returns:
            First matching HarappanSign or None
        """
        self._ensure_loaded()
        signs = self._signs_by_phoneme.get(phoneme.lower(), [])
        return signs[0] if signs else None

    def phoneme_to_signs(self, phoneme: str) -> list[HarappanSign]:
        """
        Get all Harappan signs for a phoneme.

        Args:
            phoneme: The phoneme

        Returns:
            List of matching HarappanSign objects
        """
        self._ensure_loaded()
        return self._signs_by_phoneme.get(phoneme.lower(), [])

    def get_signs_by_group(self, group: str) -> list[HarappanSign]:
        """
        Get all signs in a semantic group.

        Args:
            group: Group code (e.g., 'NUM', 'CON')

        Returns:
            List of HarappanSign objects in the group
        """
        self._ensure_loaded()
        return self._signs_by_group.get(group.upper(), [])

    def get_all_signs(self) -> list[HarappanSign]:
        """Get all 417 Harappan signs."""
        self._ensure_loaded()
        return list(self._signs_by_id.values())

    def get_all_phonemes(self) -> list[str]:
        """Get all unique phonemes in the mapping."""
        self._ensure_loaded()
        return list(self._signs_by_phoneme.keys())

    def get_all_groups(self) -> list[str]:
        """Get all semantic group codes."""
        self._ensure_loaded()
        return list(self._signs_by_group.keys())

    def search_by_semantic_field(self, query: str) -> list[HarappanSign]:
        """
        Search signs by semantic field.

        Args:
            query: Search term

        Returns:
            List of matching signs
        """
        self._ensure_loaded()
        query = query.lower()
        return [
            sign for sign in self._signs_by_id.values()
            if query in sign.semantic_field.lower() or query in sign.description.lower()
        ]

    def get_statistics(self) -> dict:
        """Get statistics about the mapping."""
        self._ensure_loaded()
        return {
            "total_signs": len(self._signs_by_id),
            "unique_phonemes": len(self._signs_by_phoneme),
            "groups": len(self._signs_by_group),
            "phoneme_distribution": {
                phoneme: len(signs)
                for phoneme, signs in self._signs_by_phoneme.items()
            },
            "group_sizes": {
                group: len(signs)
                for group, signs in self._signs_by_group.items()
            },
        }
