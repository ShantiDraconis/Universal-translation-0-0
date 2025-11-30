"""
Linguistic Family System for UTE-0/0.

Defines the 12 linguistic families used in Phase 4.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class LinguisticFamily:
    """
    Represents a linguistic family.

    Attributes:
        name: Family name
        languages: List of member languages
        region: Geographic region
        characteristics: Key phonetic/grammatical characteristics
        sample_words: Sample words showing common roots
    """

    name: str
    languages: List[str]
    region: str
    characteristics: List[str]
    sample_words: Dict[str, str]


class LinguisticFamilySystem:
    """
    The 12 Linguistic Family System for UTE-0/0.

    Implements Phase 4 of the pipeline.
    """

    FAMILIES: Dict[str, LinguisticFamily] = {
        "tupi": LinguisticFamily(
            name="Tupi",
            languages=["Tupinambá", "Guarani", "Nheengatu", "Tupi Antigo"],
            region="South America (Brazil, Paraguay, Argentina)",
            characteristics=[
                "Agglutinative",
                "Nasal vowels",
                "Verb-initial tendency",
                "Extensive prefix system",
            ],
            sample_words={
                "water": "y",
                "mother": "sy",
                "sun": "kuarahy",
                "fire": "tata",
                "earth": "yvy",
            },
        ),
        "dravidian": LinguisticFamily(
            name="Dravidian",
            languages=["Tamil", "Telugu", "Kannada", "Malayalam"],
            region="South India, Sri Lanka",
            characteristics=[
                "Agglutinative",
                "Retroflex consonants",
                "SOV word order",
                "Inclusive/exclusive pronouns",
            ],
            sample_words={
                "water": "nīr",
                "mother": "amma",
                "sun": "cūriyan",
                "fire": "tī",
                "earth": "nilam",
            },
        ),
        "sanskrit": LinguisticFamily(
            name="Indo-Aryan (Sanskrit)",
            languages=["Sanskrit", "Hindi", "Bengali", "Marathi"],
            region="South Asia",
            characteristics=[
                "Highly inflected",
                "Rich case system",
                "Devanagari script",
                "SOV word order",
            ],
            sample_words={
                "water": "jala",
                "mother": "mātṛ",
                "sun": "sūrya",
                "fire": "agni",
                "earth": "pṛthvī",
            },
        ),
        "hebrew": LinguisticFamily(
            name="Semitic (Hebrew)",
            languages=["Hebrew", "Arabic", "Aramaic", "Amharic"],
            region="Middle East, North Africa",
            characteristics=[
                "Root-pattern morphology",
                "Triliteral roots",
                "Right-to-left script",
                "VSO tendency",
            ],
            sample_words={
                "water": "mayim",
                "mother": "em",
                "sun": "shemesh",
                "fire": "esh",
                "earth": "eretz",
            },
        ),
        "quechua": LinguisticFamily(
            name="Quechuan",
            languages=["Quechua", "Runasimi"],
            region="Andes (Peru, Bolivia, Ecuador)",
            characteristics=[
                "Agglutinative",
                "Evidential markers",
                "SOV word order",
                "No grammatical gender",
            ],
            sample_words={
                "water": "yaku",
                "mother": "mama",
                "sun": "inti",
                "fire": "nina",
                "earth": "pacha",
            },
        ),
        "yoruba": LinguisticFamily(
            name="Niger-Congo (Yoruba)",
            languages=["Yoruba", "Igbo", "Akan", "Zulu"],
            region="West and Central Africa",
            characteristics=[
                "Tonal",
                "Noun class system",
                "Serial verb constructions",
                "Subject-Verb-Object",
            ],
            sample_words={
                "water": "omi",
                "mother": "ìyá",
                "sun": "òrùn",
                "fire": "iná",
                "earth": "ilẹ̀",
            },
        ),
        "bantu": LinguisticFamily(
            name="Bantu",
            languages=["Swahili", "Zulu", "Shona", "Lingala"],
            region="Sub-Saharan Africa",
            characteristics=[
                "Noun class prefixes",
                "Agglutinative verbs",
                "Tonal",
                "Subject-Verb-Object",
            ],
            sample_words={
                "water": "maji",
                "mother": "mama",
                "sun": "jua",
                "fire": "moto",
                "earth": "ardhi",
            },
        ),
        "sumerian": LinguisticFamily(
            name="Sumerian (Language Isolate)",
            languages=["Sumerian"],
            region="Ancient Mesopotamia",
            characteristics=[
                "Agglutinative",
                "Split ergative",
                "Cuneiform script",
                "SOV word order",
            ],
            sample_words={
                "water": "a",
                "mother": "ama",
                "sun": "utu",
                "fire": "izi",
                "earth": "ki",
            },
        ),
        "indo_european": LinguisticFamily(
            name="Indo-European",
            languages=["Greek", "Latin", "Germanic", "Celtic", "Slavic"],
            region="Europe, West/South Asia",
            characteristics=[
                "Highly inflected",
                "Case systems",
                "Grammatical gender",
                "Various word orders",
            ],
            sample_words={
                "water": "*wódr",
                "mother": "*méh₂tēr",
                "sun": "*sóh₂wl",
                "fire": "*péh₂wr",
                "earth": "*dʰéǵʰōm",
            },
        ),
        "arabic": LinguisticFamily(
            name="Arabic",
            languages=["Classical Arabic", "Modern Standard Arabic", "Gulf Arabic"],
            region="Middle East, North Africa",
            characteristics=[
                "Root-pattern morphology",
                "Triliteral roots",
                "VSO word order",
                "Complex verbal system",
            ],
            sample_words={
                "water": "māʾ",
                "mother": "umm",
                "sun": "shams",
                "fire": "nār",
                "earth": "arḍ",
            },
        ),
        "chinese": LinguisticFamily(
            name="Sino-Tibetan (Chinese)",
            languages=["Mandarin", "Cantonese", "Wu", "Min"],
            region="East Asia",
            characteristics=[
                "Tonal",
                "Isolating",
                "Logographic script",
                "Topic-prominent",
            ],
            sample_words={
                "water": "shuǐ",
                "mother": "mǔ",
                "sun": "rì/tàiyáng",
                "fire": "huǒ",
                "earth": "tǔ/dì",
            },
        ),
        "japanese": LinguisticFamily(
            name="Japonic",
            languages=["Japanese", "Ryukyuan"],
            region="Japan, Ryukyu Islands",
            characteristics=[
                "Agglutinative",
                "SOV word order",
                "Pitch accent",
                "Complex honorific system",
            ],
            sample_words={
                "water": "mizu",
                "mother": "haha",
                "sun": "hi/taiyō",
                "fire": "hi",
                "earth": "tsuchi",
            },
        ),
    }

    def __init__(self):
        """Initialize the linguistic family system."""
        pass

    def get_family(self, name: str) -> LinguisticFamily | None:
        """
        Get a linguistic family by name.

        Args:
            name: Family name (lowercase)

        Returns:
            LinguisticFamily if found, None otherwise
        """
        return self.FAMILIES.get(name.lower())

    def get_all_families(self) -> List[LinguisticFamily]:
        """
        Get all linguistic families.

        Returns:
            List of all families
        """
        return list(self.FAMILIES.values())

    def find_cognates(self, word: str, meaning: str) -> Dict[str, str]:
        """
        Find cognates for a concept across families.

        Args:
            word: Reference word
            meaning: Word meaning (water, mother, sun, fire, earth)

        Returns:
            Dictionary of family -> word
        """
        cognates = {}
        for name, family in self.FAMILIES.items():
            if meaning in family.sample_words:
                cognates[name] = family.sample_words[meaning]
        return cognates

    def get_families_by_region(self, region_keyword: str) -> List[LinguisticFamily]:
        """
        Get families by geographic region.

        Args:
            region_keyword: Keyword to search in region

        Returns:
            List of matching families
        """
        return [
            f for f in self.FAMILIES.values() if region_keyword.lower() in f.region.lower()
        ]

    def get_families_by_characteristic(
        self, characteristic: str
    ) -> List[LinguisticFamily]:
        """
        Get families sharing a linguistic characteristic.

        Args:
            characteristic: Characteristic to search

        Returns:
            List of matching families
        """
        return [
            f
            for f in self.FAMILIES.values()
            if any(characteristic.lower() in c.lower() for c in f.characteristics)
        ]
