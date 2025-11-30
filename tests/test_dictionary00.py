"""
Tests for the dictionary00 module.
"""

import pytest
from ute00.dictionary00.roots import UniversalRoots, UniversalRoot
from ute00.dictionary00.matcher import RootMatcher


class TestUniversalRoots:
    """Tests for UniversalRoots."""

    def test_init(self):
        """Test roots initialization."""
        roots = UniversalRoots()
        assert roots is not None
        assert roots.total_roots > 0

    def test_get_root(self):
        """Test getting a root by ID."""
        roots = UniversalRoots()
        root = roots.get_root(1)
        assert root is not None
        assert root.root_id == 1

    def test_get_root_by_meaning(self):
        """Test getting root by meaning."""
        roots = UniversalRoots()
        root = roots.get_root_by_meaning("water")
        assert root is not None
        assert "water" in root.meaning

    def test_get_roots_by_field(self):
        """Test getting roots by semantic field."""
        roots = UniversalRoots()
        field_roots = roots.get_roots_by_field("element")
        assert len(field_roots) > 0

    def test_search_by_language(self):
        """Test searching by language."""
        roots = UniversalRoots()
        sanskrit_roots = roots.search_by_language("Sanskrit")
        assert len(sanskrit_roots) > 0


class TestRootMatcher:
    """Tests for RootMatcher."""

    def test_init(self):
        """Test matcher initialization."""
        matcher = RootMatcher()
        assert matcher is not None

    def test_match_word(self):
        """Test word matching."""
        matcher = RootMatcher()
        matches = matcher.match_word("water")
        assert len(matches) > 0
        assert matches[0].similarity_score > 0

    def test_find_by_meaning(self):
        """Test finding by meaning."""
        matcher = RootMatcher()
        root = matcher.find_by_meaning("mother")
        assert root is not None
        assert root.meaning == "mother"

    def test_analyze_etymology(self):
        """Test etymology analysis."""
        matcher = RootMatcher()
        results = matcher.analyze_etymology("water")
        assert len(results) > 0
