"""
Tests for Matrix417Dynamics module
"""

import numpy as np
import pytest
from ute00.matrix417 import Matrix417Dynamics


class TestMatrix417Dynamics:
    """Test suite for Matrix417Dynamics class"""
    
    def test_initialization(self):
        """Test that the system initializes correctly"""
        system = Matrix417Dynamics()
        
        assert system.dimensions == 417
        assert len(system.runes) == 24
        assert len(system.tamil) == 12
        assert system.I == complex(0, 1)
    
    def test_runes_initialization(self):
        """Test that runes are initialized correctly"""
        system = Matrix417Dynamics()
        
        # Check that all runes have required properties
        for rune, props in system.runes.items():
            assert 'vector' in props
            assert 'energy' in props
            assert 'momentum' in props
            assert len(props['vector']) == 24
            assert 0 < props['energy'] <= 1.0
    
    def test_tamil_initialization(self):
        """Test that Tamil phonemes are initialized correctly"""
        system = Matrix417Dynamics()
        
        # Check that all Tamil phonemes have required properties
        for phoneme, props in system.tamil.items():
            assert 'type' in props
            assert 'energy' in props
            assert props['type'] == 'vowel'
            assert props['energy'] > 0
    
    def test_metric_tensor_shape(self):
        """Test that metric tensor has correct shape"""
        system = Matrix417Dynamics()
        x = np.zeros(417)
        
        g = system.metric_tensor(x)
        
        assert g.shape == (417, 417)
        assert np.allclose(np.diag(g).real, 1.0, atol=0.1)
    
    def test_equations_of_motion_shape(self):
        """Test that equations of motion return correct shape"""
        system = Matrix417Dynamics()
        
        # Initial state
        y = np.zeros(834)  # 417 positions + 417 velocities
        y[:417] = 0.01 * np.random.randn(417)
        y[417:] = 0.001 * np.random.randn(417)
        
        dydt = system.equations_of_motion(0.0, y)
        
        assert dydt.shape == (834,)
        assert np.all(np.isfinite(dydt))
    
    def test_simulate(self):
        """Test that simulation runs without errors"""
        system = Matrix417Dynamics()
        
        # Run short simulation
        solution = system.simulate(t_span=[0, 1])
        
        assert solution.success
        assert len(solution.t) > 0
        assert solution.y.shape[0] == 834
    
    def test_calculate_energies(self):
        """Test that energy calculation works"""
        system = Matrix417Dynamics()
        
        # Run short simulation
        solution = system.simulate(t_span=[0, 1])
        energies = system.calculate_energies(solution)
        
        assert 'total' in energies
        assert 'runic' in energies
        assert 'tamil' in energies
        assert 'I' in energies
        
        assert len(energies['total']) == len(solution.t)
        assert all(np.isfinite(energies['total']))


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
