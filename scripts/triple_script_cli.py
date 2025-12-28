#!/usr/bin/env python3
"""
CLI for Triple-Script Encoder (LOG-0024).

Command-line interface for encoding text into the three-layer writing system:
Runic (Elder Futhark), Tamil, and Harappan.
"""

import argparse
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from ute00.scripts import TripleScriptEncoder


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Triple-Script Encoder - Encode text in Runic, Tamil, and Harappan scripts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Encode the default phrase
  %(prog)s
  
  # Encode a custom phrase
  %(prog)s --text "em rúnico e tamil e harappan"
  
  # Show only Runic encoding
  %(prog)s --runic-only
  
  # Show only Tamil encoding
  %(prog)s --tamil-only
  
  # Show only Harappan encoding
  %(prog)s --harappan-only
  
  # Show the triple-script header
  %(prog)s --header
  
  # Show correspondence table
  %(prog)s --table
  
  # Show unified representation
  %(prog)s --tree
        """
    )
    
    parser.add_argument(
        "--text",
        "-t",
        type=str,
        help="Text to encode (default: canonical phrase)"
    )
    
    parser.add_argument(
        "--runic-only",
        "-r",
        action="store_true",
        help="Show only Runic encoding"
    )
    
    parser.add_argument(
        "--tamil-only",
        "-T",
        action="store_true",
        help="Show only Tamil encoding"
    )
    
    parser.add_argument(
        "--harappan-only",
        "-H",
        action="store_true",
        help="Show only Harappan encoding"
    )
    
    parser.add_argument(
        "--header",
        action="store_true",
        help="Show triple-script header"
    )
    
    parser.add_argument(
        "--table",
        action="store_true",
        help="Show phonetic correspondence table"
    )
    
    parser.add_argument(
        "--tree",
        action="store_true",
        help="Show unified tree representation"
    )
    
    parser.add_argument(
        "--demo",
        "-d",
        action="store_true",
        help="Run full demonstration"
    )
    
    args = parser.parse_args()
    
    # Create encoder
    encoder = TripleScriptEncoder()
    
    # Handle special commands
    if args.header:
        print(encoder.get_triple_header())
        return 0
    
    if args.table:
        table = encoder.get_correspondence_table()
        print(f"{'Element':<12} {'Portuguese':<18} {'Runic':<18} {'Tamil':<18} {'Harappan':<18}")
        print("=" * 84)
        for element, values in table.items():
            print(f"{element:<12} {values['portuguese']:<18} {values['runic']:<18} "
                  f"{values['tamil']:<18} {values['harappan']:<18}")
        return 0
    
    if args.tree:
        print(encoder.get_unified_representation())
        return 0
    
    if args.demo:
        from ute00.scripts.triple_encoder import demonstrate_triple_encoding
        demonstrate_triple_encoding()
        return 0
    
    # Encode text
    result = encoder.encode(args.text)
    
    # Display results based on flags
    if args.runic_only:
        print(result["runic"])
        print(f"Bindrune: {result['bindrune']}")
    elif args.tamil_only:
        print(result["tamil"])
        print(f"Agglutinated: {result['tamil_agglutinated']}")
    elif args.harappan_only:
        print(result["harappan"])
    else:
        # Show all
        print("=" * 70)
        print("TRIPLE-SCRIPT ENCODING")
        print("=" * 70)
        if args.text:
            print(f"\nInput: {args.text}")
        print()
        print(f"Runic (Elder Futhark):")
        print(f"  {result['runic']}")
        print(f"  Bindrune: {result['bindrune']}")
        print()
        print(f"Tamil:")
        print(f"  {result['tamil']}")
        print(f"  Agglutinated: {result['tamil_agglutinated']}")
        print()
        print(f"Harappan:")
        print(f"  {result['harappan']}")
        print()
        print(f"Interpretation: {result['interpretation']}")
        print("=" * 70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
