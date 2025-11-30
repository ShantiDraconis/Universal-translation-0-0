"""
Tests for the phonetics module.
"""

import pytest
from ute00.phonetics.analyzer import PhoneticAnalyzer, PhonemeMapping
from ute00.phonetics.segmenter import PhoneticSegmenter


class TestPhoneticAnalyzer:
    """Tests for PhoneticAnalyzer."""

    def test_init(self):
        """Test analyzer initialization."""
        analyzer = PhoneticAnalyzer()
        assert analyzer is not None

    def test_analyze_simple(self):
        """Test basic phoneme analysis."""
        analyzer = PhoneticAnalyzer()
        result = analyzer.analyze("hello")
        assert len(result) == 5
        assert all(isinstance(m, PhonemeMapping) for m in result)

    def test_analyze_with_spaces(self):
        """Test analysis ignores non-phonemes."""
        analyzer = PhoneticAnalyzer()
        result = analyzer.analyze("hello world")
        # Should have phonemes for h-e-l-l-o-w-o-r-l-d (10 chars)
        assert len(result) == 10

    def test_get_phoneme_mapping(self):
        """Test getting individual phoneme mapping."""
        analyzer = PhoneticAnalyzer()
        mapping = analyzer.get_phoneme_mapping("a")
        assert mapping is not None
        assert mapping.phoneme == "a"
        assert mapping.real == 1.0

    def test_calculate_phi(self):
        """Test Φ(f) calculation."""
        analyzer = PhoneticAnalyzer()
        phi = analyzer.calculate_phi("a")
        assert phi is not None
        assert phi == (1.0, 0.5, 1)

    def test_total_vibration(self):
        """Test total vibration calculation."""
        analyzer = PhoneticAnalyzer()
        vibration = analyzer.get_total_vibration("ab")
        # a=1.0, b=6.0
        assert vibration == 7.0


class TestPhoneticSegmenter:
    """Tests for PhoneticSegmenter."""

    def test_init(self):
        """Test segmenter initialization."""
        segmenter = PhoneticSegmenter()
        assert segmenter is not None

    def test_segment(self):
        """Test full segmentation."""
        segmenter = PhoneticSegmenter()
        result = segmenter.segment("hello")
        assert result.original == "hello"
        assert result.horizontal_inversion == "olleh"
        assert len(result.phonemes) == 5

    def test_horizontal_inversion(self):
        """Test Da Vinci horizontal inversion."""
        segmenter = PhoneticSegmenter()
        result = segmenter.horizontal_inversion("water")
        assert result == "retaw"

    def test_vertical_inversion(self):
        """Test vertical character inversion."""
        segmenter = PhoneticSegmenter()
        result = segmenter.vertical_inversion("ab")
        assert "ɐ" in result  # 'a' -> 'ɐ'

    def test_extract_phonemes(self):
        """Test phoneme extraction."""
        segmenter = PhoneticSegmenter()
        phonemes = segmenter.extract_phonemes("Hello World")
        assert phonemes == ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]

    def test_extract_nuclear_vowels(self):
        """Test nuclear vowel extraction."""
        segmenter = PhoneticSegmenter()
        vowels = segmenter.extract_nuclear_vowels("hello")
        assert vowels == ["e", "o"]
