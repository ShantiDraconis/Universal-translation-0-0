"""
Universal Translation Engine 0/0.

The main translation engine that implements the full UTE-0/0 pipeline:
T(x) = U( S(f), H(f), D(f), A(f), N(f) )

Where:
- S = Segmentation
- H = Harappan
- D = Dictionary 00
- A = Symbolic Archetypes
- N = Scientific Numerology
"""

from dataclasses import dataclass

from ute00.phonetics.analyzer import PhoneticAnalyzer, PhonemeMapping
from ute00.phonetics.segmenter import PhoneticSegmenter, SegmentationResult
from ute00.harappan.mapper import HarappanMapper, HarappanMapping
from ute00.dictionary00.matcher import RootMatcher, RootMatch
from ute00.symbolic.analyzer import SymbolicAnalyzer, SymbolicAnalysis
from ute00.numerology.calculator import NumerologyCalculator, NumerologyResult
from ute00.archetypes.families import LinguisticFamilySystem


@dataclass
class TranslationResult:
    """
    Complete result of the Universal Translation 0/0.

    Contains results from all phases of the pipeline.
    """

    # Original input
    original: str

    # Phase 1: Segmentation
    segmentation: SegmentationResult
    phoneme_mappings: list[PhonemeMapping]

    # Phase 2: Dictionary 00
    root_matches: list[RootMatch]

    # Phase 3: Harappan
    harappan: HarappanMapping

    # Phase 4: Linguistic families (cognates)
    cognates: dict[str, str]

    # Phase 5: Symbolic analysis
    symbolic: SymbolicAnalysis

    # Phase 6: Numerology
    numerology: NumerologyResult

    # Phase 7: Final synthesis
    universal_translation: str

    # Metadata
    indetermination_operator: str  # I = 0/0


class UniversalTranslator:
    """
    The Universal Translation Engine 0/0.

    Implements the formal translation function:
    T(x) = U( S(f), H(f), D(f), A(f), N(f) )

    The main operator is I = 0/0, representing:
    - Indetermination operator
    - Simultaneous origin and dissolution
    - Universal vibrational constant
    """

    # The universal indetermination operator
    I = "0/0"

    def __init__(self):
        """Initialize the Universal Translation Engine."""
        # Initialize all subsystems
        self.phonetic_analyzer = PhoneticAnalyzer()
        self.segmenter = PhoneticSegmenter()
        self.harappan_mapper = HarappanMapper()
        self.root_matcher = RootMatcher()
        self.symbolic_analyzer = SymbolicAnalyzer()
        self.numerology = NumerologyCalculator()
        self.linguistic_families = LinguisticFamilySystem()

    def translate(self, text: str) -> TranslationResult:
        """
        Perform Universal Translation 0/0 on input text.

        This implements the full 7-phase pipeline.

        Args:
            text: Input text to translate

        Returns:
            TranslationResult containing all analysis phases
        """
        # Phase 1: Segmentation and phonetic analysis
        segmentation = self.segmenter.segment(text)
        phoneme_mappings = self.phonetic_analyzer.analyze(text)

        # Phase 2: Dictionary 00 root matching
        root_matches = self.root_matcher.match_word(text)

        # Phase 3: Harappan mapping
        harappan = self.harappan_mapper.map_text(text)

        # Phase 4: Find cognates across linguistic families
        cognates = self._find_cognates(text)

        # Phase 5: Symbolic analysis
        symbolic = self.symbolic_analyzer.analyze(text)

        # Phase 6: Numerology
        numerology_result = self.numerology.calculate(text)

        # Phase 7: Final synthesis
        universal_translation = self._synthesize(
            text,
            segmentation,
            root_matches,
            harappan,
            symbolic,
            numerology_result,
        )

        return TranslationResult(
            original=text,
            segmentation=segmentation,
            phoneme_mappings=phoneme_mappings,
            root_matches=root_matches,
            harappan=harappan,
            cognates=cognates,
            symbolic=symbolic,
            numerology=numerology_result,
            universal_translation=universal_translation,
            indetermination_operator=self.I,
        )

    def _find_cognates(self, text: str) -> dict[str, str]:
        """
        Find cognates for words in text across linguistic families.

        Args:
            text: Input text

        Returns:
            Dictionary of family -> cognate word
        """
        # Try to find cognates for common meanings
        words = text.lower().split()
        cognates = {}

        meaning_keywords = {
            "water": "water",
            "mother": "mother",
            "sun": "sun",
            "fire": "fire",
            "earth": "earth",
            "água": "water",
            "mãe": "mother",
            "sol": "sun",
            "fogo": "fire",
            "terra": "earth",
        }

        for word in words:
            word = "".join(c for c in word if c.isalpha())
            if word in meaning_keywords:
                meaning = meaning_keywords[word]
                family_cognates = self.linguistic_families.find_cognates(word, meaning)
                cognates.update(family_cognates)
                break

        return cognates

    def _synthesize(
        self,
        text: str,
        segmentation: SegmentationResult,
        root_matches: list[RootMatch],
        harappan: HarappanMapping,
        symbolic: SymbolicAnalysis,
        numerology: NumerologyResult,
    ) -> str:
        """
        Synthesize the final Universal Translation 0/0.

        Args:
            text: Original text
            segmentation: Segmentation result
            root_matches: Root matching results
            harappan: Harappan mapping result
            symbolic: Symbolic analysis result
            numerology: Numerology result

        Returns:
            Final universal translation string
        """
        parts = [f"Universal Translation 0/0: '{text}'"]

        # Add Da Vinci reading (inverted)
        parts.append(f"Da Vinci reading: '{segmentation.horizontal_inversion}'")

        # Add root etymology if found
        if root_matches:
            best_match = root_matches[0]
            parts.append(
                f"Proto-root: {best_match.root.root} ({best_match.root.meaning})"
            )

        # Add Harappan interpretation
        if harappan.signs:
            dynamics = ", ".join(harappan.dynamics[:3])
            parts.append(f"Harappan dynamics: {dynamics}")

        # Add symbolic meaning
        if symbolic.detected_archetypes:
            archetypes = ", ".join(a.name for a in symbolic.detected_archetypes[:3])
            parts.append(f"Archetypes: {archetypes}")

        # Add numerological signature
        parts.append(
            f"Vibrational number: {numerology.pythagorean_reduced} ({numerology.interpretation})"
        )

        # Final synthesis with I = 0/0
        parts.append(f"Operator I = {self.I}: Origin-Dissolution Unity")

        return " | ".join(parts)

    def get_vibration(self, text: str) -> float:
        """
        Get the total vibrational value of text.

        Args:
            text: Input text

        Returns:
            Total vibration value
        """
        return self.phonetic_analyzer.get_total_vibration(text)

    def get_harappan_sequence(self, text: str) -> list[str]:
        """
        Get the Harappan symbol sequence for text.

        Args:
            text: Input text

        Returns:
            List of Harappan symbols
        """
        return self.harappan_mapper.get_sign_sequence(text)

    def get_archetypes(self, text: str) -> list[str]:
        """
        Get detected archetypes in text.

        Args:
            text: Input text

        Returns:
            List of archetype names
        """
        analysis = self.symbolic_analyzer.analyze(text)
        return [a.name for a in analysis.detected_archetypes]

    def compare_numerology(self, text: str) -> dict[str, tuple[int, int]]:
        """
        Compare numerology across all systems.

        Args:
            text: Input text

        Returns:
            Dictionary of system -> (total, reduced) values
        """
        return self.numerology.compare_systems(text)
