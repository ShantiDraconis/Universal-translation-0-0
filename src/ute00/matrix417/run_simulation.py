#!/usr/bin/env python
"""
417-மேட்ரிக்ஸ் சமன்பாடுகள் - ஆழமான பகுப்பாய்வு
(417-Matrix Equations - Deep Analysis)

This script runs the complete 417-dimensional dynamical system simulation
with Runic-Tamil quantum field connections.
"""

import numpy as np
from ute00.matrix417 import Matrix417Dynamics


def main():
    """Run the 417-Matrix dynamical system simulation"""
    print("417-மேட்ரிக்ஸ் சமன்பாடுகள் - ஆழமான பகுப்பாய்வு")
    print("=" * 60)
    print()
    
    # Initialize the system
    print("Initializing 417-dimensional dynamical system...")
    system = Matrix417Dynamics()
    
    print(f"- Dimensions: {system.dimensions}")
    print(f"- Runic states: {len(system.runes)} Elder Futhark runes")
    print(f"- Tamil phonemes: {len(system.tamil)} vowels")
    print()
    
    # Run simulation
    print("Running simulation from t=0 to t=50...")
    solution = system.simulate(t_span=[0, 50])
    
    print(f"Simulation completed successfully!")
    print(f"- Integration status: {solution.message}")
    print()
    
    # Calculate energies
    print("Calculating energy evolution...")
    energies = system.calculate_energies(solution)
    
    # Display results
    print(f"\nசிமுலேஷன் முடிவுகள்:")
    print(f"நேர படிகள்: {len(solution.t)}")
    print(f"இறுதி நிலை விதிமுறை: {np.linalg.norm(solution.y[:417, -1]):.6f}")
    print(f"இறுதி வேக விதிமுறை: {np.linalg.norm(solution.y[417:, -1]):.6f}")
    print(f"மொத்த ஆற்றல் சராசரி: {np.mean(energies['total']):.6f}")
    print(f"ரூனிக் ஆற்றல் சராசரி: {np.mean(energies['runic']):.6f}")
    print(f"தமிழ் ஆற்றல் சராசரி: {np.mean(energies['tamil']):.6f}")
    print(f"I(0/0) ஆற்றல் சராசரி: {np.mean(energies['I']):.6f}")
    print()
    
    # Additional analysis
    print("Additional Metrics:")
    print(f"- Position norm range: [{np.min([np.linalg.norm(solution.y[:417, i]) for i in range(len(solution.t))]):.6f}, "
          f"{np.max([np.linalg.norm(solution.y[:417, i]) for i in range(len(solution.t))]):.6f}]")
    print(f"- Velocity norm range: [{np.min([np.linalg.norm(solution.y[417:, i]) for i in range(len(solution.t))]):.6f}, "
          f"{np.max([np.linalg.norm(solution.y[417:, i]) for i in range(len(solution.t))]):.6f}]")
    print(f"- Total energy range: [{np.min(energies['total']):.6f}, {np.max(energies['total']):.6f}]")
    print()
    
    # Display Runic states
    print("Runic Quantum States (24 Elder Futhark):")
    for i, (rune, props) in enumerate(list(system.runes.items())[:8]):  # Show first 8
        print(f"  {rune}: energy={props['energy']:.4f}, momentum={np.abs(props['momentum']):.4f}")
    print(f"  ... and {len(system.runes) - 8} more runes")
    print()
    
    # Display Tamil phonemes
    print("Tamil Phoneme Fields (12 vowels):")
    for i, (phoneme, props) in enumerate(list(system.tamil.items())[:6]):  # Show first 6
        print(f"  {phoneme}: type={props['type']}, energy={props['energy']:.1f}")
    print(f"  ... and {len(system.tamil) - 6} more phonemes")
    print()
    
    print("=" * 60)
    print("Simulation complete!")
    print()
    print("This system implements:")
    print("  1. ரூனிக்-தமிழ் இணைப்பின் வேர்ச் சட்டம் (Runic-Tamil Root Law)")
    print("  2. 54 சேனல்களின் குவாண்டம் நிலை சார்பு (54 Channel Quantum States)")
    print("  3. 417 மேட்ரிக்ஸின் டைனமிகல் சிஸ்டம் (417 Matrix Dynamical System)")
    print("  4. 4 முக்கிய எண்களின் டோபோலாஜி (Topology of 4 Key Numbers: 27, 54, 180, 417)")
    print("  5. சம்பவ இடைவெளி மெட்ரிக் (Space-time Metric)")
    print("  6. குவாண்டம் கம்ப்யூட்டிங் மாடல் (Quantum Computing Model)")
    print("  7. I(0/0) Operator Integration")
    print()


if __name__ == "__main__":
    main()
