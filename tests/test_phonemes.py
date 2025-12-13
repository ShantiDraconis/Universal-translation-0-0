"""
Tests for the phoneme_engine module.
"""

import pytest
from universal_translation.core.phoneme_engine import (
    to_universal_phonemes,
    text_to_ipa,
    detect_family,
    get_phoneme_features,
)


class TestToUniversalPhonemes:
    """Tests for to_universal_phonemes function."""

    def test_simple_tokens(self):
        """Test phoneme conversion of simple tokens."""
        result = to_universal_phonemes(["hello", "world"])
        assert len(result) == 2
        assert result[0]["token"] == "hello"
        assert result[1]["token"] == "world"
        assert "ipa" in result[0]
        assert "family" in result[0]

    def test_empty_list(self):
        """Test phoneme conversion of empty list."""
        result = to_universal_phonemes([])
        assert result == []

    def test_single_token(self):
        """Test phoneme conversion of single token."""
        result = to_universal_phonemes(["sun"])
        assert len(result) == 1
        assert result[0]["token"] == "sun"


class TestTextToIpa:
    """Tests for text_to_ipa function."""

    def test_simple_word(self):
        """Test IPA conversion of simple word."""
        result = text_to_ipa("cat")
        assert "k" in result  # 'c' maps to 'k'
        assert "a" in result
        assert "t" in result

    def test_digraph_sh(self):
        """Test IPA conversion of 'sh' digraph."""
        result = text_to_ipa("ship")
        assert "ʃ" in result  # sh -> ʃ

    def test_empty_string(self):
        """Test IPA conversion of empty string."""
        result = text_to_ipa("")
        assert result == ""

    def test_uppercase(self):
        """Test IPA conversion handles uppercase."""
        result = text_to_ipa("HELLO")
        result_lower = text_to_ipa("hello")
        assert result == result_lower


class TestDetectFamily:
    """Tests for detect_family function."""

    def test_indo_european(self):
        """Test detection of Indo-European patterns."""
        result = detect_family("the")
        assert result == "indo_european"

    def test_tupi_nasal_vowels(self):
        """Test detection of Tupi patterns via nasal vowels."""
        result = detect_family("pirã")
        assert result == "tupi_guarani"

    def test_unknown(self):
        """Test unknown family for generic words."""
        result = detect_family("xyz123")
        assert result == "unknown"


class TestGetPhonemeFeatures:
    """Tests for get_phoneme_features function."""

    def test_vowel(self):
        """Test features for vowel."""
        result = get_phoneme_features("a")
        assert result["is_vowel"] is True
        assert result["is_consonant"] is False

    def test_nasal(self):
        """Test features for nasal consonant."""
        result = get_phoneme_features("m")
        assert result["is_nasal"] is True

    def test_plosive(self):
        """Test features for plosive consonant."""
        result = get_phoneme_features("p")
        assert result["is_plosive"] is True
