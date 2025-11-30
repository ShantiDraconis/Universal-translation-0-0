"""Configuration settings for Universal Translation 0/0."""

from pathlib import Path
from typing import Any

# Base paths
ROOT_DIR = Path(__file__).parent.parent.parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXAMPLES_DIR = DATA_DIR / "examples"

# Data files
HARAPPAN_417_CSV = RAW_DATA_DIR / "harappan_417_signs.csv"
PHONETIC_ROOTS_CSV = RAW_DATA_DIR / "phonetic_roots_global.csv"
DICTIONARY_00_CSV = RAW_DATA_DIR / "00_dictionary_1000.csv"

# Processed data files (JSON)
HARAPPAN_INDEX_JSON = PROCESSED_DATA_DIR / "harappan_sign_index.json"
PHONEME_TABLE_JSON = PROCESSED_DATA_DIR / "phoneme_universal_table.json"
DICT00_BY_TOKEN_JSON = PROCESSED_DATA_DIR / "dict00_index_by_token.json"
DICT00_BY_PHONEME_JSON = PROCESSED_DATA_DIR / "dict00_index_by_phoneme.json"

# Semantic group mappings
SEMANTIC_GROUPS: dict[str, dict[str, Any]] = {
    "NUM": {
        "full_name": "NUM_TALLY",
        "range": (1, 40),
        "phonemes": ["ta", "ti", "tu", "na", "ni", "nu", "sa", "si", "su", "wa", "ya", "ri"],
        "semantic_field": "counting, numbers, time, quantity",
        "description": "Counting marks, tally strokes, numerical values",
    },
    "CON": {
        "full_name": "CONTAINER",
        "range": (41, 80),
        "phonemes": ["ka", "ko", "ku", "ga", "go", "gu", "ma", "mo", "mu", "pa", "po", "pu"],
        "semantic_field": "containers, vessels, storage, measurement",
        "description": "Jars, pots, boxes, volume containers",
    },
    "GRID": {
        "full_name": "GRID_FIELD",
        "range": (81, 110),
        "phonemes": ["ra", "ri", "ru", "la", "li", "lu", "re", "le", "ro", "we"],
        "semantic_field": "fields, grids, patterns, weaving",
        "description": "Fields, matrices, woven patterns",
    },
    "CHEV": {
        "full_name": "CHEVRON_MOUNTAIN",
        "range": (111, 130),
        "phonemes": ["ka", "ki", "ku", "ha", "hi", "hu", "ta", "ti", "tu"],
        "semantic_field": "mountains, peaks, elevation, effort",
        "description": "Mountain shapes, chevrons, peaks",
    },
    "CIRC": {
        "full_name": "CIRCLE_CYCLE",
        "range": (131, 150),
        "phonemes": ["so", "su", "sa", "yo", "ya", "yu", "o", "u"],
        "semantic_field": "sun, moon, cycles, wholeness",
        "description": "Circular shapes, celestial cycles",
    },
    "OPER": {
        "full_name": "OPERATOR_TRIDENT",
        "range": (151, 190),
        "phonemes": ["ta", "ti", "tu", "da", "di", "du", "sa", "si", "su", "ra", "ri", "ru"],
        "semantic_field": "verbs, actions, connections, operations",
        "description": "Tridents, action markers, verbal operators",
    },
    "HUM": {
        "full_name": "HUMAN_AGENT",
        "range": (191, 230),
        "phonemes": ["ma", "mi", "mu", "na", "ni", "nu", "ama", "ani", "anu", "ima", "ina", "inu"],
        "semantic_field": "people, roles, clans, family",
        "description": "Human figures, social roles, kinship",
    },
    "ANIM": {
        "full_name": "ANIMAL_NONFISH",
        "range": (231, 260),
        "phonemes": ["ga", "gi", "gu", "pa", "pi", "pu", "ra", "ri", "ru", "ka", "ki", "ku"],
        "semantic_field": "animals, totems, beasts, power",
        "description": "Totemic animals, creatures, animal parts",
    },
    "PLANT": {
        "full_name": "PLANT_CROP",
        "range": (261, 290),
        "phonemes": ["sa", "si", "su", "ya", "yi", "yu", "ka", "ki", "ku"],
        "semantic_field": "plants, crops, growth, harvest",
        "description": "Plants, agricultural symbols, vegetation",
    },
    "ABSTR": {
        "full_name": "ABSTRACT_LIGATURE",
        "range": (291, 320),
        "phonemes": ["a", "i", "u", "e", "o", "ha", "hi", "hu", "ya", "yi", "yu"],
        "semantic_field": "connectors, particles, abstract",
        "description": "Abstract connectors, grammatical particles",
    },
    "RIT": {
        "full_name": "RITUAL_STANDARD",
        "range": (321, 360),
        "phonemes": ["tak", "sak", "ram", "lam", "kam", "han", "yum", "kum"],
        "semantic_field": "rituals, standards, ceremonies, sacred",
        "description": "Ritual standards, ceremonial marks",
    },
    "ARCH": {
        "full_name": "ARCH_BUILDING",
        "range": (361, 390),
        "phonemes": ["ko", "ku", "kal", "kul", "kar", "tor", "dom", "mur"],
        "semantic_field": "architecture, buildings, cities, structures",
        "description": "Architectural symbols, building forms",
    },
    "MISC": {
        "full_name": "MISC_RARE",
        "range": (391, 417),
        "phonemes": ["a", "ma", "na", "ra", "ya", "ta", "sa", "ka", "la", "pa", "ga", "ha", "o", "i", "u"],
        "semantic_field": "proper names, rare signs, exceptions",
        "description": "Miscellaneous rare signs, proper nouns",
    },
}

# Universal phonetic roots with cross-linguistic attestations
UNIVERSAL_ROOTS: dict[str, dict[str, str]] = {
    "ma": {"meaning": "mother/matter/origin", "attestations": "Tamil amma, Latin mater, Chinese 媽"},
    "na": {"meaning": "self/person/being", "attestations": "Tamil nāṉ, Chinese 那, Latin natus"},
    "ka": {"meaning": "object/place/solid", "attestations": "Tamil kaḷ, Chinese 器, Latin casa"},
    "ta": {"meaning": "action/strike/time", "attestations": "Tamil taṭṭu, Chinese 打, Latin tactus"},
    "sa": {"meaning": "sacred/flow/spirit", "attestations": "Tamil cattiyam, Chinese 三/水, Latin sacrum"},
    "ra": {"meaning": "flow/line/king", "attestations": "Tamil irai, Chinese 理, Latin ratio"},
    "la": {"meaning": "level/plane/blade", "attestations": "Tamil ilai, Chinese 列, Latin latus"},
    "ya": {"meaning": "motion/already/union", "attestations": "Tamil yāṉ, Chinese 也, Latin iam"},
    "ha": {"meaning": "breath/spirit/soul", "attestations": "Tamil ācai, Chinese 哈, Latin halitus"},
    "pa": {"meaning": "part/piece/father", "attestations": "Tamil paṅku, Chinese 爸, Latin pars/pater"},
    "ga": {"meaning": "solid/grasp/claw", "attestations": "Tamil kaṭṭi, Chinese 罐, Latin gradus"},
    "da": {"meaning": "give/donate", "attestations": "Tamil tarum, Chinese 大, Latin dare"},
}

# Default configuration
DEFAULT_CONFIG: dict[str, Any] = {
    "max_candidates": 5,
    "phoneme_weight": 0.4,
    "semantic_weight": 0.3,
    "frequency_weight": 0.3,
    "output_format": "unicode",
    "include_etymology": True,
    "include_numerology": False,
}
