"""
Text Normalizer for Universal Translation 0/0.

Normalizes text across different scripts and conventions
for consistent phonetic analysis.
"""

import re
import unicodedata
from typing import Optional


class Normalizer:
    """
    Normalizes text for consistent phonetic analysis.

    Handles:
    - Unicode normalization (NFC/NFD)
    - Case normalization
    - Diacritic handling
    - Script-specific normalizations
    """

    # Diacritic mapping for common romanizations
    DIACRITIC_MAP: dict[str, str] = {
        "ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u",
        "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u",
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "â": "a", "ê": "e", "î": "i", "ô": "o", "û": "u",
        "ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u",
        "ã": "a", "ñ": "n", "õ": "o",
        "ç": "c", "ş": "s", "ğ": "g",
        "ṭ": "t", "ḍ": "d", "ṇ": "n", "ḷ": "l", "ṛ": "r",
        "ś": "sh", "ṣ": "sh", "ṅ": "ng", "ŋ": "ng",
    }

    # Script-specific transliterations
    TAMIL_TRANSLIT: dict[str, str] = {
        "க": "ka", "ங": "nga", "ச": "ca", "ஞ": "nya",
        "ட": "ta", "ண": "na", "த": "tha", "ந": "na",
        "ப": "pa", "ம": "ma", "ய": "ya", "ர": "ra",
        "ல": "la", "வ": "va", "ழ": "zha", "ள": "la",
        "ற": "ra", "ன": "na",
        "அ": "a", "ஆ": "aa", "இ": "i", "ஈ": "ii",
        "உ": "u", "ஊ": "uu", "எ": "e", "ஏ": "ee",
        "ஐ": "ai", "ஒ": "o", "ஓ": "oo", "ஔ": "au",
    }

    DEVANAGARI_TRANSLIT: dict[str, str] = {
        "क": "ka", "ख": "kha", "ग": "ga", "घ": "gha", "ङ": "nga",
        "च": "ca", "छ": "cha", "ज": "ja", "झ": "jha", "ञ": "nya",
        "ट": "ta", "ठ": "tha", "ड": "da", "ढ": "dha", "ण": "na",
        "त": "ta", "थ": "tha", "द": "da", "ध": "dha", "न": "na",
        "प": "pa", "फ": "pha", "ब": "ba", "भ": "bha", "म": "ma",
        "य": "ya", "र": "ra", "ल": "la", "व": "va",
        "श": "sha", "ष": "sha", "स": "sa", "ह": "ha",
        "अ": "a", "आ": "aa", "इ": "i", "ई": "ii",
        "उ": "u", "ऊ": "uu", "ए": "e", "ऐ": "ai",
        "ओ": "o", "औ": "au",
    }

    def __init__(
        self,
        lowercase: bool = True,
        remove_diacritics: bool = False,
        transliterate: bool = True,
        unicode_form: str = "NFC",
    ) -> None:
        """
        Initialize the normalizer.

        Args:
            lowercase: Convert to lowercase
            remove_diacritics: Strip diacritical marks
            transliterate: Convert non-Latin scripts to Latin
            unicode_form: Unicode normalization form (NFC, NFD, NFKC, NFKD)
        """
        self.lowercase = lowercase
        self.remove_diacritics = remove_diacritics
        self.transliterate = transliterate
        self.unicode_form = unicode_form

    def normalize(self, text: str) -> str:
        """
        Apply all normalization steps to text.

        Args:
            text: The input text

        Returns:
            Normalized text
        """
        # Unicode normalization
        text = unicodedata.normalize(self.unicode_form, text)

        # Transliteration
        if self.transliterate:
            text = self._transliterate(text)

        # Lowercase
        if self.lowercase:
            text = text.lower()

        # Remove diacritics
        if self.remove_diacritics:
            text = self._remove_diacritics(text)

        # Clean whitespace
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def _transliterate(self, text: str) -> str:
        """Transliterate non-Latin scripts to Latin."""
        result: list[str] = []
        for char in text:
            if char in self.TAMIL_TRANSLIT:
                result.append(self.TAMIL_TRANSLIT[char])
            elif char in self.DEVANAGARI_TRANSLIT:
                result.append(self.DEVANAGARI_TRANSLIT[char])
            else:
                result.append(char)
        return "".join(result)

    def _remove_diacritics(self, text: str) -> str:
        """Remove diacritical marks from text."""
        result: list[str] = []
        for char in text:
            if char in self.DIACRITIC_MAP:
                result.append(self.DIACRITIC_MAP[char])
            else:
                # Use Unicode decomposition for remaining diacritics
                decomposed = unicodedata.normalize("NFD", char)
                base_char = "".join(
                    c for c in decomposed if unicodedata.category(c) != "Mn"
                )
                result.append(base_char if base_char else char)
        return "".join(result)

    def to_ascii(self, text: str, replacement: str = "") -> str:
        """
        Convert text to ASCII-only representation.

        Args:
            text: The input text
            replacement: Character to replace non-ASCII chars

        Returns:
            ASCII-only text
        """
        normalized = self.normalize(text)
        return "".join(
            c if ord(c) < 128 else replacement for c in normalized
        )

    def get_base_phoneme(self, phoneme: str) -> str:
        """
        Get the base form of a phoneme without length markers.

        Args:
            phoneme: The phoneme (e.g., 'aa', 'ii')

        Returns:
            Base phoneme (e.g., 'a', 'i')
        """
        # Handle long vowels
        if len(phoneme) == 2 and phoneme[0] == phoneme[1]:
            return phoneme[0]
        return phoneme
