"""Tests for the phoneme segmenter module."""

import pytest

from universal_translation_00.core.phoneme_segmenter import PhonemeSegmenter, Phoneme


class TestPhonemeSegmenter:
    """Test suite for PhonemeSegmenter class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.segmenter = PhonemeSegmenter()

    def test_segment_cv_syllable(self) -> None:
        """Test segmentation of CV syllables."""
        phonemes = self.segmenter.segment("ka")
        assert len(phonemes) == 1
        assert phonemes[0].value == "ka"

    def test_segment_multiple_syllables(self) -> None:
        """Test segmentation of multiple syllables."""
        phonemes = self.segmenter.segment("tama")
        assert len(phonemes) == 2
        assert phonemes[0].value == "ta"
        assert phonemes[1].value == "ma"

    def test_segment_cvc_ritual(self) -> None:
        """Test segmentation of CVC ritual patterns."""
        phonemes = self.segmenter.segment("tak")
        assert len(phonemes) == 1
        assert phonemes[0].value == "tak"
        assert phonemes[0].phoneme_class == "cvc_ritual"

    def test_segment_vowels(self) -> None:
        """Test segmentation of standalone vowels."""
        phonemes = self.segmenter.segment("a")
        assert len(phonemes) == 1
        assert phonemes[0].value == "a"
        assert phonemes[0].phoneme_class == "vowel"

    def test_is_vowel(self) -> None:
        """Test vowel detection."""
        assert self.segmenter.is_vowel("a") is True
        assert self.segmenter.is_vowel("e") is True
        assert self.segmenter.is_vowel("k") is False

    def test_is_consonant(self) -> None:
        """Test consonant detection."""
        assert self.segmenter.is_consonant("k") is True
        assert self.segmenter.is_consonant("t") is True
        assert self.segmenter.is_consonant("a") is False

    def test_get_syllables(self) -> None:
        """Test getting syllable-level phonemes."""
        syllables = self.segmenter.get_syllables("tamanaka")
        assert "ta" in syllables
        assert "ma" in syllables
        assert "na" in syllables
        assert "ka" in syllables

    def test_count_phonemes(self) -> None:
        """Test phoneme counting."""
        counts = self.segmenter.count_phonemes("tatata")
        assert counts["ta"] == 3

    def test_segment_complex_word(self) -> None:
        """Test segmentation of complex words."""
        phonemes = self.segmenter.segment("harapan")
        values = [p.value for p in phonemes]
        assert "ha" in values
        assert "ra" in values
        assert "pa" in values

    def test_segment_empty_string(self) -> None:
        """Test segmentation of empty string."""
        phonemes = self.segmenter.segment("")
        assert phonemes == []

    def test_segment_cvv_human(self) -> None:
        """Test segmentation of CVV human patterns."""
        phonemes = self.segmenter.segment("ama")
        assert len(phonemes) == 1
        assert phonemes[0].value == "ama"
        assert phonemes[0].phoneme_class == "cvv_human"


class TestPhoneme:
    """Test suite for Phoneme dataclass."""

    def test_phoneme_creation(self) -> None:
        """Test Phoneme creation."""
        phoneme = Phoneme(
            value="ta",
            position=0,
            source_text="ta",
            phoneme_class="cv_t",
        )

        assert phoneme.value == "ta"
        assert phoneme.position == 0
        assert phoneme.phoneme_class == "cv_t"

    def test_phoneme_repr(self) -> None:
        """Test Phoneme string representation."""
        phoneme = Phoneme(
            value="ka",
            position=0,
            source_text="ka",
            phoneme_class="cv_k",
        )

        repr_str = repr(phoneme)
        assert "ka" in repr_str
        assert "cv_k" in repr_str
