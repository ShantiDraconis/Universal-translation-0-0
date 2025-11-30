"""
Phonetic Analyzer for UTE-0/0.

Provides phonetic analysis and phoneme-to-number mapping.
"""

from dataclasses import dataclass


@dataclass
class PhonemeMapping:
    """
    Represents a phoneme mapping with real, imaginary, and structural components.

    Φ(f) = (n_r, n_i, n_s)

    Where:
    - n_r = real component (phonetic frequency)
    - n_i = imaginary component (symbolism)
    - n_s = structural component (position in universal tree)
    """

    phoneme: str
    real: float  # n_r - phonetic frequency
    imaginary: float  # n_i - symbolism
    structural: float  # n_s - position in universal tree


class PhoneticAnalyzer:
    """
    Analyzes phonetic properties of text and maps phonemes to numerical values.

    The analyzer uses the universal phoneme mapping system defined by:
    Φ(f) = (n_r, n_i, n_s)
    """

    # Universal phoneme mappings (simplified initial set)
    PHONEME_MAPPINGS = {
        # Vowels
        "a": PhonemeMapping("a", 1.0, 0.5, 1),
        "e": PhonemeMapping("e", 2.0, 0.6, 2),
        "i": PhonemeMapping("i", 3.0, 0.7, 3),
        "o": PhonemeMapping("o", 4.0, 0.8, 4),
        "u": PhonemeMapping("u", 5.0, 0.9, 5),
        # Consonants (basic set)
        "b": PhonemeMapping("b", 6.0, 0.1, 6),
        "c": PhonemeMapping("c", 7.0, 0.2, 7),
        "d": PhonemeMapping("d", 8.0, 0.3, 8),
        "f": PhonemeMapping("f", 9.0, 0.4, 9),
        "g": PhonemeMapping("g", 10.0, 0.5, 10),
        "h": PhonemeMapping("h", 11.0, 0.6, 11),
        "j": PhonemeMapping("j", 12.0, 0.7, 12),
        "k": PhonemeMapping("k", 13.0, 0.8, 13),
        "l": PhonemeMapping("l", 14.0, 0.9, 14),
        "m": PhonemeMapping("m", 15.0, 1.0, 15),
        "n": PhonemeMapping("n", 16.0, 0.1, 16),
        "p": PhonemeMapping("p", 17.0, 0.2, 17),
        "q": PhonemeMapping("q", 18.0, 0.3, 18),
        "r": PhonemeMapping("r", 19.0, 0.4, 19),
        "s": PhonemeMapping("s", 20.0, 0.5, 20),
        "t": PhonemeMapping("t", 21.0, 0.6, 21),
        "v": PhonemeMapping("v", 22.0, 0.7, 22),
        "w": PhonemeMapping("w", 23.0, 0.8, 23),
        "x": PhonemeMapping("x", 24.0, 0.9, 24),
        "y": PhonemeMapping("y", 25.0, 1.0, 25),
        "z": PhonemeMapping("z", 26.0, 0.1, 26),
    }

    def __init__(self):
        """Initialize the PhoneticAnalyzer."""
        self._cache: dict = {}

    def analyze(self, text: str) -> list[PhonemeMapping]:
        """
        Analyze text and return phoneme mappings.

        Args:
            text: Input text to analyze

        Returns:
            List of PhonemeMapping objects for each phoneme in the text
        """
        mappings = []
        for char in text.lower():
            if char in self.PHONEME_MAPPINGS:
                mappings.append(self.PHONEME_MAPPINGS[char])
        return mappings

    def get_phoneme_mapping(self, phoneme: str) -> PhonemeMapping | None:
        """
        Get the mapping for a specific phoneme.

        Args:
            phoneme: Single phoneme character

        Returns:
            PhonemeMapping if found, None otherwise
        """
        return self.PHONEME_MAPPINGS.get(phoneme.lower())

    def calculate_phi(self, phoneme: str) -> tuple[float, float, float] | None:
        """
        Calculate the Φ(f) = (n_r, n_i, n_s) for a phoneme.

        Args:
            phoneme: Single phoneme character

        Returns:
            Tuple of (real, imaginary, structural) if found, None otherwise
        """
        mapping = self.get_phoneme_mapping(phoneme)
        if mapping:
            return (mapping.real, mapping.imaginary, mapping.structural)
        return None

    def get_total_vibration(self, text: str) -> float:
        """
        Calculate the total vibrational value of text.

        This sums the real components of all phoneme mappings.

        Args:
            text: Input text

        Returns:
            Total vibrational value
        """
        mappings = self.analyze(text)
        return sum(m.real for m in mappings)
