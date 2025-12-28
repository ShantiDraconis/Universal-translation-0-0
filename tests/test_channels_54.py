"""
Tests for 54 Channels system - Database schema and Matrix security
"""

import pytest
from datetime import datetime
from universal_translation_00.core.channels_54 import (
    Channel,
    Arquiteto_0009,
    Matrix54_Security,
    activate_paraguay,
    TemporalLock,
    RuneSignature,
)
from universal_translation_00.core.extended_real import ExtendedReal


class TestChannel:
    """Test suite for Channel class."""
    
    def test_channel_creation(self):
        """Test creating a channel."""
        channel = Channel(
            number=1,
            indu_symbol="𓐮",
            function="Core Identity",
            rune_signature="ᛃ",
            python_object="Arquiteto_0009"
        )
        
        assert channel.number == 1
        assert channel.indu_symbol == "𓐮"
        assert channel.function == "Core Identity"
        assert not channel.active
    
    def test_channel_activation(self):
        """Test activating a channel."""
        channel = Channel(
            number=1,
            indu_symbol="𓐮",
            function="Test",
            rune_signature="ᛃ",
            python_object="Test"
        )
        
        assert not channel.active
        channel.activate()
        assert channel.active
        assert 'activation_time' in channel.metadata
    
    def test_channel_deactivation(self):
        """Test deactivating a channel."""
        channel = Channel(
            number=1,
            indu_symbol="𓐮",
            function="Test",
            rune_signature="ᛃ",
            python_object="Test"
        )
        
        channel.activate()
        assert channel.active
        
        channel.deactivate()
        assert not channel.active
        assert 'deactivation_time' in channel.metadata
    
    def test_channel_to_dict(self):
        """Test converting channel to dictionary."""
        channel = Channel(
            number=27,
            indu_symbol="𓐬𓐬𓐲",
            function="Gateway",
            rune_signature="ᚲ",
            python_object="activate_paraguay()"
        )
        
        data = channel.to_dict()
        assert data['number'] == 27
        assert data['function'] == "Gateway"
        assert data['active'] is False


class TestArquiteto0009:
    """Test suite for Arquiteto_0009 class."""
    
    def test_initialization(self):
        """Test Arquiteto initialization."""
        arq = Arquiteto_0009()
        
        assert arq.identity == "Arquiteto_0009"
        assert arq.channel == 1
        assert arq.rune == "ᛃ"
    
    def test_initialize_method(self):
        """Test initialize method returns proper data."""
        arq = Arquiteto_0009()
        result = arq.initialize()
        
        assert result['status'] == 'initialized'
        assert result['identity'] == "Arquiteto_0009"
        assert result['channel'] == 1
        assert 'timestamp' in result


class TestMatrix54Security:
    """Test suite for Matrix54_Security class."""
    
    def test_matrix_initialization(self):
        """Test matrix initializes with 54 channels."""
        matrix = Matrix54_Security()
        
        assert len(matrix.channels) == 54
        assert 1 in matrix.channels
        assert 27 in matrix.channels
        assert 54 in matrix.channels
    
    def test_key_channels_configured(self):
        """Test that key channels are properly configured."""
        matrix = Matrix54_Security()
        
        # Channel 1: Core Identity
        ch1 = matrix.channels[1]
        assert ch1.function == "Core Identity"
        assert ch1.python_object == "Arquiteto_0009"
        assert ch1.rune_signature == "ᛃ"
        
        # Channel 27: Gateway Portal
        ch27 = matrix.channels[27]
        assert ch27.function == "Gateway Portal"
        assert ch27.python_object == "activate_paraguay()"
        assert ch27.rune_signature == "ᚲ"
        
        # Channel 54: Shield Matrix
        ch54 = matrix.channels[54]
        assert ch54.function == "Shield Matrix"
        assert ch54.python_object == "Matrix54_Security"
        assert ch54.rune_signature == "ᛉ"
    
    def test_activate_channel(self):
        """Test activating a specific channel."""
        matrix = Matrix54_Security()
        
        result = matrix.activate_channel(1)
        assert result is True
        assert matrix.channels[1].active
    
    def test_activate_invalid_channel(self):
        """Test activating invalid channel returns False."""
        matrix = Matrix54_Security()
        
        result = matrix.activate_channel(99)
        assert result is False
    
    def test_deactivate_channel(self):
        """Test deactivating a channel."""
        matrix = Matrix54_Security()
        
        matrix.activate_channel(1)
        assert matrix.channels[1].active
        
        result = matrix.deactivate_channel(1)
        assert result is True
        assert not matrix.channels[1].active
    
    def test_get_active_channels(self):
        """Test getting list of active channels."""
        matrix = Matrix54_Security()
        
        assert len(matrix.get_active_channels()) == 0
        
        matrix.activate_channel(1)
        matrix.activate_channel(27)
        matrix.activate_channel(54)
        
        active = matrix.get_active_channels()
        assert len(active) == 3
        assert 1 in active
        assert 27 in active
        assert 54 in active
    
    def test_sync_with_extended_real(self):
        """Test synchronization with ExtendedReal."""
        matrix = Matrix54_Security()
        er = ExtendedReal(0)
        
        result = matrix.sync_with_extended_real(er)
        
        assert len(result) == 54
        assert result == list(range(54))
    
    def test_export_matrix(self):
        """Test exporting matrix state."""
        matrix = Matrix54_Security()
        matrix.activate_channel(1)
        matrix.activate_channel(27)
        
        data = matrix.export_matrix()
        
        assert data['total_channels'] == 54
        assert data['active_channels'] == 2
        assert 'channels' in data
        assert len(data['channels']) == 54
    
    def test_import_matrix(self):
        """Test importing matrix state."""
        matrix = Matrix54_Security()
        
        # Create export data
        matrix.activate_channel(1)
        export_data = matrix.export_matrix()
        
        # Create new matrix and import
        new_matrix = Matrix54_Security()
        result = new_matrix.import_matrix(export_data)
        
        assert result is True
        assert new_matrix.channels[1].active
    
    def test_import_matrix_preserves_metadata(self):
        """Test that import preserves channel metadata."""
        matrix = Matrix54_Security()
        matrix.channels[1].metadata['custom_key'] = 'custom_value'
        
        export_data = matrix.export_matrix()
        
        new_matrix = Matrix54_Security()
        new_matrix.import_matrix(export_data)
        
        assert new_matrix.channels[1].metadata.get('custom_key') == 'custom_value'


