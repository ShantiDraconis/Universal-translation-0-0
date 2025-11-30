"""
Harappan Geometry for Universal Translation 0/0.

Geometric and cosmological interpretations of Harappan signs
based on their visual form and semantic group.
"""

from dataclasses import dataclass
from typing import Optional

from universal_translation_00.harappan.mapping import HarappanSign


@dataclass
class GeometricProperties:
    """Geometric properties of a Harappan sign."""

    shape_class: str  # 'linear', 'angular', 'circular', 'compound'
    symmetry: str  # 'vertical', 'horizontal', 'radial', 'none'
    complexity: int  # 1-5 scale
    element: str  # 'fire', 'water', 'earth', 'air', 'spirit'
    direction: str  # 'up', 'down', 'left', 'right', 'center'
    cosmic_zone: str  # 'celestial', 'terrestrial', 'chthonic'


class HarappanGeometry:
    """
    Provides geometric and cosmological analysis of Harappan signs.

    Based on the visual properties of sign groups and their
    relationship to universal symbolic patterns.
    """

    # Group to shape class mapping
    GROUP_SHAPES: dict[str, str] = {
        "NUM": "linear",
        "CON": "curved",
        "GRID": "angular",
        "CHEV": "angular",
        "CIRC": "circular",
        "OPER": "compound",
        "HUM": "compound",
        "ANIM": "compound",
        "PLANT": "organic",
        "ABSTR": "minimal",
        "RIT": "compound",
        "ARCH": "angular",
        "MISC": "varied",
    }

    # Group to element mapping
    GROUP_ELEMENTS: dict[str, str] = {
        "NUM": "air",
        "CON": "earth",
        "GRID": "earth",
        "CHEV": "fire",
        "CIRC": "spirit",
        "OPER": "fire",
        "HUM": "water",
        "ANIM": "earth",
        "PLANT": "water",
        "ABSTR": "air",
        "RIT": "spirit",
        "ARCH": "earth",
        "MISC": "spirit",
    }

    # Group to cosmic zone mapping
    GROUP_ZONES: dict[str, str] = {
        "NUM": "celestial",
        "CON": "terrestrial",
        "GRID": "terrestrial",
        "CHEV": "celestial",
        "CIRC": "celestial",
        "OPER": "terrestrial",
        "HUM": "terrestrial",
        "ANIM": "terrestrial",
        "PLANT": "terrestrial",
        "ABSTR": "celestial",
        "RIT": "celestial",
        "ARCH": "terrestrial",
        "MISC": "chthonic",
    }

    # Phoneme to direction mapping
    PHONEME_DIRECTIONS: dict[str, str] = {
        "ka": "up", "ki": "up", "ku": "up",
        "ga": "down", "gi": "down", "gu": "down",
        "ta": "right", "ti": "right", "tu": "right",
        "da": "left", "di": "left", "du": "left",
        "na": "center", "ni": "center", "nu": "center",
        "ma": "center", "mi": "center", "mu": "center",
        "ra": "up", "ri": "up", "ru": "up",
        "la": "left", "li": "left", "lu": "left",
        "sa": "up", "si": "up", "su": "up",
        "ha": "up", "hi": "up", "hu": "up",
        "ya": "right", "yi": "right", "yu": "right",
        "wa": "center", "wi": "center", "wu": "center",
        "pa": "down", "pi": "down", "pu": "down",
    }

    # Balance thresholds for elemental analysis
    MONO_ELEMENTAL_COUNT = 1
    DUAL_ELEMENTAL_COUNT = 2
    BALANCED_MIN_COUNT = 4

    def __init__(self) -> None:
        """Initialize the geometry analyzer."""
        pass

    def get_shape_class(self, sign: HarappanSign) -> str:
        """Get the shape class of a sign."""
        return self.GROUP_SHAPES.get(sign.group, "varied")

    def get_element(self, sign: HarappanSign) -> str:
        """Get the elemental association of a sign."""
        return self.GROUP_ELEMENTS.get(sign.group, "spirit")

    def get_cosmic_zone(self, sign: HarappanSign) -> str:
        """Get the cosmic zone of a sign."""
        return self.GROUP_ZONES.get(sign.group, "terrestrial")

    def get_direction(self, sign: HarappanSign) -> str:
        """Get the directional association of a sign."""
        return self.PHONEME_DIRECTIONS.get(sign.phoneme, "center")

    def get_symmetry(self, sign: HarappanSign) -> str:
        """
        Determine symmetry type based on group and phoneme.

        Args:
            sign: The Harappan sign

        Returns:
            Symmetry type string
        """
        # Groups with typically symmetric signs
        if sign.group in ("CIRC", "ABSTR"):
            return "radial"
        if sign.group in ("CHEV", "ARCH"):
            return "vertical"
        if sign.group in ("NUM", "GRID"):
            return "horizontal"
        return "none"

    def get_complexity(self, sign: HarappanSign) -> int:
        """
        Estimate visual complexity of a sign (1-5 scale).

        Args:
            sign: The Harappan sign

        Returns:
            Complexity value 1-5
        """
        # CVC phonemes are more complex
        if len(sign.phoneme) >= 3:
            return 4

        # Compound groups are more complex
        if sign.group in ("HUM", "ANIM", "RIT"):
            return 4

        # Simple groups
        if sign.group in ("NUM", "ABSTR"):
            return 2

        return 3

    def get_properties(self, sign: HarappanSign) -> GeometricProperties:
        """
        Get complete geometric properties of a sign.

        Args:
            sign: The Harappan sign

        Returns:
            GeometricProperties dataclass
        """
        return GeometricProperties(
            shape_class=self.get_shape_class(sign),
            symmetry=self.get_symmetry(sign),
            complexity=self.get_complexity(sign),
            element=self.get_element(sign),
            direction=self.get_direction(sign),
            cosmic_zone=self.get_cosmic_zone(sign),
        )

    def get_compatible_signs(
        self, sign: HarappanSign, signs: list[HarappanSign]
    ) -> list[HarappanSign]:
        """
        Find geometrically compatible signs.

        Args:
            sign: The reference sign
            signs: List of signs to filter

        Returns:
            List of compatible signs
        """
        ref_props = self.get_properties(sign)
        compatible: list[HarappanSign] = []

        for other in signs:
            other_props = self.get_properties(other)

            # Same element or complementary
            if other_props.element == ref_props.element:
                compatible.append(other)
            # Same cosmic zone
            elif other_props.cosmic_zone == ref_props.cosmic_zone:
                compatible.append(other)

        return compatible

    def analyze_sequence(self, signs: list[HarappanSign]) -> dict:
        """
        Analyze geometric properties of a sign sequence.

        Args:
            signs: List of Harappan signs

        Returns:
            Dictionary with sequence analysis
        """
        if not signs:
            return {"error": "Empty sequence"}

        elements = [self.get_element(s) for s in signs]
        zones = [self.get_cosmic_zone(s) for s in signs]
        complexities = [self.get_complexity(s) for s in signs]

        return {
            "count": len(signs),
            "elements": list(set(elements)),
            "dominant_element": max(set(elements), key=elements.count),
            "zones": list(set(zones)),
            "dominant_zone": max(set(zones), key=zones.count),
            "average_complexity": sum(complexities) / len(complexities),
            "balance": self._calculate_balance(elements),
        }

    def _calculate_balance(self, elements: list[str]) -> str:
        """Calculate elemental balance of a sequence."""
        counts = {e: elements.count(e) for e in set(elements)}
        if len(counts) == self.MONO_ELEMENTAL_COUNT:
            return "mono-elemental"
        if len(counts) == self.DUAL_ELEMENTAL_COUNT:
            return "dual-elemental"
        if len(counts) >= self.BALANCED_MIN_COUNT:
            return "balanced"
        return "varied"
