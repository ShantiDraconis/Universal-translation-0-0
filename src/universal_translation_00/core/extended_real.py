"""
[𓏟] MUNDOKABARA_CORE_ENGINE
ᚦᛖ ᛖᛊᛏᛖᚾᛞᛖᛞ ᚱᛖᛄᛚ ᛁᛗᛈᛚᛖᛗᛖᚾᛏᛄᛏᛁᛟᚾ

ExtendedReal - Core mathematical engine that handles I = 0/0 indeterminacy.
This prevents system collapse when division by zero (chaos of Cádiz) occurs.
"""

from typing import Any, List, Optional, Union


class ExtendedReal:
    """
    [𓀠] ExtendedReal - The Logos
    
    Implements the mathematical operator I = 0/0, representing the indeterminate
    nucleus from which all units emerge—the "collapse point" between language,
    consciousness, body, and cosmos.
    
    Attributes:
        value: The stored value (can be numeric or 'I' for indeterminate)
        is_indeterminate: Boolean flag indicating if this represents I = 0/0
    """
    
    def __init__(self, value: Union[int, float, str, None] = None):
        """
        Initialize an ExtendedReal number.
        
        Args:
            value: The value to store. Can be:
                - A numeric value (int/float)
                - The string 'I' to represent I = 0/0
                - None (defaults to 0)
        """
        # [𓍢] Check for Indeterminacy
        if value == 'I' or self._is_zero_divided_by_zero(value):
            self.is_indeterminate = True
            self.value = "ᛃ(I/0)"  # Jera rune - cycle/harvest
        else:
            self.is_indeterminate = False
            self.value = value if value is not None else 0
    
    def _is_zero_divided_by_zero(self, value: Any) -> bool:
        """
        Check if a value represents 0/0 mathematically.
        
        Args:
            value: Value to check
            
        Returns:
            True if value represents 0/0, False otherwise
        """
        # In practice, we can't actually compute 0/0, so we look for the string
        # or explicitly handle the 'I' symbol
        return isinstance(value, str) and value in ('0/0', 'I', 'i')
    
    def sync(self, channels: int = 54) -> List[int]:
        """
        [𓋹] Synchronize with the 54 channels
        ᛊᚤᚾᚳᚺᚱᛟᚾᛁᛉᛖ ᚹᛁᚦ ᚦᛖ 54 ᚳᚺᛄᚾᚾᛖᛚᛊ
        
        Creates a synchronization array representing the 54 channels
        of the Mund-O-Ka-Ba-Ra system.
        
        Args:
            channels: Number of channels to sync (default: 54)
            
        Returns:
            List of channel indices [0..53]
        """
        # [𓄹] Generate channel array
        return list(range(channels))
    
    def __repr__(self) -> str:
        """String representation of ExtendedReal."""
        if self.is_indeterminate:
            return f"ExtendedReal(I=0/0: {self.value})"
        return f"ExtendedReal({self.value})"
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        if self.is_indeterminate:
            return f"I (0/0) - Indeterminate"
        return str(self.value)
    
    def __eq__(self, other) -> bool:
        """Equality comparison."""
        if isinstance(other, ExtendedReal):
            if self.is_indeterminate and other.is_indeterminate:
                return True
            if self.is_indeterminate or other.is_indeterminate:
                return False
            return self.value == other.value
        return False
    
    def __add__(self, other: Union['ExtendedReal', int, float]) -> 'ExtendedReal':
        """Addition operation."""
        if self.is_indeterminate:
            return ExtendedReal('I')
        
        if isinstance(other, ExtendedReal):
            if other.is_indeterminate:
                return ExtendedReal('I')
            return ExtendedReal(self.value + other.value)
        
        return ExtendedReal(self.value + other)
    
    def __mul__(self, other: Union['ExtendedReal', int, float]) -> 'ExtendedReal':
        """Multiplication operation."""
        if self.is_indeterminate:
            return ExtendedReal('I')
        
        if isinstance(other, ExtendedReal):
            if other.is_indeterminate:
                return ExtendedReal('I')
            return ExtendedReal(self.value * other.value)
        
        return ExtendedReal(self.value * other)
    
    def to_numeric(self, default: float = 0.0) -> float:
        """
        Convert to numeric value.
        
        Args:
            default: Default value to return if indeterminate
            
        Returns:
            Numeric value or default if indeterminate
        """
        if self.is_indeterminate:
            return default
        
        try:
            return float(self.value)
        except (ValueError, TypeError):
            return default


# [𓉐] ᚦᛖ-ᛒᚢᛁᛚᛞᛁᚾᚷ-ᛒᛚᛟᚳᚳᛊ
# The Building Blocks - Factory functions

def create_indeterminate() -> ExtendedReal:
    """
    Create an indeterminate ExtendedReal representing I = 0/0.
    
    Returns:
        ExtendedReal instance representing indeterminacy
    """
    return ExtendedReal('I')


def create_numeric(value: Union[int, float]) -> ExtendedReal:
    """
    Create a numeric ExtendedReal.
    
    Args:
        value: Numeric value to wrap
        
    Returns:
        ExtendedReal instance with numeric value
    """
    return ExtendedReal(value)
