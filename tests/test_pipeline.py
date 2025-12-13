"""
Tests for the pipeline module.
"""

import pytest
from universal_translation.core.pipeline import (
    translate_text,
    translate_harappan,
    full_pipeline,
)


class TestTranslateText:
    """Tests for translate_text function."""

    def test_simple_translation(self):
        """Test translation of simple text."""
        result = translate_text("Hello world")
        assert result["input"] == "Hello world"
        assert "tokens" in result
        assert "phonemes" in result
        assert "symbolic" in result
        assert "synthesis" in result

    def test_empty_text(self):
        """Test translation of empty text."""
        result = translate_text("")
        assert result["input"] == ""
        assert result["tokens"] == []

    def test_specific_stages(self):
        """Test running specific stages only."""
        result = translate_text("test", stages=["tokenize"])
        assert "tokens" in result
        assert "phonemes" not in result or result.get("phonemes") is None

    def test_tokens_present(self):
        """Test that tokens are correctly generated."""
        result = translate_text("fire water earth")
        assert result["tokens"] == ["fire", "water", "earth"]


class TestTranslateHarappan:
    """Tests for translate_harappan function."""

    def test_simple_sequence(self):
        """Test translation of Harappan sequence."""
        result = translate_harappan([1, 8, 15])
        assert result["input_ids"] == [1, 8, 15]
        assert "decoded_signs" in result
        assert len(result["decoded_signs"]) == 3

    def test_empty_sequence(self):
        """Test translation of empty sequence."""
        result = translate_harappan([])
        assert result["input_ids"] == []
        assert result["decoded_signs"] == []

    def test_decoded_signs_structure(self):
        """Test structure of decoded signs."""
        result = translate_harappan([8])
        sign = result["decoded_signs"][0]
        assert "mahadevan_id" in sign
        assert "universal_code" in sign
        assert "category" in sign


class TestFullPipeline:
    """Tests for full_pipeline function."""

    def test_all_stages(self):
        """Test that all 10 stages are present."""
        result = full_pipeline("Hello")
        assert "stage_1_segmentation" in result
        assert "stage_2_phonemes" in result
        assert "stage_4_families" in result
        assert "stage_5_symbolic" in result
        assert "stage_6_archaeo" in result
        assert "stage_7_numerology" in result
        assert "stage_8_translations" in result
        assert "stage_9_diagram" in result
        assert "stage_10_universal" in result

    def test_universal_phrase_format(self):
        """Test format of final universal phrase."""
        result = full_pipeline("fire")
        phrase = result["stage_10_universal"]
        assert phrase.startswith("Universal Translation 0/0:")

    def test_with_inversions(self):
        """Test pipeline with inversions enabled."""
        result = full_pipeline("test", include_inversions=True)
        assert "inverted" in result["stage_1_segmentation"]

    def test_diagram_contains_metrics(self):
        """Test that diagram contains expected metrics."""
        result = full_pipeline("hello world")
        diagram = result["stage_9_diagram"]
        assert "token_count" in diagram
        assert "syllable_count" in diagram
        assert "numerological_root" in diagram
