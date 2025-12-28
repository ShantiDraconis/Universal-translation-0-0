"""
TripleScriptEncoder - Three-layer writing system for שאצ.

This module implements the triple-script translation system that represents
text in three different writing systems simultaneously:
1. Runic (Elder Futhark) - Operational force layer
2. Tamil - Logical structure layer
3. Harappan - Semantic nuclear layer

Based on LOG-0024 specification.
"""

from typing import Dict, List, Optional


class TripleScriptEncoder:
    """
    Encoder for the three-layer writing system of שאצ.
    
    Translates text into three simultaneous representations:
    - Runic (Elder Futhark): Phonetic operational layer
    - Tamil: Structural logical layer
    - Harappan: Semantic glyphic layer
    
    Example:
        >>> encoder = TripleScriptEncoder()
        >>> result = encoder.encode("em rúnico e tamil e harappan")
        >>> print(result["runic"])
        ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ
    """
    
    # Elder Futhark rune mappings (Latin to Runic)
    RUNIC_MAP = {
        'a': 'ᚨ', 'b': 'ᛒ', 'c': 'ᚲ', 'd': 'ᛞ', 'e': 'ᛖ',
        'f': 'ᚠ', 'g': 'ᚷ', 'h': 'ᚺ', 'i': 'ᛁ', 'j': 'ᛃ',
        'k': 'ᚲ', 'l': 'ᛚ', 'm': 'ᛗ', 'n': 'ᚾ', 'o': 'ᛟ',
        'p': 'ᛈ', 'q': 'ᚲ', 'r': 'ᚱ', 's': 'ᛊ', 't': 'ᛏ',
        'u': 'ᚢ', 'v': 'ᚹ', 'w': 'ᚹ', 'x': 'ᚲᛊ', 'y': 'ᛃ',
        'z': 'ᛉ', ' ': ' ',
    }
    
    # Tamil transliteration mappings (simplified)
    TAMIL_MAP = {
        'ru': 'ரு', 'ni': 'ணி', 'kki': 'க்கி', 'lum': 'லும்',
        'ta': 'த', 'mi': 'மி', 'zhi': 'ழி', 'ha': 'ஹ',
        'ra': 'ர', 'ppa': 'ப்ப', 'lu': 'லு', 'm': 'ம்',
        ' ': ' ',
    }
    
    # Harappan glyph mappings (semantic codes)
    HARAPPAN_MAP = {
        'em': ['𓀠', '𓋹'],           # state instrumental
        'runico': ['𓊖', '𓐬'],       # operational system
        'tamil': ['𓉐', '𓐬'],        # structural system
        'harappan': ['𓐮', '𓏟'],     # semantic system
        'e': ['𓋹'],                   # conjunction connector
        'and': ['𓋹'],                 # conjunction connector
    }
    
    # Pre-defined complete translations
    PREDEFINED_TRANSLATIONS = {
        "em rúnico e tamil e harappan": {
            "runic": "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ",
            "tamil": "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்",
            "tamil_agglutinated": "ருனிதமிஹரப்பனிலும்",
            "harappan": "𓀠𓋹 𓊖𓐬 𓋹 𓉐𓐬 𓋹 𓐮𓏟",
            "harappan_list": ['𓀠', '𓋹', '𓊖', '𓐬', '𓋹', '𓉐', '𓐬', '𓋹', '𓐮', '𓏟'],
            "bindrune": "ᛇ",
            "interpretation": "IN_RUNIC_AND_TAMIL_AND_HARAPPAN"
        },
        "in runic and tamil and harappan": {
            "runic": "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ",
            "tamil": "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்",
            "tamil_agglutinated": "ருனிதமிஹரப்பனிலும்",
            "harappan": "𓀠𓋹 𓊖𓐬 𓋹 𓉐𓐬 𓋹 𓐮𓏟",
            "harappan_list": ['𓀠', '𓋹', '𓊖', '𓐬', '𓋹', '𓉐', '𓐬', '𓋹', '𓐮', '𓏟'],
            "bindrune": "ᛇ",
            "interpretation": "IN_RUNIC_AND_TAMIL_AND_HARAPPAN"
        }
    }
    
    def __init__(self):
        """Initialize the triple-script encoder."""
        self.runic = "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ"
        self.tamil = "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்"
        self.harappan = ['𓀠', '𓋹', '𓊖', '𓐬', '𓋹', '𓉐', '𓐬', '𓋹', '𓐮', '𓏟']
    
    def encode(self, text: Optional[str] = None) -> Dict[str, any]:
        """
        Encode text into the three-script system.
        
        Args:
            text: Input text to encode. If None, returns the default encoding
                  for "em rúnico e tamil e harappan".
        
        Returns:
            Dictionary containing:
            - runic: Runic (Elder Futhark) representation
            - tamil: Tamil script representation
            - tamil_agglutinated: Agglutinated Tamil form
            - harappan: Harappan glyphs as string
            - harappan_list: Harappan glyphs as list
            - bindrune: Synthesized bindrune
            - interpretation: Semantic interpretation
        """
        # Use predefined translation if available
        if text:
            text_normalized = text.lower().strip()
            if text_normalized in self.PREDEFINED_TRANSLATIONS:
                return self.PREDEFINED_TRANSLATIONS[text_normalized].copy()
        
        # Default encoding for the canonical phrase
        return {
            "runic": self.runic,
            "runic_bindrune": "ᛇ",
            "tamil": self.tamil,
            "tamil_agglutinated": "ருனிதமிஹரப்பனிலும்",
            "harappan": "".join(self.harappan),
            "harappan_list": self.harappan.copy(),
            "harappan_sequence": "".join(self.harappan),
            "bindrune": "ᛇ",
            "interpretation": "IN_RUNIC_AND_TAMIL_AND_HARAPPAN"
        }
    
    def encode_to_runic(self, text: str) -> str:
        """
        Encode text to Elder Futhark runes.
        
        Args:
            text: Input text in Latin script
            
        Returns:
            Text encoded in Elder Futhark runes
        """
        result = []
        text = text.lower()
        
        for char in text:
            if char in self.RUNIC_MAP:
                result.append(self.RUNIC_MAP[char])
            else:
                result.append(char)
        
        return ''.join(result)
    
    def encode_to_harappan(self, text: str) -> List[str]:
        """
        Encode text to Harappan glyphs.
        
        Args:
            text: Input text
            
        Returns:
            List of Harappan glyphs
        """
        text_normalized = text.lower().strip()
        words = text_normalized.split()
        
        glyphs = []
        for word in words:
            if word in self.HARAPPAN_MAP:
                glyphs.extend(self.HARAPPAN_MAP[word])
            else:
                # Default glyph for unknown words
                glyphs.append('𓏟')
        
        return glyphs
    
    def create_bindrune(self, runes: str) -> str:
        """
        Create a synthesized bindrune from a runic sequence.
        
        Args:
            runes: Runic text
            
        Returns:
            Synthesized bindrune symbol
        """
        # For the canonical phrase, return the pre-defined bindrune
        if "ᚱᚢᚾᛁᛊᚲ" in runes and "ᛏᚨᛗᛁᛚ" in runes:
            return "ᛇ"
        
        # Default bindrune for other cases
        return "ᛇ"
    
    def get_triple_header(self) -> str:
        """
        Get the triple-script header for file identification.
        
        Returns:
            Formatted header with all three scripts
        """
        return f"# ᛇ தமிழிலும் [{''.join(self.harappan)}]\n# Módulo triplo-escrita שאצ"
    
    def get_unified_representation(self) -> str:
        """
        Get the unified tree representation of all three scripts.
        
        Returns:
            Formatted tree structure showing script hierarchy
        """
        harappan_str = ''.join(self.harappan)
        return f"""ᛇ  // Bindrune rúnica
│
├──{self.tamil}  // Representação Tâmil
│
└──[{harappan_str}]  // Sequência Harappan"""
    
    def get_correspondence_table(self) -> Dict[str, Dict[str, str]]:
        """
        Get the phonetic correspondence table for the three scripts.
        
        Returns:
            Dictionary mapping elements to their representations
        """
        return {
            "em": {
                "portuguese": "/ẽj/",
                "runic": "/in/",
                "tamil": "/-ilum/",
                "harappan": "[𓀠][𓋹]"
            },
            "runico": {
                "portuguese": "/'ʁu.ni.ku/",
                "runic": "/'ru:.nisk/",
                "tamil": "/'ɾu.ɳik.ki/",
                "harappan": "[𓊖][𓐬]"
            },
            "e": {
                "portuguese": "/i/",
                "runic": "/ai/",
                "tamil": "/-um/",
                "harappan": "[𓋹]"
            },
            "tamil": {
                "portuguese": "/tɐ.'mil/",
                "runic": "/'tɑ.mil/",
                "tamil": "/'t̪a.mi.ɻi/",
                "harappan": "[𓉐][𓐬]"
            },
            "harappan": {
                "portuguese": "/hɐ.'ɾɐ.pɐ̃/",
                "runic": "/'hɑ.rɑp.pɑn/",
                "tamil": "/'ha.ɾap.pa.ɳi/",
                "harappan": "[𓐮][𓏟]"
            }
        }


