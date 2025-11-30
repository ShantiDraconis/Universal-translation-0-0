"""
Tests for the tokenizer module.
"""

import pytest
from universal_translation.core.tokenizer import (
    basic_tokenize,
    syllable_tokenize,
    phoneme_tokenize,
    harappan_sign_tokenize,
)


class TestBasicTokenize:
    """Tests for basic_tokenize function."""

    def test_simple_text(self):
        """Test tokenization of simple text."""
        result = basic_tokenize("Hello world")
        assert result == ["Hello", "world"]

    def test_empty_string(self):
        """Test tokenization of empty string."""
        result = basic_tokenize("")
        assert result == []

    def test_single_word(self):
        """Test tokenization of single word."""
        result = basic_tokenize("Universal")
        assert result == ["Universal"]

    def test_multiple_spaces(self):
        """Test tokenization with multiple spaces."""
        result = basic_tokenize("Hello   world")
        assert result == ["Hello", "world"]

    def test_unicode_text(self):
        """Test tokenization with Unicode characters."""
        result = basic_tokenize("मनस् पितृ")
        assert result == ["मनस्", "पितृ"]


class TestSyllableTokenize:
    """Tests for syllable_tokenize function."""

    def test_simple_word(self):
        """Test syllable tokenization of simple word."""
        result = syllable_tokenize("hello")
        assert len(result) > 0

    def test_empty_string(self):
        """Test syllable tokenization of empty string."""
        result = syllable_tokenize("")
        assert result == []


class TestPhonemeTokenize:
    """Tests for phoneme_tokenize function."""

    def test_simple_word(self):
        """Test phoneme tokenization of simple word."""
        result = phoneme_tokenize("cat")
        assert "c" in result or "k" in result  # Depends on processing
        assert "a" in result
        assert "t" in result

    def test_empty_string(self):
        """Test phoneme tokenization of empty string."""
        result = phoneme_tokenize("")
        assert result == []


class TestHarappanSignTokenize:
    """Tests for harappan_sign_tokenize function."""

    def test_mahadevan_format(self):
        """Test tokenization of Mahadevan format signs."""
        result = harappan_sign_tokenize("M-001-M-008-M-015")
        assert "M-001" in result
        assert "M-008" in result
        assert "M-015" in result

    def test_simple_numbers(self):
        """Test tokenization of simple numeric signs."""
        result = harappan_sign_tokenize("1, 8, 15")
        assert "1" in result
        assert "8" in result
        assert "15" in result

    def test_empty_string(self):
        """Test tokenization of empty string."""
        result = harappan_sign_tokenize("")
        assert result == []
