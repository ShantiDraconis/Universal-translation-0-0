"""
Example usage of the Triple-Script Encoder (LOG-0024).

This example demonstrates how to use the TripleScriptEncoder to encode
text in the three-layer writing system: Runic, Tamil, and Harappan.
"""

from ute00.scripts import TripleScriptEncoder


def main():
    """Run example demonstrations of triple-script encoding."""
    
    print("=" * 80)
    print("TRIPLE-SCRIPT ENCODER - EXAMPLE USAGE (LOG-0024)")
    print("=" * 80)
    print()
    
    # Create encoder instance
    encoder = TripleScriptEncoder()
    
    # Example 1: Default encoding
    print("Example 1: Default encoding")
    print("-" * 80)
    result = encoder.encode()
    print(f"Runic:       {result['runic']}")
    print(f"Bindrune:    {result['bindrune']}")
    print(f"Tamil:       {result['tamil']}")
    print(f"Agglutinated: {result['tamil_agglutinated']}")
    print(f"Harappan:    {result['harappan']}")
    print()
    
    # Example 2: Portuguese phrase
    print("Example 2: Portuguese phrase")
    print("-" * 80)
    result = encoder.encode("em rúnico e tamil e harappan")
    print(f"Input:        'em rúnico e tamil e harappan'")
    print(f"Runic:        {result['runic']}")
    print(f"Tamil:        {result['tamil']}")
    print(f"Harappan:     {result['harappan']}")
    print(f"Interpretation: {result['interpretation']}")
    print()
    
    # Example 3: English phrase
    print("Example 3: English phrase")
    print("-" * 80)
    result = encoder.encode("in runic and tamil and harappan")
    print(f"Input:        'in runic and tamil and harappan'")
    print(f"Runic:        {result['runic']}")
    print(f"Tamil:        {result['tamil']}")
    print(f"Harappan:     {result['harappan']}")
    print()
    
    # Example 4: Triple-script header
    print("Example 4: Triple-script header for module files")
    print("-" * 80)
    header = encoder.get_triple_header()
    print(header)
    print()
    
    # Example 5: Unified representation
    print("Example 5: Unified tree representation")
    print("-" * 80)
    tree = encoder.get_unified_representation()
    print(tree)
    print()
    
    # Example 6: Correspondence table
    print("Example 6: Phonetic correspondence table")
    print("-" * 80)
    table = encoder.get_correspondence_table()
    print(f"{'Element':<12} {'Portuguese':<18} {'Runic':<18} {'Tamil':<18} {'Harappan':<18}")
    print("-" * 84)
    for element, values in table.items():
        print(f"{element:<12} {values['portuguese']:<18} {values['runic']:<18} "
              f"{values['tamil']:<18} {values['harappan']:<18}")
    print()
    
    # Example 7: Encode to individual scripts
    print("Example 7: Encode to individual scripts")
    print("-" * 80)
    text = "test"
    runic = encoder.encode_to_runic(text)
    print(f"'{text}' in Runic: {runic}")
    
    harappan_glyphs = encoder.encode_to_harappan("em e")
    print(f"'em e' in Harappan: {harappan_glyphs}")
    print()
    
    # Example 8: Create bindrune
    print("Example 8: Create bindrune")
    print("-" * 80)
    runes = "ᛁᚾ ᚱᚢᚾᛁᛊᚲ ᚨᛁ ᛏᚨᛗᛁᛚ"
    bindrune = encoder.create_bindrune(runes)
    print(f"Runes:    {runes}")
    print(f"Bindrune: {bindrune}")
    print()
    
    print("=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
