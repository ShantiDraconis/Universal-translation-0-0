"""
Harappan Sign System for UTE-0/0.

Implements the 417 Harappan signs mapping system.
Symbol → Number → Dynamics
"""

from dataclasses import dataclass
# Modern Python typing (3.10+)


@dataclass
class HarappanSign:
    """
    Represents a Harappan sign with its properties.

    Attributes:
        sign_id: Unique identifier (1-417)
        symbol: Unicode representation or description
        numeric_value: Associated numerical value
        dynamics: Dynamic interpretation
        category: Sign category (pictographic, abstract, compound)
    """

    sign_id: int
    symbol: str
    numeric_value: int
    dynamics: str
    category: str


class HarappanSignSystem:
    """
    The Harappan sign system containing 417 signs.

    This implements Phase 3 of the UTE-0/0 pipeline:
    Symbol → Number → Dynamics
    """

    # Initial set of key Harappan signs (simplified representation)
    # Full system would contain all 417 documented signs
    SIGNS: dict[int, HarappanSign] = {
        # Anthropomorphic signs
        1: HarappanSign(1, "𐠀", 1, "human_standing", "anthropomorphic"),
        2: HarappanSign(2, "𐠁", 2, "human_seated", "anthropomorphic"),
        3: HarappanSign(3, "𐠂", 3, "human_arms_raised", "anthropomorphic"),
        # Animal signs
        10: HarappanSign(10, "𐠊", 10, "bull", "zoomorphic"),
        11: HarappanSign(11, "𐠋", 11, "elephant", "zoomorphic"),
        12: HarappanSign(12, "𐠌", 12, "rhinoceros", "zoomorphic"),
        13: HarappanSign(13, "𐠍", 13, "tiger", "zoomorphic"),
        14: HarappanSign(14, "𐠎", 14, "fish", "zoomorphic"),
        15: HarappanSign(15, "𐠏", 15, "bird", "zoomorphic"),
        # Plant signs
        20: HarappanSign(20, "𐠔", 20, "tree", "botanical"),
        21: HarappanSign(21, "𐠕", 21, "grain", "botanical"),
        22: HarappanSign(22, "𐠖", 22, "leaf", "botanical"),
        # Geometric signs
        30: HarappanSign(30, "𐠞", 30, "circle", "geometric"),
        31: HarappanSign(31, "𐠟", 31, "square", "geometric"),
        32: HarappanSign(32, "𐠠", 32, "triangle", "geometric"),
        33: HarappanSign(33, "𐠡", 33, "line_vertical", "geometric"),
        34: HarappanSign(34, "𐠢", 34, "line_horizontal", "geometric"),
        35: HarappanSign(35, "𐠣", 35, "cross", "geometric"),
        # Numerical signs
        40: HarappanSign(40, "𐠨", 1, "one_stroke", "numerical"),
        41: HarappanSign(41, "𐠩", 2, "two_strokes", "numerical"),
        42: HarappanSign(42, "𐠪", 3, "three_strokes", "numerical"),
        43: HarappanSign(43, "𐠫", 4, "four_strokes", "numerical"),
        44: HarappanSign(44, "𐠬", 5, "five_strokes", "numerical"),
        # Water signs
        50: HarappanSign(50, "𐠲", 50, "water_wave", "elemental"),
        51: HarappanSign(51, "𐠳", 51, "water_vessel", "elemental"),
        # Fire signs
        60: HarappanSign(60, "𐠼", 60, "fire_flames", "elemental"),
        61: HarappanSign(61, "𐠽", 61, "sun_rays", "elemental"),
        # Container signs
        70: HarappanSign(70, "𐡆", 70, "jar", "container"),
        71: HarappanSign(71, "𐡇", 71, "pot", "container"),
        # Abstract compound signs
        100: HarappanSign(100, "𐡤", 100, "compound_deity", "compound"),
        101: HarappanSign(101, "𐡥", 101, "compound_ritual", "compound"),
        # Directional signs
        200: HarappanSign(200, "𐢀", 200, "direction_up", "directional"),
        201: HarappanSign(201, "𐢁", 201, "direction_down", "directional"),
        202: HarappanSign(202, "𐢂", 202, "direction_left", "directional"),
        203: HarappanSign(203, "𐢃", 203, "direction_right", "directional"),
    }

    def __init__(self):
        """Initialize the Harappan sign system."""
        self._reverse_lookup: dict[str, HarappanSign] = {
            sign.symbol: sign for sign in self.SIGNS.values()
        }

    def get_sign(self, sign_id: int) -> HarappanSign | None:
        """
        Get a sign by its ID.

        Args:
            sign_id: Sign identifier (1-417)

        Returns:
            HarappanSign if found, None otherwise
        """
        return self.SIGNS.get(sign_id)

    def get_sign_by_symbol(self, symbol: str) -> HarappanSign | None:
        """
        Get a sign by its symbol representation.

        Args:
            symbol: Unicode symbol

        Returns:
            HarappanSign if found, None otherwise
        """
        return self._reverse_lookup.get(symbol)

    def get_signs_by_category(self, category: str) -> list[HarappanSign]:
        """
        Get all signs in a category.

        Args:
            category: Sign category

        Returns:
            List of signs in the category
        """
        return [sign for sign in self.SIGNS.values() if sign.category == category]

    def get_numeric_value(self, sign_id: int) -> int | None:
        """
        Get the numeric value of a sign.

        Args:
            sign_id: Sign identifier

        Returns:
            Numeric value if found, None otherwise
        """
        sign = self.get_sign(sign_id)
        return sign.numeric_value if sign else None

    def get_all_categories(self) -> list[str]:
        """
        Get all unique sign categories.

        Returns:
            List of category names
        """
        return list(set(sign.category for sign in self.SIGNS.values()))

    @property
    def total_signs(self) -> int:
        """Return the total number of signs in the system."""
        return len(self.SIGNS)
