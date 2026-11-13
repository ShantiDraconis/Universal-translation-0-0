"""
Tests for the harappan module.
"""

from ute00.harappan.signs import HarappanSignSystem, HarappanSign
from ute00.harappan.mapper import HarappanMapper


class TestHarappanSignSystem:
    """Tests for HarappanSignSystem."""

    def test_init(self):
        """Test sign system initialization."""
        system = HarappanSignSystem()
        assert system is not None
        assert system.total_signs > 0

    def test_get_sign(self):
        """Test getting a sign by ID."""
        system = HarappanSignSystem()
        sign = system.get_sign(1)
        assert sign is not None
        assert sign.sign_id == 1

    def test_get_signs_by_category(self):
        """Test getting signs by category."""
        system = HarappanSignSystem()
        signs = system.get_signs_by_category("zoomorphic")
        assert len(signs) > 0
        assert all(s.category == "zoomorphic" for s in signs)

    def test_get_all_categories(self):
        """Test getting all categories."""
        system = HarappanSignSystem()
        categories = system.get_all_categories()
        assert "zoomorphic" in categories
        assert "geometric" in categories


class TestHarappanMapper:
    """Tests for HarappanMapper."""

    def test_init(self):
        """Test mapper initialization."""
        mapper = HarappanMapper()
        assert mapper is not None

    def test_map_text(self):
        """Test text mapping."""
        mapper = HarappanMapper()
        result = mapper.map_text("water")
        assert result.original == "water"
        assert len(result.signs) > 0
        assert result.total_numeric_value > 0

    def test_map_phoneme(self):
        """Test single phoneme mapping."""
        mapper = HarappanMapper()
        sign = mapper.map_phoneme("a")
        assert sign is not None
        assert isinstance(sign, HarappanSign)

    def test_get_sign_sequence(self):
        """Test sign sequence generation."""
        mapper = HarappanMapper()
        sequence = mapper.get_sign_sequence("ab")
        assert len(sequence) == 2
