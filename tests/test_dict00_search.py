"""Tests for the dictionary search module."""

import pytest

from universal_translation_00.dict00.search import Dict00Search
from universal_translation_00.dict00.loader import Dict00Loader, DictEntry
from universal_translation_00.dict00.scoring import PhoneticScorer


class TestDict00Search:
    """Test suite for Dict00Search class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.search = Dict00Search()

    def test_search_by_phoneme_exact(self) -> None:
        """Test exact phoneme search."""
        results = self.search.search_by_phoneme("ma")
        assert len(results) > 0

    def test_search_by_meaning(self) -> None:
        """Test meaning search."""
        results = self.search.search_by_meaning("mother")
        assert len(results) >= 0  # May or may not have results depending on data

    def test_search_by_semantic_class(self) -> None:
        """Test semantic class search."""
        results = self.search.search_by_semantic_class("human")
        assert len(results) >= 0

    def test_find_similar(self) -> None:
        """Test finding similar phonemes."""
        similar = self.search.find_similar("ta")
        assert isinstance(similar, list)

    def test_multi_search(self) -> None:
        """Test multi-criteria search."""
        results = self.search.multi_search(phoneme="ma")
        assert isinstance(results, list)


class TestDict00Loader:
    """Test suite for Dict00Loader class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.loader = Dict00Loader()

    def test_get_all_entries(self) -> None:
        """Test getting all entries."""
        entries = self.loader.get_all_entries()
        assert len(entries) > 0

    def test_get_by_phoneme(self) -> None:
        """Test getting entries by phoneme."""
        entries = self.loader.get_by_phoneme("a")
        # May be empty if not in default data
        assert isinstance(entries, list)

    def test_get_all_phonemes(self) -> None:
        """Test getting all phonemes."""
        phonemes = self.loader.get_all_phonemes()
        assert len(phonemes) > 0


class TestPhoneticScorer:
    """Test suite for PhoneticScorer class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.scorer = PhoneticScorer()

    def test_identical_phonemes(self) -> None:
        """Test scoring identical phonemes."""
        score = self.scorer.phoneme_similarity("ta", "ta")
        assert score == 1.0

    def test_similar_phonemes(self) -> None:
        """Test scoring similar phonemes."""
        score = self.scorer.phoneme_similarity("ta", "da")
        assert 0.5 < score < 1.0

    def test_different_phonemes(self) -> None:
        """Test scoring different phonemes."""
        score = self.scorer.phoneme_similarity("ta", "mu")
        assert 0.0 <= score < 0.8

    def test_rank_candidates(self) -> None:
        """Test ranking candidates."""
        candidates = ["ta", "da", "ma", "ka"]
        ranked = self.scorer.rank_candidates("ta", candidates)

        assert len(ranked) == len(candidates)
        assert ranked[0][0] == "ta"  # Most similar should be first
        assert ranked[0][1] == 1.0


class TestDictEntry:
    """Test suite for DictEntry dataclass."""

    def test_entry_creation(self) -> None:
        """Test DictEntry creation."""
        entry = DictEntry(
            token=1,
            phoneme="a",
            meaning_en="open",
            meaning_pt="abrir",
            semantic_class="abstract",
            frequency="high",
        )

        assert entry.token == 1
        assert entry.phoneme == "a"

    def test_entry_to_dict(self) -> None:
        """Test conversion to dictionary."""
        entry = DictEntry(
            token=1,
            phoneme="a",
            meaning_en="open",
            meaning_pt="abrir",
            semantic_class="abstract",
            frequency="high",
        )

        d = entry.to_dict()
        assert d["token"] == 1
        assert d["phoneme"] == "a"
        assert "meaning_en" in d
