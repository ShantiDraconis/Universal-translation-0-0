"""Tests for the Harappan mapping module."""

import pytest

from universal_translation_00.harappan.mapping import HarappanMapping, HarappanSign


class TestHarappanMapping:
    """Test suite for HarappanMapping class."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mapping = HarappanMapping()

    def test_get_sign_by_id(self) -> None:
        """Test getting a sign by ID."""
        sign = self.mapping.get_sign("H001")
        assert sign is not None
        assert sign.id == "H001"
        assert sign.group == "NUM"

    def test_get_sign_numeric_id(self) -> None:
        """Test getting a sign by numeric ID."""
        sign = self.mapping.get_sign("1")
        assert sign is not None
        assert sign.id == "H001"

    def test_phoneme_to_sign(self) -> None:
        """Test mapping phoneme to sign."""
        sign = self.mapping.phoneme_to_sign("ta")
        assert sign is not None
        assert sign.phoneme == "ta"

    def test_phoneme_to_signs_multiple(self) -> None:
        """Test getting all signs for a phoneme."""
        signs = self.mapping.phoneme_to_signs("ta")
        assert len(signs) > 0
        assert all(s.phoneme == "ta" for s in signs)

    def test_get_signs_by_group(self) -> None:
        """Test getting signs by group."""
        signs = self.mapping.get_signs_by_group("NUM")
        assert len(signs) > 0
        assert all(s.group == "NUM" for s in signs)

    def test_get_all_signs(self) -> None:
        """Test getting all signs."""
        signs = self.mapping.get_all_signs()
        assert len(signs) == 417

    def test_get_all_phonemes(self) -> None:
        """Test getting all unique phonemes."""
        phonemes = self.mapping.get_all_phonemes()
        assert len(phonemes) > 0
        assert "ta" in phonemes
        assert "ma" in phonemes

    def test_get_all_groups(self) -> None:
        """Test getting all groups."""
        groups = self.mapping.get_all_groups()
        assert "NUM" in groups
        assert "CON" in groups
        assert "HUM" in groups

    def test_search_by_semantic_field(self) -> None:
        """Test searching by semantic field."""
        signs = self.mapping.search_by_semantic_field("counting")
        assert len(signs) > 0

    def test_get_statistics(self) -> None:
        """Test getting statistics."""
        stats = self.mapping.get_statistics()
        assert stats["total_signs"] == 417
        assert "unique_phonemes" in stats
        assert "groups" in stats

    def test_sign_not_found(self) -> None:
        """Test behavior when sign is not found."""
        sign = self.mapping.get_sign("H999")
        assert sign is None

    def test_phoneme_not_found(self) -> None:
        """Test behavior when phoneme is not found."""
        sign = self.mapping.phoneme_to_sign("xyz")
        assert sign is None


class TestHarappanSign:
    """Test suite for HarappanSign dataclass."""

    def test_sign_creation(self) -> None:
        """Test HarappanSign creation."""
        sign = HarappanSign(
            id="H001",
            group="NUM",
            group_full="NUM_TALLY",
            phoneme="ta",
            semantic_field="counting",
            tamil_root="taṭṭu",
            chinese_root="打",
            norse_root="tala",
            latin_root="tactus",
            tupi_root="ta",
            description="Single stroke",
        )

        assert sign.id == "H001"
        assert sign.phoneme == "ta"

    def test_sign_to_dict(self) -> None:
        """Test conversion to dictionary."""
        sign = HarappanSign(
            id="H001",
            group="NUM",
            group_full="NUM_TALLY",
            phoneme="ta",
            semantic_field="counting",
            tamil_root="taṭṭu",
            chinese_root="打",
            norse_root="tala",
            latin_root="tactus",
            tupi_root="ta",
            description="Single stroke",
        )

        d = sign.to_dict()
        assert d["id"] == "H001"
        assert d["phoneme"] == "ta"
        assert "tamil_root" in d

    def test_sign_get_cognates(self) -> None:
        """Test getting cognates."""
        sign = HarappanSign(
            id="H001",
            group="NUM",
            group_full="NUM_TALLY",
            phoneme="ta",
            semantic_field="counting",
            tamil_root="taṭṭu",
            chinese_root="打",
            norse_root="tala",
            latin_root="tactus",
            tupi_root="ta",
            description="Single stroke",
        )

        cognates = sign.get_cognates()
        assert cognates["tamil"] == "taṭṭu"
        assert cognates["chinese"] == "打"
