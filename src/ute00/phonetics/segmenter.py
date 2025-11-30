"""
Phonetic Segmenter for UTE-0/0.

Provides segmentation and mirroring functionality for phonetic analysis.
"""

from dataclasses import dataclass
# Modern Python typing (3.10+)


@dataclass
class SegmentationResult:
    """Result of phonetic segmentation."""

    original: str
    horizontal_inversion: str
    vertical_inversion: str
    syllables: list[str]
    phonemes: list[str]
    nuclear_vowels: list[str]


class PhoneticSegmenter:
    """
    Segments text into phonetic components with Da Vinci-style inversions.

    Phase 1 of the UTE-0/0 pipeline:
    - Horizontal inversion
    - Vertical inversion
    - Syllable → phoneme → nuclear vowel
    """

    # Basic vowels for nuclear identification
    VOWELS = set("aeiouáéíóúàèìòùâêîôûäëïöü")

    # Vertical mirroring map (approximate visual flip)
    VERTICAL_MIRROR = {
        "a": "ɐ",
        "b": "q",
        "c": "ɔ",
        "d": "p",
        "e": "ə",
        "f": "ɟ",
        "g": "ƃ",
        "h": "ɥ",
        "i": "ı",
        "j": "ɾ",
        "k": "ʞ",
        "l": "l",
        "m": "ɯ",
        "n": "u",
        "o": "o",
        "p": "d",
        "q": "b",
        "r": "ɹ",
        "s": "s",
        "t": "ʇ",
        "u": "n",
        "v": "ʌ",
        "w": "ʍ",
        "x": "x",
        "y": "ʎ",
        "z": "z",
    }

    def __init__(self):
        """Initialize the PhoneticSegmenter."""
        pass

    def segment(self, text: str) -> SegmentationResult:
        """
        Perform full segmentation on input text.

        Args:
            text: Input text to segment

        Returns:
            SegmentationResult with all segmentation components
        """
        return SegmentationResult(
            original=text,
            horizontal_inversion=self.horizontal_inversion(text),
            vertical_inversion=self.vertical_inversion(text),
            syllables=self.syllabify(text),
            phonemes=self.extract_phonemes(text),
            nuclear_vowels=self.extract_nuclear_vowels(text),
        )

    def horizontal_inversion(self, text: str) -> str:
        """
        Perform horizontal inversion (Da Vinci reading).

        Simply reverses the string.

        Args:
            text: Input text

        Returns:
            Horizontally inverted text
        """
        return text[::-1]

    def vertical_inversion(self, text: str) -> str:
        """
        Perform vertical inversion using character mapping.

        Args:
            text: Input text

        Returns:
            Vertically inverted text (characters flipped)
        """
        result = []
        for char in text.lower():
            result.append(self.VERTICAL_MIRROR.get(char, char))
        return "".join(result)

    def syllabify(self, text: str) -> list[str]:
        """
        Basic syllabification of text.

        Uses simple vowel-consonant patterns for syllable detection.

        Args:
            text: Input text

        Returns:
            List of syllables
        """
        syllables = []
        words = text.lower().split()

        for word in words:
            # Filter to only alphabetic characters
            word = "".join(c for c in word if c.isalpha())
            if not word:
                continue

            i = 0
            while i < len(word):
                chunk = ""
                # Get initial consonants
                while i < len(word) and word[i] not in self.VOWELS:
                    chunk += word[i]
                    i += 1
                # Get vowels
                while i < len(word) and word[i] in self.VOWELS:
                    chunk += word[i]
                    i += 1
                # Get trailing consonant if not followed by vowel
                if i < len(word) and word[i] not in self.VOWELS:
                    # Check if next char after this is a vowel
                    if i + 1 < len(word) and word[i + 1] in self.VOWELS:
                        # Don't include, starts next syllable
                        pass
                    else:
                        chunk += word[i]
                        i += 1
                if chunk:
                    syllables.append(chunk)

        return syllables if syllables else [text]

    def extract_phonemes(self, text: str) -> list[str]:
        """
        Extract individual phonemes from text.

        Args:
            text: Input text

        Returns:
            List of phonemes
        """
        return [char for char in text.lower() if char.isalpha()]

    def extract_nuclear_vowels(self, text: str) -> list[str]:
        """
        Extract nuclear vowels from text.

        Nuclear vowels are the core vowels of each syllable.

        Args:
            text: Input text

        Returns:
            List of nuclear vowels
        """
        return [char for char in text.lower() if char in self.VOWELS]
