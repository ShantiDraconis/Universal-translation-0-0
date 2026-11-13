"""
Tests for the harappan_engine module.
"""

import pytest
from universal_translation.core.harappan_engine import (
    decode_sequence,
    encode_sequence,
    get_sign_category,
    get_universal_code,
    decode_to_universal,
)


class TestDecodeSequence:
    """Tests for decode_sequence function."""

    def test_simple_sequence(self):
        """Test decoding simple sequence."""
        result = decode_sequence([1, 8, 15])
        assert "SIGN_1" in result
        assert "SIGN_8" in result
        assert "SIGN_15" in result

    def test_empty_sequence(self):
        """Test decoding empty sequence."""
        result = decode_sequence([])
        assert result == ""

    def test_single_sign(self):
        """Test decoding single sign."""
        result = decode_sequence([42])
        assert result == "SIGN_42"


class TestEncodeSequence:
    """Tests for encode_sequence function."""

    def test_simple_encoding(self):
        """Test encoding simple symbolic string."""
        result = encode_sequence("SIGN_1 SIGN_8 SIGN_15")
        assert result == [1, 8, 15]

    def test_empty_string(self):
        """Test encoding empty string."""
        result = encode_sequence("")
        assert result == []

    def test_no_signs(self):
        """Test encoding string with no signs."""
        result = encode_sequence("hello world")
        assert result == []


class TestGetSignCategory:
    """Tests for get_sign_category function."""

    def test_anthropomorphic(self):
        """Test category for anthropomorphic signs (1-7)."""
        assert get_sign_category(1) == "Anthropomorphic"
        assert get_sign_category(7) == "Anthropomorphic"

    def test_zoomorphic(self):
        """Test category for zoomorphic signs (8-23)."""
        assert get_sign_category(8) == "Zoomorphic"
        assert get_sign_category(23) == "Zoomorphic"

    def test_numerals(self):
        """Test category for numeral signs (41-50)."""
        assert get_sign_category(41) == "Numerals"
        assert get_sign_category(50) == "Numerals"

    def test_markers(self):
        """Test category for marker sign (417)."""
        assert get_sign_category(417) == "Markers"

    def test_unknown(self):
        """Test category for out-of-range sign."""
        assert get_sign_category(999) == "Unknown"


class TestGetUniversalCode:
    """Tests for get_universal_code function."""

    def test_anthropomorphic_code(self):
        """Test universal code for anthropomorphic sign."""
        result = get_universal_code(1)
        assert result == "00-HUM-001"

    def test_zoomorphic_code(self):
        """Test universal code for zoomorphic sign."""
        result = get_universal_code(8)
        assert result == "00-ANI-008"

    def test_code_format(self):
        """Test code format with zero-padding."""
        result = get_universal_code(42)
        assert result.startswith("00-")
        assert "-042" in result


class TestDecodeToUniversal:
    """Tests for decode_to_universal function."""

    def test_simple_decode(self):
        """Test full decoding to universal format."""
        result = decode_to_universal([1, 8])
        assert len(result) == 2
        assert result[0]["mahadevan_id"] == 1
        assert result[0]["universal_code"] == "00-HUM-001"
        assert result[1]["mahadevan_id"] == 8
        assert result[1]["category"] == "Zoomorphic"

    def test_empty_list(self):
        """Test decoding empty list."""
        result = decode_to_universal([])
        assert result == []
