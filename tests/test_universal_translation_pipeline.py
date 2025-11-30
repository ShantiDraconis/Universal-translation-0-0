"""Tests for the universal translation pipeline."""

import pytest

from universal_translation_00.core.pipeline_manager import UniversalTranslator, TranslationResult


class TestUniversalTranslator:
    """Test suite for UniversalTranslator class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.translator = UniversalTranslator()

    def test_translate_simple_text(self) -> None:
        """Test translation of simple text."""
        result = self.translator.translate("mama")
        assert isinstance(result, TranslationResult)
        assert result.original_text == "mama"
        assert len(result.phonemes) > 0

    def test_translate_returns_phonetic_reading(self) -> None:
        """Test that translation returns phonetic reading."""
        result = self.translator.translate("tata")
        assert result.phonetic_reading != ""

    def test_translate_returns_harappan_sequence(self) -> None:
        """Test that translation returns Harappan sequence."""
        result = self.translator.translate("nama")
        # May or may not have Harappan signs depending on mapping
        assert isinstance(result.harappan_sequence, str)

    def test_translate_to_phonemes(self) -> None:
        """Test quick phoneme translation."""
        phonemes = self.translator.translate_to_phonemes("kamana")
        assert isinstance(phonemes, list)

    def test_translate_to_harappan(self) -> None:
        """Test quick Harappan translation."""
        harappan = self.translator.translate_to_harappan("sama")
        assert isinstance(harappan, list)

    def test_translate_empty_text(self) -> None:
        """Test translation of empty text."""
        result = self.translator.translate("")
        assert result.original_text == ""
        assert len(result.phonemes) == 0

    def test_translate_with_etymology(self) -> None:
        """Test translation includes etymology."""
        translator = UniversalTranslator(include_etymology=True)
        result = translator.translate("mama")
        assert "etymology" in result.metadata

    def test_translate_metadata(self) -> None:
        """Test that translation includes metadata."""
        result = self.translator.translate("test")
        assert "word_count" in result.metadata
        assert "phoneme_count" in result.metadata


class TestTranslationResult:
    """Test suite for TranslationResult dataclass."""

    def test_result_to_dict(self) -> None:
        """Test conversion to dictionary."""
        translator = UniversalTranslator()
        result = translator.translate("ka")
        d = result.to_dict()

        assert "original_text" in d
        assert "phonetic_reading" in d
        assert "harappan_sequence" in d
        assert "tokens" in d
        assert "phonemes" in d

    def test_result_repr(self) -> None:
        """Test string representation."""
        translator = UniversalTranslator()
        result = translator.translate("ta")
        repr_str = repr(result)

        assert "TranslationResult" in repr_str
        assert "original" in repr_str
