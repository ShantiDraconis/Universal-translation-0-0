"""
Tests for ExtendedReal class - Core mathematical engine for I = 0/0
"""

import pytest
from universal_translation_00.core.extended_real import (
    ExtendedReal,
    create_indeterminate,
    create_numeric,
)


class TestExtendedReal:
    """Test suite for ExtendedReal class."""
    
    def test_create_numeric_value(self):
        """Test creating ExtendedReal with numeric values."""
        er = ExtendedReal(42)
        assert er.value == 42
        assert not er.is_indeterminate
    
    def test_create_indeterminate_with_i(self):
        """Test creating indeterminate value with 'I'."""
        er = ExtendedReal('I')
        assert er.is_indeterminate
        assert er.value == "ᛃ(I/0)"
    
    def test_create_indeterminate_with_zero_over_zero(self):
        """Test creating indeterminate with '0/0' string."""
        er = ExtendedReal('0/0')
        assert er.is_indeterminate
        assert er.value == "ᛃ(I/0)"
    
    def test_sync_default_channels(self):
        """Test sync method returns 54 channels by default."""
        er = ExtendedReal(0)
        channels = er.sync()
        assert len(channels) == 54
        assert channels == list(range(54))
    
    def test_sync_custom_channels(self):
        """Test sync with custom channel count."""
        er = ExtendedReal(0)
        channels = er.sync(10)
        assert len(channels) == 10
        assert channels == list(range(10))
    
    def test_string_representation_numeric(self):
        """Test string representation of numeric value."""
        er = ExtendedReal(3.14)
        assert "3.14" in str(er)
    
    def test_string_representation_indeterminate(self):
        """Test string representation of indeterminate value."""
        er = ExtendedReal('I')
        assert "I (0/0)" in str(er) or "Indeterminate" in str(er)
    
    def test_repr_numeric(self):
        """Test repr of numeric value."""
        er = ExtendedReal(42)
        assert "ExtendedReal(42)" == repr(er)
    
    def test_repr_indeterminate(self):
        """Test repr of indeterminate value."""
        er = ExtendedReal('I')
        assert "I=0/0" in repr(er)
    
    def test_equality_numeric(self):
        """Test equality for numeric values."""
        er1 = ExtendedReal(5)
        er2 = ExtendedReal(5)
        er3 = ExtendedReal(10)
        
        assert er1 == er2
        assert er1 != er3
    
    def test_equality_indeterminate(self):
        """Test equality for indeterminate values."""
        er1 = ExtendedReal('I')
        er2 = ExtendedReal('0/0')
        
        assert er1 == er2  # Both indeterminate
    
    def test_equality_mixed(self):
        """Test equality between numeric and indeterminate."""
        er1 = ExtendedReal(5)
        er2 = ExtendedReal('I')
        
        assert er1 != er2
    
    def test_addition_numeric(self):
        """Test addition of numeric values."""
        er1 = ExtendedReal(3)
        er2 = ExtendedReal(4)
        result = er1 + er2
        
        assert result.value == 7
        assert not result.is_indeterminate
    
    def test_addition_with_indeterminate(self):
        """Test that adding indeterminate yields indeterminate."""
        er1 = ExtendedReal(5)
        er2 = ExtendedReal('I')
        result = er1 + er2
        
        assert result.is_indeterminate
    
    def test_addition_with_scalar(self):
        """Test addition with Python scalar."""
        er = ExtendedReal(5)
        result = er + 3
        
        assert result.value == 8
        assert not result.is_indeterminate
    
    def test_multiplication_numeric(self):
        """Test multiplication of numeric values."""
        er1 = ExtendedReal(3)
        er2 = ExtendedReal(4)
        result = er1 * er2
        
        assert result.value == 12
        assert not result.is_indeterminate
    
    def test_multiplication_with_indeterminate(self):
        """Test that multiplying by indeterminate yields indeterminate."""
        er1 = ExtendedReal(5)
        er2 = ExtendedReal('I')
        result = er1 * er2
        
        assert result.is_indeterminate
    
    def test_multiplication_with_scalar(self):
        """Test multiplication with Python scalar."""
        er = ExtendedReal(5)
        result = er * 3
        
        assert result.value == 15
        assert not result.is_indeterminate
    
    def test_to_numeric_with_value(self):
        """Test converting to numeric value."""
        er = ExtendedReal(42.5)
        numeric = er.to_numeric()
        
        assert numeric == 42.5
        assert isinstance(numeric, float)
    
    def test_to_numeric_indeterminate_default(self):
        """Test converting indeterminate to numeric with default."""
        er = ExtendedReal('I')
        numeric = er.to_numeric()
        
        assert numeric == 0.0
    
    def test_to_numeric_indeterminate_custom_default(self):
        """Test converting indeterminate to numeric with custom default."""
        er = ExtendedReal('I')
        numeric = er.to_numeric(default=99.9)
        
        assert numeric == 99.9
    
    def test_factory_create_indeterminate(self):
        """Test factory function for creating indeterminate."""
        er = create_indeterminate()
        
        assert er.is_indeterminate
        assert er.value == "ᛃ(I/0)"
    
    def test_factory_create_numeric(self):
        """Test factory function for creating numeric."""
        er = create_numeric(123)
        
        assert er.value == 123
        assert not er.is_indeterminate
    
    def test_default_value_is_zero(self):
        """Test that default value is 0."""
        er = ExtendedReal()
        assert er.value == 0
        assert not er.is_indeterminate
    
    def test_indeterminate_propagation(self):
        """Test that indeterminate propagates through operations."""
        er_i = ExtendedReal('I')
        er_n = ExtendedReal(10)
        
        # Addition
        result1 = er_i + er_n
        assert result1.is_indeterminate
        
        # Multiplication
        result2 = er_i * er_n
        assert result2.is_indeterminate
        
        # Chained operations
        result3 = (er_i + er_n) * ExtendedReal(5)
        assert result3.is_indeterminate
