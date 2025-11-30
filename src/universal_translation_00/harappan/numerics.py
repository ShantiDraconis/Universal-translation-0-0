"""
Harappan Numerics for Universal Translation 0/0.

Numerical and mathematical interpretations of Harappan signs
based on their group and phonetic values.
"""

from typing import Optional

from universal_translation_00.harappan.mapping import HarappanSign


class HarappanNumerics:
    """
    Provides numerical interpretations of Harappan signs.

    Includes:
    - Base numerical values
    - Pythagorean values
    - Kabbalistic gematria
    - Position values
    """

    # Phoneme to Pythagorean number (1-9 cycle)
    PYTHAGOREAN_MAP: dict[str, int] = {
        "a": 1, "i": 9, "u": 3, "e": 5, "o": 6,
        "ka": 2, "ki": 2, "ku": 2, "ko": 2,
        "ga": 3, "gi": 3, "gu": 3, "go": 3,
        "ta": 2, "ti": 2, "tu": 2, "to": 2,
        "da": 4, "di": 4, "du": 4, "do": 4,
        "na": 5, "ni": 5, "nu": 5, "no": 5,
        "pa": 7, "pi": 7, "pu": 7, "po": 7,
        "ma": 4, "mi": 4, "mu": 4, "mo": 4,
        "ya": 1, "yi": 1, "yu": 1, "yo": 1,
        "ra": 9, "ri": 9, "ru": 9, "ro": 9,
        "la": 3, "li": 3, "lu": 3, "lo": 3,
        "wa": 5, "wi": 5, "wu": 5, "wo": 5,
        "sa": 1, "si": 1, "su": 1, "so": 1,
        "ha": 8, "hi": 8, "hu": 8, "ho": 8,
    }

    # Group numeric base values
    GROUP_BASE: dict[str, int] = {
        "NUM": 1,
        "CON": 40,
        "GRID": 80,
        "CHEV": 110,
        "CIRC": 130,
        "OPER": 150,
        "HUM": 190,
        "ANIM": 230,
        "PLANT": 260,
        "ABSTR": 290,
        "RIT": 320,
        "ARCH": 360,
        "MISC": 390,
    }

    def __init__(self) -> None:
        """Initialize the numerics calculator."""
        pass

    def get_sign_number(self, sign: HarappanSign) -> int:
        """
        Get the numeric value from sign ID.

        Args:
            sign: The Harappan sign

        Returns:
            Numeric value (1-417)
        """
        return int(sign.id[1:])

    def get_pythagorean_value(self, sign: HarappanSign) -> int:
        """
        Get Pythagorean numerological value.

        Args:
            sign: The Harappan sign

        Returns:
            Pythagorean value (1-9)
        """
        # Get base from phoneme
        base = self.PYTHAGOREAN_MAP.get(sign.phoneme, 0)
        if base == 0:
            # Calculate from sign number
            num = self.get_sign_number(sign)
            base = self._reduce_to_single(num)
        return base

    def _reduce_to_single(self, num: int) -> int:
        """Reduce number to single digit (1-9)."""
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num if num > 0 else 9

    def get_gematria_value(self, sign: HarappanSign) -> int:
        """
        Get kabbalistic gematria value.

        Maps phonemes to Hebrew letter values.

        Args:
            sign: The Harappan sign

        Returns:
            Gematria value
        """
        # Hebrew letter value mapping (simplified)
        gematria: dict[str, int] = {
            "a": 1, "b": 2, "g": 3, "d": 4, "h": 5,
            "w": 6, "z": 7, "ch": 8, "t": 9, "y": 10,
            "k": 20, "l": 30, "m": 40, "n": 50, "s": 60,
            "p": 80, "ts": 90, "q": 100, "r": 200, "sh": 300,
        }

        phoneme = sign.phoneme.lower()
        value = 0

        for char in phoneme:
            value += gematria.get(char, 0)

        return value if value > 0 else self.get_sign_number(sign)

    def get_position_in_group(self, sign: HarappanSign) -> int:
        """
        Get position within semantic group.

        Args:
            sign: The Harappan sign

        Returns:
            Position index (1-based)
        """
        base = self.GROUP_BASE.get(sign.group, 0)
        num = self.get_sign_number(sign)
        return num - base

    def get_cosmic_number(self, sign: HarappanSign) -> dict:
        """
        Get comprehensive cosmic numerology.

        Args:
            sign: The Harappan sign

        Returns:
            Dictionary with all numeric values
        """
        num = self.get_sign_number(sign)
        return {
            "sign_number": num,
            "pythagorean": self.get_pythagorean_value(sign),
            "gematria": self.get_gematria_value(sign),
            "position": self.get_position_in_group(sign),
            "reduced": self._reduce_to_single(num),
            "group_base": self.GROUP_BASE.get(sign.group, 0),
        }

    def calculate_sequence_value(self, signs: list[HarappanSign]) -> dict:
        """
        Calculate numeric values for a sequence of signs.

        Args:
            signs: List of Harappan signs

        Returns:
            Dictionary with sequence numerology
        """
        total = sum(self.get_sign_number(s) for s in signs)
        pythagorean = sum(self.get_pythagorean_value(s) for s in signs)

        return {
            "total": total,
            "pythagorean_sum": pythagorean,
            "pythagorean_reduced": self._reduce_to_single(pythagorean),
            "count": len(signs),
            "average": total / len(signs) if signs else 0,
        }
