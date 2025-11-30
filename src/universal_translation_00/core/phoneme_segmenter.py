"""
Phoneme Segmenter for Universal Translation 0/0.

Segments tokens into phonemes based on script-specific rules
and universal phonetic patterns.
"""

import re
from dataclasses import dataclass


@dataclass
class Phoneme:
    """Represents a phoneme extracted from text."""

    value: str
    position: int
    source_text: str
    phoneme_class: str  # 'vowel', 'consonant', 'syllable'

    def __repr__(self) -> str:
        return f"Phoneme({self.value!r}, class={self.phoneme_class})"


class PhonemeSegmenter:
    """
    Segments text into phonemes using universal phonetic patterns.

    This segmenter recognizes common phoneme patterns across
    multiple language families, optimized for the Universal
    Translation 0/0 system.
    """

    # Universal vowels
    VOWELS = set("aeiouāēīōūàèìòùáéíóúâêîôûäëïöü")

    # Universal consonants
    CONSONANTS = set("bcdfghjklmnpqrstvwxyzṭṇḍḷṛśṣñṅŋçğ")

    # Common CV syllable patterns (Consonant + Vowel)
    CV_PATTERNS: list[tuple[str, str]] = [
        # CVC patterns (ritual/architectural)
        (r"(tak|sak|ram|lam|kam|han|yum|kum)", "cvc_ritual"),
        (r"(kal|kul|kar|tor|dom|mur)", "cvc_arch"),
        # CVV patterns (human/extended)
        (r"(ama|ani|anu|ima|ina|inu)", "cvv_human"),
        # CV patterns (basic syllables)
        (r"([kgtdpbmnrlsywh][aeiou])", "cv_basic"),
        (r"(ka|ki|ku|ke|ko)", "cv_k"),
        (r"(ga|gi|gu|ge|go)", "cv_g"),
        (r"(ta|ti|tu|te|to)", "cv_t"),
        (r"(da|di|du|de|do)", "cv_d"),
        (r"(pa|pi|pu|pe|po)", "cv_p"),
        (r"(ba|bi|bu|be|bo)", "cv_b"),
        (r"(ma|mi|mu|me|mo)", "cv_m"),
        (r"(na|ni|nu|ne|no)", "cv_n"),
        (r"(ra|ri|ru|re|ro)", "cv_r"),
        (r"(la|li|lu|le|lo)", "cv_l"),
        (r"(sa|si|su|se|so)", "cv_s"),
        (r"(ya|yi|yu|ye|yo)", "cv_y"),
        (r"(wa|wi|wu|we|wo)", "cv_w"),
        (r"(ha|hi|hu|he|ho)", "cv_h"),
        # Single vowels
        (r"([aeiou])", "vowel"),
    ]

    def __init__(self) -> None:
        """Initialize the phoneme segmenter."""
        # Compile patterns for efficiency
        self._compiled_patterns: list[tuple[re.Pattern[str], str]] = [
            (re.compile(pattern, re.IGNORECASE), name)
            for pattern, name in self.CV_PATTERNS
        ]

    def is_vowel(self, char: str) -> bool:
        """Check if a character is a vowel."""
        return char.lower() in self.VOWELS

    def is_consonant(self, char: str) -> bool:
        """Check if a character is a consonant."""
        return char.lower() in self.CONSONANTS

    def segment(self, text: str) -> list[Phoneme]:
        """
        Segment text into phonemes.

        Args:
            text: The input text to segment

        Returns:
            List of Phoneme objects
        """
        text = text.lower()
        phonemes: list[Phoneme] = []
        position = 0

        while position < len(text):
            matched = False
            remaining = text[position:]

            # Try each pattern from longest to shortest
            for pattern, phoneme_class in self._compiled_patterns:
                match = pattern.match(remaining)
                if match:
                    phoneme_value = match.group(1) if match.lastindex else match.group()
                    phonemes.append(
                        Phoneme(
                            value=phoneme_value,
                            position=position,
                            source_text=match.group(),
                            phoneme_class=phoneme_class,
                        )
                    )
                    position += len(match.group())
                    matched = True
                    break

            if not matched:
                # Handle single characters that don't match patterns
                char = text[position]
                if char.isalpha():
                    p_class = "vowel" if self.is_vowel(char) else "consonant"
                    phonemes.append(
                        Phoneme(
                            value=char,
                            position=position,
                            source_text=char,
                            phoneme_class=p_class,
                        )
                    )
                position += 1

        return phonemes

    def get_syllables(self, text: str) -> list[str]:
        """
        Get syllable-level phonemes from text.

        Args:
            text: The input text

        Returns:
            List of syllable strings
        """
        phonemes = self.segment(text)
        return [p.value for p in phonemes if "cv" in p.phoneme_class or p.phoneme_class == "vowel"]

    def count_phonemes(self, text: str) -> dict[str, int]:
        """
        Count occurrences of each phoneme in text.

        Args:
            text: The input text

        Returns:
            Dictionary mapping phoneme to count
        """
        phonemes = self.segment(text)
        counts: dict[str, int] = {}
        for p in phonemes:
            counts[p.value] = counts.get(p.value, 0) + 1
        return counts
