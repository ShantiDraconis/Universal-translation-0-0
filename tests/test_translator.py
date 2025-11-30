"""
Tests for the translator engine.
"""

import pytest
from ute00.translator.engine import UniversalTranslator, TranslationResult


class TestUniversalTranslator:
    """Tests for UniversalTranslator."""

    def test_init(self):
        """Test translator initialization."""
        translator = UniversalTranslator()
        assert translator is not None
        assert translator.I == "0/0"

    def test_translate(self):
        """Test basic translation."""
        translator = UniversalTranslator()
        result = translator.translate("water")
        assert isinstance(result, TranslationResult)
        assert result.original == "water"
        assert result.indetermination_operator == "0/0"

    def test_translate_has_all_phases(self):
        """Test translation includes all pipeline phases."""
        translator = UniversalTranslator()
        result = translator.translate("mother")

        # Check all phases are present
        assert result.segmentation is not None
        assert result.phoneme_mappings is not None
        assert result.root_matches is not None
        assert result.harappan is not None
        assert result.cognates is not None
        assert result.symbolic is not None
        assert result.numerology is not None
        assert result.universal_translation is not None

    def test_get_vibration(self):
        """Test vibration calculation."""
        translator = UniversalTranslator()
        vibration = translator.get_vibration("ab")
        assert vibration == 7.0  # a=1.0, b=6.0

    def test_get_harappan_sequence(self):
        """Test Harappan sequence generation."""
        translator = UniversalTranslator()
        sequence = translator.get_harappan_sequence("ab")
        assert len(sequence) == 2

    def test_compare_numerology(self):
        """Test numerology comparison."""
        translator = UniversalTranslator()
        comparison = translator.compare_numerology("test")
        assert "pythagorean" in comparison
        assert "kabbalistic" in comparison
        assert "astrological" in comparison
        assert "mirrored" in comparison

    def test_universal_translation_format(self):
        """Test universal translation output format."""
        translator = UniversalTranslator()
        result = translator.translate("fire")
        assert "Universal Translation 0/0:" in result.universal_translation
        assert "Da Vinci reading:" in result.universal_translation
        assert "Operator I = 0/0" in result.universal_translation
