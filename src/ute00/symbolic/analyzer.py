"""
Symbolic Analyzer for UTE-0/0.

Analyzes text for archetypal and symbolic content.
"""

from dataclasses import dataclass
from typing import Dict, List

from ute00.symbolic.archetypes import Archetype, ArchetypalSystem


@dataclass
class SymbolicAnalysis:
    """Result of symbolic analysis."""

    original: str
    detected_archetypes: List[Archetype]
    dominant_elements: List[str]
    vibration_profile: Dict[str, int]
    symbolic_meaning: str


class SymbolicAnalyzer:
    """
    Analyzes text for symbolic and archetypal content.

    Implements Phase 5 of the UTE-0/0 pipeline.
    """

    # Word to archetype mapping (simplified)
    WORD_ARCHETYPE_MAP: Dict[str, str] = {
        # Mother archetype keywords
        "mother": "mother",
        "mãe": "mother",
        "madre": "mother",
        "mutter": "mother",
        "earth": "mother",
        "terra": "mother",
        "womb": "mother",
        "birth": "mother",
        "nurture": "mother",
        "create": "mother",
        "origin": "mother",
        # Fire archetype keywords
        "fire": "fire",
        "fogo": "fire",
        "fuego": "fire",
        "feuer": "fire",
        "flame": "fire",
        "burn": "fire",
        "light": "fire",
        "sun": "fire",
        "sol": "fire",
        "energy": "fire",
        "passion": "fire",
        # Serpent archetype keywords
        "serpent": "serpent",
        "snake": "serpent",
        "serpente": "serpent",
        "cobra": "serpent",
        "wisdom": "serpent",
        "cycle": "serpent",
        "spiral": "serpent",
        "kundalini": "serpent",
        "renewal": "serpent",
        # Timeline archetype keywords
        "time": "timeline",
        "tempo": "timeline",
        "flow": "timeline",
        "sequence": "timeline",
        "eternal": "timeline",
        "forever": "timeline",
        "continuity": "timeline",
        # Primordial water keywords
        "water": "primordial_water",
        "água": "primordial_water",
        "sea": "primordial_water",
        "ocean": "primordial_water",
        "void": "primordial_water",
        "source": "primordial_water",
        "abyss": "primordial_water",
        "deep": "primordial_water",
        # Extended archetypes
        "father": "sky_father",
        "pai": "sky_father",
        "sky": "sky_father",
        "heaven": "sky_father",
        "tree": "tree_of_life",
        "árvore": "tree_of_life",
        "growth": "tree_of_life",
        "hero": "hero",
        "herói": "hero",
        "journey": "hero",
        "shadow": "shadow",
        "sombra": "shadow",
        "dark": "shadow",
        "self": "self",
        "whole": "self",
        "unity": "self",
        "death": "death_rebirth",
        "rebirth": "death_rebirth",
        "transformation": "death_rebirth",
        "child": "divine_child",
        "criança": "divine_child",
        "hope": "divine_child",
        "future": "divine_child",
    }

    def __init__(self):
        """Initialize the symbolic analyzer."""
        self.archetype_system = ArchetypalSystem()

    def analyze(self, text: str) -> SymbolicAnalysis:
        """
        Perform symbolic analysis on text.

        Args:
            text: Text to analyze

        Returns:
            SymbolicAnalysis with detected archetypes and meanings
        """
        words = text.lower().split()
        detected = []
        element_counts: Dict[str, int] = {}
        vibration_counts: Dict[str, int] = {}

        for word in words:
            # Clean punctuation
            word = "".join(c for c in word if c.isalpha())
            if word in self.WORD_ARCHETYPE_MAP:
                archetype_name = self.WORD_ARCHETYPE_MAP[word]
                archetype = self.archetype_system.get_archetype(archetype_name)
                if archetype and archetype not in detected:
                    detected.append(archetype)

                    # Count elements
                    for element in archetype.elements:
                        element_counts[element] = element_counts.get(element, 0) + 1

                    # Count vibrations
                    vibration_counts[archetype.vibration] = (
                        vibration_counts.get(archetype.vibration, 0) + 1
                    )

        # Get dominant elements
        sorted_elements = sorted(
            element_counts.items(), key=lambda x: x[1], reverse=True
        )
        dominant_elements = [e[0] for e in sorted_elements[:3]]

        # Generate symbolic meaning
        meaning = self._generate_meaning(detected, dominant_elements)

        return SymbolicAnalysis(
            original=text,
            detected_archetypes=detected,
            dominant_elements=dominant_elements,
            vibration_profile=vibration_counts,
            symbolic_meaning=meaning,
        )

    def _generate_meaning(
        self, archetypes: List[Archetype], elements: List[str]
    ) -> str:
        """
        Generate a symbolic meaning summary.

        Args:
            archetypes: Detected archetypes
            elements: Dominant elements

        Returns:
            Summary string
        """
        if not archetypes:
            return "No archetypal patterns detected."

        archetype_names = [a.name for a in archetypes]
        all_meanings = []
        for a in archetypes:
            all_meanings.extend(a.meanings[:2])

        meaning = f"Archetypal patterns: {', '.join(archetype_names)}. "
        unique_meanings = list(set(all_meanings))[:5]
        meaning += f"Core themes: {', '.join(unique_meanings)}. "
        if elements:
            meaning += f"Elemental influence: {', '.join(elements)}."

        return meaning

    def get_archetype_for_word(self, word: str) -> Archetype | None:
        """
        Get the archetype associated with a word.

        Args:
            word: Word to look up

        Returns:
            Archetype if found, None otherwise
        """
        archetype_name = self.WORD_ARCHETYPE_MAP.get(word.lower())
        if archetype_name:
            return self.archetype_system.get_archetype(archetype_name)
        return None
