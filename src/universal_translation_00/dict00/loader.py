"""
Dictionary 0/0 Loader for Universal Translation 0/0.

Loads and indexes the universal phonetic dictionary.
"""

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from universal_translation_00.config import DICTIONARY_00_CSV, PROCESSED_DATA_DIR


@dataclass
class DictEntry:
    """A dictionary entry with phoneme and meanings."""

    token: int
    phoneme: str
    meaning_en: str
    meaning_pt: str
    semantic_class: str
    frequency: str

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "token": self.token,
            "phoneme": self.phoneme,
            "meaning_en": self.meaning_en,
            "meaning_pt": self.meaning_pt,
            "semantic_class": self.semantic_class,
            "frequency": self.frequency,
        }


class Dict00Loader:
    """
    Loads and provides access to the Dictionary 0/0.

    The dictionary contains universal phonetic tokens with
    meanings across multiple languages.
    """

    def __init__(self, data_file: Optional[Path] = None) -> None:
        """
        Initialize the dictionary loader.

        Args:
            data_file: Path to CSV file (uses default if None)
        """
        self.data_file = data_file or DICTIONARY_00_CSV
        self._entries: list[DictEntry] = []
        self._by_token: dict[int, DictEntry] = {}
        self._by_phoneme: dict[str, list[DictEntry]] = {}
        self._by_class: dict[str, list[DictEntry]] = {}
        self._loaded = False

    def _ensure_loaded(self) -> None:
        """Ensure dictionary is loaded."""
        if not self._loaded:
            self._load()

    def _load(self) -> None:
        """Load dictionary from CSV."""
        if not self.data_file.exists():
            self._generate_default()
            return

        with open(self.data_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                entry = DictEntry(
                    token=int(row["token"]),
                    phoneme=row["phoneme"],
                    meaning_en=row["meaning_en"],
                    meaning_pt=row["meaning_pt"],
                    semantic_class=row["semantic_class"],
                    frequency=row["frequency"],
                )
                self._add_entry(entry)

        self._loaded = True

    def _add_entry(self, entry: DictEntry) -> None:
        """Add entry to all indexes."""
        self._entries.append(entry)
        self._by_token[entry.token] = entry

        if entry.phoneme not in self._by_phoneme:
            self._by_phoneme[entry.phoneme] = []
        self._by_phoneme[entry.phoneme].append(entry)

        if entry.semantic_class not in self._by_class:
            self._by_class[entry.semantic_class] = []
        self._by_class[entry.semantic_class].append(entry)

    def _generate_default(self) -> None:
        """Generate default dictionary entries."""
        default_entries = [
            (1, "a", "open/from", "abrir/de", "abstract", "high"),
            (2, "i", "this/is", "isto/é", "abstract", "high"),
            (3, "u", "that/mouth", "aquilo/boca", "abstract", "high"),
            (4, "e", "toward/from", "para/de", "abstract", "high"),
            (5, "o", "whole/unity", "todo/unidade", "abstract", "high"),
            (6, "ma", "mother/matter", "mãe/matéria", "human", "high"),
            (7, "na", "self/person", "eu/pessoa", "human", "high"),
            (8, "ka", "object/place", "objeto/lugar", "container", "high"),
            (9, "ta", "action/do", "ação/fazer", "operator", "high"),
            (10, "sa", "sacred/spirit", "sagrado/espírito", "ritual", "high"),
        ]

        for token, phoneme, meaning_en, meaning_pt, sem_class, freq in default_entries:
            entry = DictEntry(
                token=token,
                phoneme=phoneme,
                meaning_en=meaning_en,
                meaning_pt=meaning_pt,
                semantic_class=sem_class,
                frequency=freq,
            )
            self._add_entry(entry)

        self._loaded = True

    def get_entry(self, token: int) -> Optional[DictEntry]:
        """Get entry by token number."""
        self._ensure_loaded()
        return self._by_token.get(token)

    def get_by_phoneme(self, phoneme: str) -> list[DictEntry]:
        """Get all entries for a phoneme."""
        self._ensure_loaded()
        return self._by_phoneme.get(phoneme.lower(), [])

    def get_by_class(self, semantic_class: str) -> list[DictEntry]:
        """Get all entries in a semantic class."""
        self._ensure_loaded()
        return self._by_class.get(semantic_class.lower(), [])

    def get_all_entries(self) -> list[DictEntry]:
        """Get all dictionary entries."""
        self._ensure_loaded()
        return self._entries.copy()

    def get_all_phonemes(self) -> list[str]:
        """Get all unique phonemes."""
        self._ensure_loaded()
        return list(self._by_phoneme.keys())

    def export_json(self, output_path: Optional[Path] = None) -> None:
        """Export dictionary to JSON."""
        self._ensure_loaded()
        output = output_path or PROCESSED_DATA_DIR / "dict00_full.json"
        output.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "entries": [e.to_dict() for e in self._entries],
            "by_phoneme": {
                p: [e.to_dict() for e in entries]
                for p, entries in self._by_phoneme.items()
            },
        }

        with open(output, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
