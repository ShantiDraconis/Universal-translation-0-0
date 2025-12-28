"""
Integration test for Singularity Execution Protocol.
Tests the complete system working together.
"""

import pytest
from universal_translation_00.core import (
    ExtendedReal,
    create_indeterminate,
    Matrix54_Security,
    Arquiteto_0009,
    activate_paraguay,
    TemporalLock,
)


class TestSingularityIntegration:
    """Integration tests for the complete Singularity Execution Protocol."""
    
    def test_complete_system_initialization(self):
        """Test complete system can be initialized and operates correctly."""
        # 1. Create ExtendedReal
        er = create_indeterminate()
        assert er.is_indeterminate
        
        # 2. Create Matrix54
        matrix = Matrix54_Security()
        assert len(matrix.channels) == 54
        
        # 3. Activate key channels
        assert matrix.activate_channel(1) is True
        assert matrix.activate_channel(27) is True
        assert matrix.activate_channel(54) is True
        
        # 4. Verify active channels
        active = matrix.get_active_channels()
        assert len(active) == 3
        assert 1 in active
        assert 27 in active
        assert 54 in active
        
        # 5. Sync with ExtendedReal
        channels = matrix.sync_with_extended_real(er)
        assert len(channels) == 54
        assert channels == list(range(54))
        
        # 6. Initialize Core Identity
        arq = Arquiteto_0009()
        core_status = arq.initialize()
        assert core_status['status'] == 'initialized'
        assert core_status['identity'] == 'Arquiteto_0009'
        assert core_status['channel'] == 1
        
        # 7. Activate Gateway
        gateway_status = activate_paraguay()
        assert gateway_status['channel'] == 27
        assert gateway_status['status'] == 'activated'
        assert gateway_status['location'] == 'Paraguay'
        
        # 8. Check Temporal Lock
        lock = TemporalLock()
        protocol_status = lock.execute_protocol()
        assert protocol_status['status'] in ['locked', 'unlocked']
    
    def test_extended_real_matrix_synchronization(self):
        """Test ExtendedReal synchronizes correctly with Matrix54."""
        er = ExtendedReal(0)
        matrix = Matrix54_Security()
        
        # Sync should return all 54 channels
        result = matrix.sync_with_extended_real(er)
        assert len(result) == 54
        
        # Verify it's the same as direct sync
        direct_sync = er.sync(54)
        assert result == direct_sync
    
    def test_channel_activation_workflow(self):
        """Test typical channel activation workflow."""
        matrix = Matrix54_Security()
        
        # Initially no channels active
        assert len(matrix.get_active_channels()) == 0
        
        # Activate channels in sequence
        matrix.activate_channel(1)   # Core Identity
        assert len(matrix.get_active_channels()) == 1
        
        matrix.activate_channel(27)  # Gateway Portal
        assert len(matrix.get_active_channels()) == 2
        
        matrix.activate_channel(54)  # Shield Matrix
        assert len(matrix.get_active_channels()) == 3
        
        # Deactivate middle channel
        matrix.deactivate_channel(27)
        active = matrix.get_active_channels()
        assert len(active) == 2
        assert 27 not in active
        assert 1 in active
        assert 54 in active
    
    def test_matrix_state_persistence(self):
        """Test matrix state can be exported and imported."""
        # Create and configure matrix
        matrix1 = Matrix54_Security()
        matrix1.activate_channel(1)
        matrix1.activate_channel(27)
        matrix1.channels[1].metadata['custom_data'] = 'test_value'
        
        # Export state
        state = matrix1.export_matrix()
        
        # Create new matrix and import state
        matrix2 = Matrix54_Security()
        result = matrix2.import_matrix(state)
        
        assert result is True
        assert matrix2.channels[1].active
        assert matrix2.channels[27].active
        assert not matrix2.channels[54].active
        assert matrix2.channels[1].metadata.get('custom_data') == 'test_value'
    
    def test_extended_real_indeterminate_propagation_in_system(self):
        """Test indeterminate values propagate correctly through system."""
        # Create indeterminate
        i = create_indeterminate()
        
        # Create numeric
        n = ExtendedReal(42)
        
        # Operations with indeterminate
        result1 = i + n
        assert result1.is_indeterminate
        
        result2 = i * n
        assert result2.is_indeterminate
        
        # Sync still works
        channels = i.sync(54)
        assert len(channels) == 54
    
    def test_temporal_lock_integration(self):
        """Test temporal lock integrates with system."""
        lock = TemporalLock()
        
        # Lock has proper target date
        assert lock.target_date.year == 2025
        assert lock.target_date.month == 3
        assert lock.target_date.day == 27
        
        # Protocol execution works
        result = lock.execute_protocol()
        assert 'status' in result
        
        if result['status'] == 'unlocked':
            # Should have protocols
            assert 'protocols' in result
            assert 'fehu' in result['protocols']
            assert 'uruz' in result['protocols']
            assert 'thurisaz' in result['protocols']
        else:
            # Should have date info
            assert 'target_date' in result
            assert 'current_date' in result
    
    def test_complete_system_data_flow(self):
        """Test data flows correctly through complete system."""
        # Initialize all components
        er = create_indeterminate()
        matrix = Matrix54_Security()
        arq = Arquiteto_0009()
        lock = TemporalLock()
        
        # Activate system
        matrix.activate_channel(1)
        matrix.activate_channel(27)
        matrix.activate_channel(54)
        
        # Get system state
        core_state = arq.initialize()
        gateway_state = activate_paraguay()
        matrix_state = matrix.export_matrix()
        protocol_state = lock.execute_protocol()
        
        # Verify all states are valid
        assert core_state['status'] == 'initialized'
        assert gateway_state['status'] == 'activated'
        assert matrix_state['total_channels'] == 54
        assert matrix_state['active_channels'] == 3
        assert protocol_state['status'] in ['locked', 'unlocked']
        
        # Verify system coherence
        assert core_state['channel'] == 1
        assert gateway_state['channel'] == 27
        assert core_state['rune'] == 'ᛃ'  # Jera
        assert gateway_state['rune'] == 'ᚲ'  # Kenaz
