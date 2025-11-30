"""
Harappan Mapper for UTE-0/0.

Maps text and phonemes to Harappan sign equivalents.
"""

from dataclasses import dataclass
# Modern Python typing (3.10+)

from ute00.harappan.signs import HarappanSign, HarappanSignSystem


@dataclass
class HarappanMapping:
    """Result of mapping text to Harappan signs."""

    original: str
    signs: list[HarappanSign]
    total_numeric_value: int
    dynamics: list[str]


class HarappanMapper:
    """
    Maps phonemes and concepts to Harappan signs.

    This implements Phase 3 of the UTE-0/0 pipeline.
    """

    # Phoneme to sign category mappings
    PHONEME_CATEGORY_MAP: dict[str, str] = {
        # Vowels map to elemental/abstract
        "a": "elemental",
        "e": "elemental",
        "i": "directional",
        "o": "geometric",
        "u": "container",
        # Consonants map to various categories
        "b": "zoomorphic",
        "c": "geometric",
        "d": "directional",
        "f": "elemental",
        "g": "botanical",
        "h": "anthropomorphic",
        "j": "zoomorphic",
        "k": "geometric",
        "l": "directional",
        "m": "anthropomorphic",
        "n": "numerical",
        "p": "botanical",
        "q": "compound",
        "r": "directional",
        "s": "elemental",
        "t": "geometric",
        "v": "zoomorphic",
        "w": "elemental",
        "x": "compound",
        "y": "directional",
        "z": "geometric",
    }

    def __init__(self):
        """Initialize the Harappan mapper."""
        self.sign_system = HarappanSignSystem()

    def map_text(self, text: str) -> HarappanMapping:
        """
        Map text to Harappan signs.

        Args:
            text: Input text to map

        Returns:
            HarappanMapping with matched signs
        """
        signs = []
        dynamics = []

        for char in text.lower():
            if char.isalpha():
                category = self.PHONEME_CATEGORY_MAP.get(char, "geometric")
                category_signs = self.sign_system.get_signs_by_category(category)
                if category_signs:
                    # Select first sign from category (could be more sophisticated)
                    sign = category_signs[0]
                    signs.append(sign)
                    dynamics.append(sign.dynamics)

        total_value = sum(s.numeric_value for s in signs)

        return HarappanMapping(
            original=text,
            signs=signs,
            total_numeric_value=total_value,
            dynamics=dynamics,
        )

    def map_phoneme(self, phoneme: str) -> HarappanSign | None:
        """
        Map a single phoneme to a Harappan sign.

        Args:
            phoneme: Single phoneme character

        Returns:
            HarappanSign if mapping exists, None otherwise
        """
        category = self.PHONEME_CATEGORY_MAP.get(phoneme.lower())
        if category:
            signs = self.sign_system.get_signs_by_category(category)
            return signs[0] if signs else None
        return None

    def get_sign_sequence(self, text: str) -> list[str]:
        """
        Get the symbol sequence for text.

        Args:
            text: Input text

        Returns:
            List of Harappan symbol characters
        """
        mapping = self.map_text(text)
        return [sign.symbol for sign in mapping.signs]