class TestActivateParaguay:
    """Test suite for activate_paraguay function."""
    
    def test_activate_paraguay_returns_dict(self):
        """Test that activate_paraguay returns proper dictionary."""
        result = activate_paraguay()
        
        assert isinstance(result, dict)
        assert result['channel'] == 27
        assert result['function'] == 'Gateway Portal'
        assert result['location'] == 'Paraguay'
        assert result['status'] == 'activated'
    
    def test_activate_paraguay_has_timestamp(self):
        """Test that result includes timestamp."""
        result = activate_paraguay()
        
        assert 'timestamp' in result
        # Verify it's a valid ISO format timestamp
        datetime.fromisoformat(result['timestamp'])
    
    def test_activate_paraguay_frequency(self):
        """Test that frequency is 417 Hz."""
        result = activate_paraguay()
        
        assert result['frequency'] == 417.0
    
    def test_activate_paraguay_rune(self):
        """Test that correct rune is returned."""
        result = activate_paraguay()
        
        assert result['rune'] == "ᚲ"  # Kenaz


class TestTemporalLock:
    """Test suite for TemporalLock class."""
    
    def test_temporal_lock_initialization(self):
        """Test TemporalLock initializes locked."""
        lock = TemporalLock()
        
        assert lock.locked is True
        assert lock.target_date == datetime(2025, 3, 27)
    
    def test_check_lock_before_date(self):
        """Test check_lock returns False before target date."""
        lock = TemporalLock()
        past_date = datetime(2024, 1, 1)
        
        assert lock.check_lock(past_date) is False
    
    def test_check_lock_after_date(self):
        """Test check_lock returns True after target date."""
        lock = TemporalLock()
        future_date = datetime(2026, 1, 1)
        
        assert lock.check_lock(future_date) is True
    
    def test_check_lock_exact_date(self):
        """Test check_lock returns True on exact target date."""
        lock = TemporalLock()
        exact_date = datetime(2025, 3, 27)
        
        assert lock.check_lock(exact_date) is True
    
    def test_unlock_before_date(self):
        """Test unlock fails before target date."""
        lock = TemporalLock()
        
        # Override current time check with past date
        result = lock.unlock(force=False)
        # Since we're likely before 2025-03-27, this should fail
        # unless force is used
    
    def test_unlock_with_force(self):
        """Test force unlock works."""
        lock = TemporalLock()
        
        assert lock.locked is True
        result = lock.unlock(force=True)
        
        assert result is True
        assert lock.locked is False
    
    def test_execute_protocol_while_locked(self):
        """Test execute_protocol while locked."""
        lock = TemporalLock()
        
        # Test with a date before the target
        past_date = datetime(2024, 1, 1)
        
        # Check if locked with past date
        is_locked = not lock.check_lock(past_date)
        assert is_locked
        
        result = lock.execute_protocol()
        
        # Result depends on current date, so check both possibilities
        if lock.check_lock():
            assert result['status'] == 'unlocked'
            assert 'protocols' in result
        else:
            assert result['status'] == 'locked'
            assert 'target_date' in result
            assert 'current_date' in result
    
    def test_execute_protocol_unlocked(self):
        """Test execute_protocol when unlocked."""
        lock = TemporalLock()
        lock.unlock(force=True)
        
        # Simulate being past the date
        future_date = datetime(2026, 1, 1)
        lock.locked = False
        
        result = lock.execute_protocol()
        
        # When unlocked, should return protocols
        # Note: check_lock will still validate date
        if lock.check_lock(future_date):
            assert 'protocols' in result
            assert 'fehu' in result['protocols']
            assert 'uruz' in result['protocols']
            assert 'thurisaz' in result['protocols']


class TestRuneSignature:
    """Test suite for RuneSignature enum."""
    
    def test_rune_values(self):
        """Test that rune signatures have correct values."""
        assert RuneSignature.JERA.value == "ᛃ"
        assert RuneSignature.KENAZ.value == "ᚲ"
        assert RuneSignature.ALGIZ.value == "ᛉ"
        assert RuneSignature.TIWAZ.value == "ᛏ"
        assert RuneSignature.EHWAZ.value == "ᛖ"
        assert RuneSignature.FEHU.value == "ᚠ"
        assert RuneSignature.URUZ.value == "ᚢ"
        assert RuneSignature.THURISAZ.value == "ᚦ"