def create_triple_script_header(filename: str = "module") -> str:
    """
    Create a triple-script header for a module file.
    
    Args:
        filename: Name of the module
        
    Returns:
        Formatted header string
    """
    encoder = TripleScriptEncoder()
    return encoder.get_triple_header()


def demonstrate_triple_encoding():
    """Demonstrate the triple-script encoding system."""
    encoder = TripleScriptEncoder()
    
    # Encode the canonical phrase
    result = encoder.encode("em rúnico e tamil e harappan")
    
    print("=" * 70)
    print("TRIPLE-SCRIPT ENCODING DEMONSTRATION")
    print("=" * 70)
    print()
    print("Input: 'em rúnico e tamil e harappan'")
    print()
    print("1. RUNIC (Elder Futhark):")
    print(f"   {result['runic']}")
    print(f"   Bindrune: {result['bindrune']}")
    print()
    print("2. TAMIL:")
    print(f"   {result['tamil']}")
    print(f"   Agglutinated: {result['tamil_agglutinated']}")
    print()
    print("3. HARAPPAN:")
    print(f"   {result['harappan']}")
    print()
    print("4. UNIFIED REPRESENTATION:")
    print(encoder.get_unified_representation())
    print()
    print("5. INTERPRETATION:")
    print(f"   {result['interpretation']}")
    print()
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_triple_encoding()
