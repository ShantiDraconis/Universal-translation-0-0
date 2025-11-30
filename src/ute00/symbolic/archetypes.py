"""
Archetypal System for UTE-0/0.

Defines the core archetypes for symbolic analysis.
"""

from dataclasses import dataclass
# Modern Python typing (3.10+)


@dataclass
class Archetype:
    """
    Represents a universal archetype.

    Attributes:
        name: Archetype name
        symbol: Primary symbol representation
        meanings: List of associated meanings
        elements: Related elemental associations
        vibration: Vibrational quality
    """

    name: str
    symbol: str
    meanings: list[str]
    elements: list[str]
    vibration: str


class ArchetypalSystem:
    """
    The Universal Archetypal System.

    Contains the core symbolic archetypes used in Phase 5 of UTE-0/0:
    - Mother
    - Fire
    - Serpent
    - Timeline
    - Primordial water
    """

    ARCHETYPES: dict[str, Archetype] = {
        # Core 5 archetypes from UTE-0/0 system
        "mother": Archetype(
            name="mother",
            symbol="◯",
            meanings=[
                "origin",
                "nurture",
                "protection",
                "fertility",
                "earth",
                "creation",
            ],
            elements=["earth", "water"],
            vibration="receptive",
        ),
        "fire": Archetype(
            name="fire",
            symbol="△",
            meanings=[
                "transformation",
                "energy",
                "passion",
                "destruction",
                "rebirth",
                "light",
            ],
            elements=["fire"],
            vibration="active",
        ),
        "serpent": Archetype(
            name="serpent",
            symbol="∿",
            meanings=[
                "wisdom",
                "kundalini",
                "cycle",
                "renewal",
                "knowledge",
                "eternity",
            ],
            elements=["earth", "water"],
            vibration="spiral",
        ),
        "timeline": Archetype(
            name="timeline",
            symbol="─",
            meanings=["continuity", "flow", "causality", "sequence", "eternity"],
            elements=["air"],
            vibration="linear",
        ),
        "primordial_water": Archetype(
            name="primordial_water",
            symbol="≈",
            meanings=[
                "source",
                "unconscious",
                "potential",
                "void",
                "creation",
                "dissolution",
            ],
            elements=["water"],
            vibration="flowing",
        ),
        # Extended archetypes
        "sky_father": Archetype(
            name="sky_father",
            symbol="⊙",
            meanings=["authority", "order", "light", "spirit", "consciousness"],
            elements=["air", "fire"],
            vibration="emanating",
        ),
        "tree_of_life": Archetype(
            name="tree_of_life",
            symbol="⸙",
            meanings=["growth", "connection", "cosmos", "axis_mundi", "levels"],
            elements=["earth", "water", "air"],
            vibration="ascending",
        ),
        "hero": Archetype(
            name="hero",
            symbol="⚔",
            meanings=["journey", "transformation", "trial", "victory", "return"],
            elements=["fire", "air"],
            vibration="dynamic",
        ),
        "shadow": Archetype(
            name="shadow",
            symbol="◐",
            meanings=["unconscious", "repressed", "potential", "darkness", "hidden"],
            elements=["earth", "water"],
            vibration="hidden",
        ),
        "self": Archetype(
            name="self",
            symbol="☉",
            meanings=["wholeness", "integration", "center", "completion", "unity"],
            elements=["fire", "air", "water", "earth"],
            vibration="harmonizing",
        ),
        "death_rebirth": Archetype(
            name="death_rebirth",
            symbol="☽☾",
            meanings=[
                "transformation",
                "cycle",
                "ending",
                "beginning",
                "transcendence",
            ],
            elements=["water", "fire"],
            vibration="cyclical",
        ),
        "divine_child": Archetype(
            name="divine_child",
            symbol="✦",
            meanings=["potential", "innocence", "future", "hope", "new_beginning"],
            elements=["air", "fire"],
            vibration="emerging",
        ),
    }

    def __init__(self):
        """Initialize the archetypal system."""
        self._by_element: dict[str, list[Archetype]] = {}
        for archetype in self.ARCHETYPES.values():
            for element in archetype.elements:
                if element not in self._by_element:
                    self._by_element[element] = []
                self._by_element[element].append(archetype)

    def get_archetype(self, name: str) -> Archetype | None:
        """
        Get an archetype by name.

        Args:
            name: Archetype name

        Returns:
            Archetype if found, None otherwise
        """
        return self.ARCHETYPES.get(name.lower())

    def get_by_element(self, element: str) -> list[Archetype]:
        """
        Get archetypes associated with an element.

        Args:
            element: Element name (fire, water, earth, air)

        Returns:
            List of associated archetypes
        """
        return self._by_element.get(element.lower(), [])

    def get_by_vibration(self, vibration: str) -> list[Archetype]:
        """
        Get archetypes by vibrational quality.

        Args:
            vibration: Vibrational quality

        Returns:
            List of matching archetypes
        """
        return [
            a for a in self.ARCHETYPES.values() if a.vibration == vibration.lower()
        ]

    def find_by_meaning(self, meaning: str) -> list[Archetype]:
        """
        Find archetypes containing a specific meaning.

        Args:
            meaning: Meaning to search

        Returns:
            List of archetypes with that meaning
        """
        meaning = meaning.lower()
        return [a for a in self.ARCHETYPES.values() if meaning in a.meanings]

    def get_core_archetypes(self) -> list[Archetype]:
        """
        Get the core 5 archetypes of UTE-0/0.

        Returns:
            List of core archetypes
        """
        core_names = ["mother", "fire", "serpent", "timeline", "primordial_water"]
        return [self.ARCHETYPES[name] for name in core_names]

    @property
    def all_archetypes(self) -> list[Archetype]:
        """Return all archetypes."""
        return list(self.ARCHETYPES.values())
