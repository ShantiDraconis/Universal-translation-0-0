"""
Tests for the triple-script encoder (LOG-0024).
"""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from ute00.scripts.triple_encoder import TripleScriptEncoder, create_triple_script_header


class TestTripleScriptEncoder:
    """Test suite for TripleScriptEncoder."""
    
    def test_initialization(self):
        """Test that encoder initializes correctly."""
        encoder = TripleScriptEncoder()
        assert encoder.runic == "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ"
        assert encoder.tamil == "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்"
        assert len(encoder.harappan) == 10
    
    def test_encode_default(self):
        """Test encoding with default phrase."""
        encoder = TripleScriptEncoder()
        result = encoder.encode()
        
        assert "runic" in result
        assert "tamil" in result
        assert "harappan" in result
        assert "bindrune" in result
        assert "interpretation" in result
        
        assert result["runic"] == "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ"
        assert result["tamil"] == "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்"
        assert result["bindrune"] == "ᛇ"
    
    def test_encode_portuguese(self):
        """Test encoding with Portuguese phrase."""
        encoder = TripleScriptEncoder()
        result = encoder.encode("em rúnico e tamil e harappan")
        
        assert result["runic"] == "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ"
        assert result["tamil"] == "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்"
        assert result["interpretation"] == "IN_RUNIC_AND_TAMIL_AND_HARAPPAN"
    
    def test_encode_english(self):
        """Test encoding with English phrase."""
        encoder = TripleScriptEncoder()
        result = encoder.encode("in runic and tamil and harappan")
        
        assert result["runic"] == "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ ᚨᛁ ᚺᚨᚱᚨᛈᛈᚨᚾ"
        assert result["tamil"] == "ருனிக்கிலும் தமிழிலும் ஹரப்பனிலும்"
        assert result["interpretation"] == "IN_RUNIC_AND_TAMIL_AND_HARAPPAN"
    
    def test_harappan_list(self):
        """Test Harappan glyph list."""
        encoder = TripleScriptEncoder()
        result = encoder.encode()
        
        assert "harappan_list" in result
        assert isinstance(result["harappan_list"], list)
        assert len(result["harappan_list"]) == 10
        assert result["harappan_list"][0] == '𓀠'
        assert result["harappan_list"][-1] == '𓏟'
    
    def test_tamil_agglutinated(self):
        """Test agglutinated Tamil form."""
        encoder = TripleScriptEncoder()
        result = encoder.encode()
        
        assert "tamil_agglutinated" in result
        assert result["tamil_agglutinated"] == "ருனிதமிஹரப்பனிலும்"
    
    def test_encode_to_runic(self):
        """Test runic encoding function."""
        encoder = TripleScriptEncoder()
        
        # Test basic Latin to Runic conversion
        runic = encoder.encode_to_runic("test")
        assert runic == "ᛏᛖᛊᛏ"
        
        # Test with spaces
        runic = encoder.encode_to_runic("in runic")
        assert " " in runic
        assert "ᛁᚾ" in runic
    
    def test_encode_to_harappan(self):
        """Test Harappan encoding function."""
        encoder = TripleScriptEncoder()
        
        # Test known words
        glyphs = encoder.encode_to_harappan("em")
        assert glyphs == ['𓀠', '𓋹']
        
        glyphs = encoder.encode_to_harappan("e")
        assert glyphs == ['𓋹']
    
    def test_create_bindrune(self):
        """Test bindrune creation."""
        encoder = TripleScriptEncoder()
        
        # Test with canonical phrase
        bindrune = encoder.create_bindrune("ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ")
        assert bindrune == "ᛇ"
    
    def test_get_triple_header(self):
        """Test triple-script header generation."""
        encoder = TripleScriptEncoder()
        header = encoder.get_triple_header()
        
        assert "ᛇ" in header
        assert "தமிழிலும்" in header
        assert "𓀠" in header
        assert "Módulo triplo-escrita" in header
    
    def test_get_unified_representation(self):
        """Test unified tree representation."""
        encoder = TripleScriptEncoder()
        tree = encoder.get_unified_representation()
        
        assert "ᛇ" in tree
        assert "Bindrune rúnica" in tree
        assert "ருனிக்கிலும்" in tree
        assert "Representação Tâmil" in tree
        assert "𓀠" in tree
        assert "Sequência Harappan" in tree
    
    def test_get_correspondence_table(self):
        """Test correspondence table."""
        encoder = TripleScriptEncoder()
        table = encoder.get_correspondence_table()
        
        assert "em" in table
        assert "runico" in table
        assert "e" in table
        assert "tamil" in table
        assert "harappan" in table
        
        # Check structure
        assert "portuguese" in table["em"]
        assert "runic" in table["em"]
        assert "tamil" in table["em"]
        assert "harappan" in table["em"]
    
    def test_runic_map_exists(self):
        """Test that Runic map is properly defined."""
        encoder = TripleScriptEncoder()
        
        assert 'a' in encoder.RUNIC_MAP
        assert 'i' in encoder.RUNIC_MAP
        assert 'n' in encoder.RUNIC_MAP
        assert encoder.RUNIC_MAP['i'] == 'ᛁ'
        assert encoder.RUNIC_MAP['n'] == 'ᚾ'
    
    def test_harappan_map_exists(self):
        """Test that Harappan map is properly defined."""
        encoder = TripleScriptEncoder()
        
        assert 'em' in encoder.HARAPPAN_MAP
        assert 'runico' in encoder.HARAPPAN_MAP
        assert 'tamil' in encoder.HARAPPAN_MAP
        assert 'harappan' in encoder.HARAPPAN_MAP
        assert 'e' in encoder.HARAPPAN_MAP


class TestTripleScriptHelpers:
    """Test helper functions."""
    
    def test_create_triple_script_header(self):
        """Test header creation helper."""
        header = create_triple_script_header("test_module")
        
        assert isinstance(header, str)
        assert "ᛇ" in header
        assert "𓀠" in header


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
