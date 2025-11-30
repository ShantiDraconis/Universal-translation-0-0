"""
Universal Roots for UTE-0/0.

Contains the 1000 primordial word roots of the Universal Dictionary 00.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class UniversalRoot:
    """
    Represents a primordial word root.

    Attributes:
        root_id: Unique identifier (1-1000)
        root: The primordial root form
        meaning: Core meaning
        phonetic_class: Phonetic classification
        semantic_field: Semantic category
        related_languages: Languages with cognates
    """

    root_id: int
    root: str
    meaning: str
    phonetic_class: str
    semantic_field: str
    related_languages: List[str]


class UniversalRoots:
    """
    The Universal Dictionary 00 containing 1000 primordial roots.

    This implements Phase 2 of the UTE-0/0 pipeline.
    Roots are organized by:
    - Phonetic similarity
    - Symbolic similarity
    - Cosmological similarity
    """

    # Initial set of primordial roots (representative sample)
    # Full dictionary would contain 1000 roots
    ROOTS: Dict[int, UniversalRoot] = {
        # Water/Liquid roots
        1: UniversalRoot(
            1,
            "*akw",
            "water",
            "guttural-labial",
            "element",
            ["Sanskrit", "Latin", "Greek", "Germanic"],
        ),
        2: UniversalRoot(
            2,
            "*mar",
            "sea/large body of water",
            "nasal-liquid",
            "element",
            ["Latin", "Celtic", "Semitic"],
        ),
        3: UniversalRoot(
            3,
            "*nebh",
            "cloud/moisture",
            "nasal-labial",
            "element",
            ["Sanskrit", "Greek", "Latin", "Slavic"],
        ),
        # Fire/Heat roots
        10: UniversalRoot(
            10,
            "*egni",
            "fire",
            "guttural-nasal",
            "element",
            ["Sanskrit", "Latin", "Slavic", "Baltic"],
        ),
        11: UniversalRoot(
            11,
            "*bhel",
            "shine/burn",
            "labial-liquid",
            "element",
            ["Greek", "Latin", "Germanic", "Baltic"],
        ),
        12: UniversalRoot(
            12,
            "*gwher",
            "heat/warm",
            "labial-liquid",
            "element",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        # Earth/Ground roots
        20: UniversalRoot(
            20,
            "*dhghem",
            "earth/ground",
            "dental-guttural",
            "element",
            ["Sanskrit", "Greek", "Latin", "Slavic"],
        ),
        21: UniversalRoot(
            21,
            "*ters",
            "dry/solid",
            "dental-sibilant",
            "element",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        # Air/Wind roots
        30: UniversalRoot(
            30,
            "*anH",
            "breathe/spirit",
            "vowel-nasal",
            "element",
            ["Sanskrit", "Greek", "Latin", "Celtic"],
        ),
        31: UniversalRoot(
            31,
            "*weH",
            "blow/wind",
            "labial-vowel",
            "element",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        # Life/Nature roots
        40: UniversalRoot(
            40,
            "*gwiH",
            "live",
            "labial-vowel",
            "life",
            ["Sanskrit", "Greek", "Latin", "Slavic"],
        ),
        41: UniversalRoot(
            41,
            "*mer",
            "die/death",
            "nasal-liquid",
            "life",
            ["Sanskrit", "Greek", "Latin", "Slavic"],
        ),
        42: UniversalRoot(
            42,
            "*genH",
            "beget/born",
            "guttural-nasal",
            "life",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        # Body parts
        50: UniversalRoot(
            50,
            "*kerd",
            "heart",
            "guttural-dental",
            "body",
            ["Sanskrit", "Greek", "Latin", "Slavic", "Germanic"],
        ),
        51: UniversalRoot(
            51,
            "*okw",
            "eye/see",
            "vowel-guttural",
            "body",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        52: UniversalRoot(
            52,
            "*ped",
            "foot",
            "labial-dental",
            "body",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        53: UniversalRoot(
            53,
            "*man",
            "hand",
            "nasal-nasal",
            "body",
            ["Sanskrit", "Latin", "Germanic"],
        ),
        # Family/Social roots
        60: UniversalRoot(
            60,
            "*mater",
            "mother",
            "nasal-dental",
            "family",
            ["Sanskrit", "Greek", "Latin", "Slavic", "Germanic"],
        ),
        61: UniversalRoot(
            61,
            "*pater",
            "father",
            "labial-dental",
            "family",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        62: UniversalRoot(
            62,
            "*bhrater",
            "brother",
            "labial-dental",
            "family",
            ["Sanskrit", "Greek", "Latin", "Slavic", "Germanic"],
        ),
        63: UniversalRoot(
            63,
            "*swesor",
            "sister",
            "sibilant-liquid",
            "family",
            ["Sanskrit", "Greek", "Latin", "Slavic", "Germanic"],
        ),
        # Numbers
        70: UniversalRoot(
            70,
            "*oynos",
            "one",
            "vowel-nasal",
            "number",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        71: UniversalRoot(
            71,
            "*dwoh",
            "two",
            "dental-labial",
            "number",
            ["Sanskrit", "Greek", "Latin", "Germanic", "Slavic"],
        ),
        72: UniversalRoot(
            72,
            "*treyes",
            "three",
            "dental-liquid",
            "number",
            ["Sanskrit", "Greek", "Latin", "Germanic", "Slavic"],
        ),
        # Celestial roots
        80: UniversalRoot(
            80,
            "*dyew",
            "sky/god/shine",
            "dental-labial",
            "celestial",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        81: UniversalRoot(
            81,
            "*mehns",
            "moon/month",
            "nasal-sibilant",
            "celestial",
            ["Sanskrit", "Greek", "Latin", "Germanic", "Slavic"],
        ),
        82: UniversalRoot(
            82,
            "*Hster",
            "star",
            "sibilant-dental",
            "celestial",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        # Action roots
        90: UniversalRoot(
            90,
            "*steh",
            "stand",
            "sibilant-dental",
            "action",
            ["Sanskrit", "Greek", "Latin", "Germanic", "Slavic"],
        ),
        91: UniversalRoot(
            91,
            "*sed",
            "sit",
            "sibilant-dental",
            "action",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        92: UniversalRoot(
            92,
            "*gwebh",
            "go/walk",
            "guttural-labial",
            "action",
            ["Sanskrit", "Greek", "Germanic"],
        ),
        93: UniversalRoot(
            93,
            "*bher",
            "carry/bear",
            "labial-liquid",
            "action",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        # Cognitive roots
        100: UniversalRoot(
            100,
            "*weid",
            "see/know",
            "labial-dental",
            "cognitive",
            ["Sanskrit", "Greek", "Latin", "Germanic", "Slavic"],
        ),
        101: UniversalRoot(
            101,
            "*gnoh",
            "know",
            "guttural-nasal",
            "cognitive",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
        102: UniversalRoot(
            102,
            "*men",
            "think/mind",
            "nasal-nasal",
            "cognitive",
            ["Sanskrit", "Greek", "Latin", "Germanic"],
        ),
    }

    def __init__(self):
        """Initialize the Universal Roots dictionary."""
        self._by_meaning: Dict[str, UniversalRoot] = {
            root.meaning: root for root in self.ROOTS.values()
        }
        self._by_field: Dict[str, List[UniversalRoot]] = {}
        for root in self.ROOTS.values():
            if root.semantic_field not in self._by_field:
                self._by_field[root.semantic_field] = []
            self._by_field[root.semantic_field].append(root)

    def get_root(self, root_id: int) -> UniversalRoot | None:
        """
        Get a root by its ID.

        Args:
            root_id: Root identifier (1-1000)

        Returns:
            UniversalRoot if found, None otherwise
        """
        return self.ROOTS.get(root_id)

    def get_root_by_meaning(self, meaning: str) -> UniversalRoot | None:
        """
        Get a root by its meaning.

        Args:
            meaning: Core meaning to search

        Returns:
            UniversalRoot if found, None otherwise
        """
        return self._by_meaning.get(meaning)

    def get_roots_by_field(self, field: str) -> List[UniversalRoot]:
        """
        Get all roots in a semantic field.

        Args:
            field: Semantic field name

        Returns:
            List of roots in the field
        """
        return self._by_field.get(field, [])

    def get_all_fields(self) -> List[str]:
        """
        Get all semantic field names.

        Returns:
            List of field names
        """
        return list(self._by_field.keys())

    def search_by_phonetic_class(self, phonetic_class: str) -> List[UniversalRoot]:
        """
        Search roots by phonetic class.

        Args:
            phonetic_class: Phonetic classification to search

        Returns:
            List of matching roots
        """
        return [
            root
            for root in self.ROOTS.values()
            if root.phonetic_class == phonetic_class
        ]

    def search_by_language(self, language: str) -> List[UniversalRoot]:
        """
        Search roots that have cognates in a language.

        Args:
            language: Language name

        Returns:
            List of roots with cognates in the language
        """
        return [
            root for root in self.ROOTS.values() if language in root.related_languages
        ]

    @property
    def total_roots(self) -> int:
        """Return total number of roots in the dictionary."""
        return len(self.ROOTS)
