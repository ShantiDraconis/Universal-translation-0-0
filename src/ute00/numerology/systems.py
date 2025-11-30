"""
Numerology Systems for UTE-0/0.

Defines the four numerology systems used in Phase 6:
- Pythagorean
- Kabbalistic
- Astrological
- Mirrored
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict


class NumerologyType(Enum):
    """Types of numerology systems."""

    PYTHAGOREAN = "pythagorean"
    KABBALISTIC = "kabbalistic"
    ASTROLOGICAL = "astrological"
    MIRRORED = "mirrored"


@dataclass
class NumerologySystem:
    """
    Represents a numerology mapping system.

    Attributes:
        name: System name
        description: System description
        letter_values: Letter to number mapping
    """

    name: str
    description: str
    letter_values: Dict[str, int]


# Pythagorean numerology: most common Western system
PYTHAGOREAN_VALUES: Dict[str, int] = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 4,
    "n": 5,
    "o": 6,
    "p": 7,
    "q": 8,
    "r": 9,
    "s": 1,
    "t": 2,
    "u": 3,
    "v": 4,
    "w": 5,
    "x": 6,
    "y": 7,
    "z": 8,
}

# Kabbalistic/Hebrew numerology (Gematria-inspired)
KABBALISTIC_VALUES: Dict[str, int] = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 80,
    "g": 3,
    "h": 5,
    "i": 10,
    "j": 10,
    "k": 20,
    "l": 30,
    "m": 40,
    "n": 50,
    "o": 70,
    "p": 80,
    "q": 100,
    "r": 200,
    "s": 300,
    "t": 400,
    "u": 6,
    "v": 6,
    "w": 6,
    "x": 60,
    "y": 10,
    "z": 7,
}

# Astrological numerology (based on planetary associations)
ASTROLOGICAL_VALUES: Dict[str, int] = {
    "a": 1,  # Sun
    "b": 2,  # Moon
    "c": 3,  # Jupiter
    "d": 4,  # Uranus
    "e": 5,  # Mercury
    "f": 6,  # Venus
    "g": 7,  # Neptune
    "h": 8,  # Saturn
    "i": 9,  # Mars
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 4,
    "n": 5,
    "o": 6,
    "p": 7,
    "q": 8,
    "r": 9,
    "s": 1,
    "t": 2,
    "u": 3,
    "v": 4,
    "w": 5,
    "x": 6,
    "y": 7,
    "z": 8,
}

# Mirrored numerology (reflection system for UTE-0/0)
MIRRORED_VALUES: Dict[str, int] = {
    "a": 9,
    "b": 8,
    "c": 7,
    "d": 6,
    "e": 5,
    "f": 4,
    "g": 3,
    "h": 2,
    "i": 1,
    "j": 9,
    "k": 8,
    "l": 7,
    "m": 6,
    "n": 5,
    "o": 4,
    "p": 3,
    "q": 2,
    "r": 1,
    "s": 9,
    "t": 8,
    "u": 7,
    "v": 6,
    "w": 5,
    "x": 4,
    "y": 3,
    "z": 2,
}

# System definitions
NUMEROLOGY_SYSTEMS: Dict[NumerologyType, NumerologySystem] = {
    NumerologyType.PYTHAGOREAN: NumerologySystem(
        name="Pythagorean",
        description="Western numerology based on Pythagorean number philosophy",
        letter_values=PYTHAGOREAN_VALUES,
    ),
    NumerologyType.KABBALISTIC: NumerologySystem(
        name="Kabbalistic",
        description="Hebrew-inspired Gematria numerology system",
        letter_values=KABBALISTIC_VALUES,
    ),
    NumerologyType.ASTROLOGICAL: NumerologySystem(
        name="Astrological",
        description="Numerology based on planetary associations",
        letter_values=ASTROLOGICAL_VALUES,
    ),
    NumerologyType.MIRRORED: NumerologySystem(
        name="Mirrored",
        description="UTE-0/0 reflection numerology system (I = 0/0)",
        letter_values=MIRRORED_VALUES,
    ),
}


def get_system(system_type: NumerologyType) -> NumerologySystem:
    """
    Get a numerology system by type.

    Args:
        system_type: Type of numerology system

    Returns:
        NumerologySystem instance
    """
    return NUMEROLOGY_SYSTEMS[system_type]


def get_all_systems() -> Dict[NumerologyType, NumerologySystem]:
    """
    Get all numerology systems.

    Returns:
        Dictionary of all systems
    """
    return NUMEROLOGY_SYSTEMS
