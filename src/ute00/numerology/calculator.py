"""
Numerology Calculator for UTE-0/0.

Calculates numerical values using the four numerology systems.
"""

from dataclasses import dataclass
from typing import Dict, List

from ute00.numerology.systems import (
    NUMEROLOGY_SYSTEMS,
    NumerologySystem,
    NumerologyType,
)


@dataclass
class NumerologyResult:
    """Result of numerology calculation."""

    original: str
    pythagorean: int
    pythagorean_reduced: int
    kabbalistic: int
    kabbalistic_reduced: int
    astrological: int
    astrological_reduced: int
    mirrored: int
    mirrored_reduced: int
    master_number: int | None
    interpretation: str


class NumerologyCalculator:
    """
    Calculates numerical values using multiple systems.

    Implements Phase 6 of the UTE-0/0 pipeline.
    """

    # Master numbers (not reduced)
    MASTER_NUMBERS = {11, 22, 33, 44}

    # Number interpretations
    NUMBER_MEANINGS: Dict[int, str] = {
        1: "Unity, beginning, individuality, leadership",
        2: "Duality, partnership, balance, cooperation",
        3: "Creation, expression, synthesis, growth",
        4: "Foundation, stability, structure, order",
        5: "Change, freedom, adventure, dynamics",
        6: "Harmony, love, responsibility, nurture",
        7: "Wisdom, introspection, spirituality, analysis",
        8: "Power, abundance, manifestation, karma",
        9: "Completion, universal love, wisdom, endings",
        11: "Master number: Illumination, intuition, spiritual insight",
        22: "Master number: Master builder, large-scale achievement",
        33: "Master number: Master teacher, spiritual service",
        44: "Master number: Master healer, angelic realm",
    }

    def __init__(self):
        """Initialize the numerology calculator."""
        self.systems = NUMEROLOGY_SYSTEMS

    def calculate(self, text: str) -> NumerologyResult:
        """
        Calculate numerology values for text.

        Args:
            text: Text to analyze

        Returns:
            NumerologyResult with values from all systems
        """
        pythagorean = self._calculate_system(text, NumerologyType.PYTHAGOREAN)
        kabbalistic = self._calculate_system(text, NumerologyType.KABBALISTIC)
        astrological = self._calculate_system(text, NumerologyType.ASTROLOGICAL)
        mirrored = self._calculate_system(text, NumerologyType.MIRRORED)

        pythagorean_reduced = self._reduce(pythagorean)
        kabbalistic_reduced = self._reduce(kabbalistic)
        astrological_reduced = self._reduce(astrological)
        mirrored_reduced = self._reduce(mirrored)

        # Determine master number if any
        master = None
        for num in [pythagorean, kabbalistic, astrological, mirrored]:
            if num in self.MASTER_NUMBERS:
                master = num
                break

        # Generate interpretation
        interpretation = self._interpret(
            pythagorean_reduced, master, text  # Use primary system for interpretation
        )

        return NumerologyResult(
            original=text,
            pythagorean=pythagorean,
            pythagorean_reduced=pythagorean_reduced,
            kabbalistic=kabbalistic,
            kabbalistic_reduced=kabbalistic_reduced,
            astrological=astrological,
            astrological_reduced=astrological_reduced,
            mirrored=mirrored,
            mirrored_reduced=mirrored_reduced,
            master_number=master,
            interpretation=interpretation,
        )

    def _calculate_system(self, text: str, system_type: NumerologyType) -> int:
        """
        Calculate value using a specific system.

        Args:
            text: Text to calculate
            system_type: Numerology system to use

        Returns:
            Total numerical value
        """
        system = self.systems[system_type]
        total = 0

        for char in text.lower():
            if char in system.letter_values:
                total += system.letter_values[char]

        return total

    def _reduce(self, number: int) -> int:
        """
        Reduce a number to single digit (unless master number).

        Args:
            number: Number to reduce

        Returns:
            Reduced number
        """
        if number in self.MASTER_NUMBERS:
            return number

        while number > 9 and number not in self.MASTER_NUMBERS:
            number = sum(int(d) for d in str(number))

        return number

    def _interpret(self, reduced: int, master: int | None, text: str) -> str:
        """
        Generate interpretation of numerology result.

        Args:
            reduced: Reduced number
            master: Master number if detected
            text: Original text

        Returns:
            Interpretation string
        """
        if master:
            meaning = self.NUMBER_MEANINGS.get(master, "Unknown master number")
            return f"'{text}' resonates with {master}. {meaning}"
        else:
            meaning = self.NUMBER_MEANINGS.get(reduced, "Unknown vibration")
            return f"'{text}' reduces to {reduced}. {meaning}"

    def calculate_single_system(
        self, text: str, system_type: NumerologyType
    ) -> tuple[int, int]:
        """
        Calculate using a single system.

        Args:
            text: Text to calculate
            system_type: System to use

        Returns:
            Tuple of (total, reduced) values
        """
        total = self._calculate_system(text, system_type)
        reduced = self._reduce(total)
        return total, reduced

    def get_letter_values(
        self, text: str, system_type: NumerologyType
    ) -> List[tuple[str, int]]:
        """
        Get individual letter values.

        Args:
            text: Text to analyze
            system_type: System to use

        Returns:
            List of (letter, value) tuples
        """
        system = self.systems[system_type]
        return [(char, system.letter_values.get(char, 0)) for char in text.lower()]

    def compare_systems(self, text: str) -> Dict[str, tuple[int, int]]:
        """
        Compare results across all systems.

        Args:
            text: Text to analyze

        Returns:
            Dictionary of system_name -> (total, reduced) tuples
        """
        results = {}
        for system_type in NumerologyType:
            total = self._calculate_system(text, system_type)
            reduced = self._reduce(total)
            results[system_type.value] = (total, reduced)
        return results
