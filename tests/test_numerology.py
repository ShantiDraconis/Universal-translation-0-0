"""
Tests for the numerology_engine module.
"""

import pytest
from universal_translation.core.numerology_engine import (
    word_value,
    reduce_to_root,
    normalize_to_zero_over_zero,
    get_symbolic_meaning,
    analyze_word,
    analyze_phrase,
)


class TestWordValue:
    """Tests for word_value function."""

    def test_pythagorean_simple(self):
        """Test Pythagorean value for simple word."""
        result = word_value("abc", "pythagorean")
        assert result == 1 + 2 + 3  # a=1, b=2, c=3

    def test_pythagorean_default(self):
        """Test default system is Pythagorean."""
        result = word_value("abc")
        assert result == 6

    def test_ordinal_simple(self):
        """Test ordinal value for simple word."""
        result = word_value("abc", "ordinal")
        assert result == 1 + 2 + 3  # a=1, b=2, c=3

    def test_empty_string(self):
        """Test value of empty string."""
        result = word_value("")
        assert result == 0


class TestReduceToRoot:
    """Tests for reduce_to_root function."""

    def test_single_digit(self):
        """Test reduction of single digit."""
        assert reduce_to_root(5) == 5

    def test_two_digits(self):
        """Test reduction of two-digit number."""
        assert reduce_to_root(15) == 6  # 1+5=6

    def test_multiple_reductions(self):
        """Test number requiring multiple reductions."""
        assert reduce_to_root(999) == 9  # 9+9+9=27, 2+7=9

    def test_zero(self):
        """Test reduction of zero."""
        assert reduce_to_root(0) == 0


class TestNormalizeToZeroOverZero:
    """Tests for normalize_to_zero_over_zero function."""

    def test_zero_input(self):
        """Test normalization of zero."""
        result = normalize_to_zero_over_zero(0)
        assert result == 0.0

    def test_positive_input(self):
        """Test normalization of positive number."""
        result = normalize_to_zero_over_zero(9)
        assert result == 1.0  # root 9 / 9 = 1.0

    def test_range(self):
        """Test normalized values are in [0, 1] range."""
        for i in range(1, 100):
            result = normalize_to_zero_over_zero(i)
            assert 0.0 <= result <= 1.0


class TestGetSymbolicMeaning:
    """Tests for get_symbolic_meaning function."""

    def test_unity(self):
        """Test symbolic meaning for 1."""
        result = get_symbolic_meaning(1)
        assert result["root"] == 1
        assert "Unity" in result["archetype"]

    def test_zero(self):
        """Test symbolic meaning for 0."""
        result = get_symbolic_meaning(0)
        assert result["root"] == 0
        assert "Void" in result["archetype"] or "Potential" in result["archetype"]

    def test_nine(self):
        """Test symbolic meaning for 9."""
        result = get_symbolic_meaning(9)
        assert result["root"] == 9
        assert "Completion" in result["archetype"] or "Universal" in result["archetype"]


class TestAnalyzeWord:
    """Tests for analyze_word function."""

    def test_simple_word(self):
        """Test complete analysis of simple word."""
        result = analyze_word("sun")
        assert result["word"] == "sun"
        assert "pythagorean_value" in result
        assert "pythagorean_root" in result
        assert "symbolic_meaning" in result
        assert 1 <= result["pythagorean_root"] <= 9


class TestAnalyzePhrase:
    """Tests for analyze_phrase function."""

    def test_simple_phrase(self):
        """Test complete analysis of phrase."""
        result = analyze_phrase("fire water")
        assert result["phrase"] == "fire water"
        assert len(result["word_analyses"]) == 2
        assert "total_value" in result
        assert "phrase_meaning" in result
