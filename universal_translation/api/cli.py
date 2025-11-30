"""
universal_translation/api/cli.py

Command-line interface for the Universal Translation Engine 0/0.

Usage:
    python -m universal_translation.api.cli "Hello world"
    python -m universal_translation.api.cli --mode full "Om mani padme hum"
    python -m universal_translation.api.cli --harappan 1 8 15
    python -m universal_translation.api.cli --numerology "Sacred text"

Example:
    $ python -m universal_translation.api.cli "fire water earth"
    {
        "input": "fire water earth",
        "tokens": ["fire", "water", "earth"],
        ...
    }
"""

import argparse
import json
import sys
from typing import List

from universal_translation.api.translate import (
    translate,
    decode_harappan,
    analyze_numerology,
    get_symbolic_meaning,
    get_universal_phrase,
)


def format_output(data: dict, format_type: str = "json") -> str:
    """Format output data for display."""
    if format_type == "json":
        return json.dumps(data, indent=2, ensure_ascii=False)
    elif format_type == "simple":
        # Simple key-value format
        lines = []
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value, ensure_ascii=False)
            lines.append(f"{key}: {value}")
        return "\n".join(lines)
    else:
        return str(data)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Universal Translation Engine 0/0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Hello world"
  %(prog)s --mode full "Om mani padme hum"
  %(prog)s --harappan 1 8 15 42
  %(prog)s --numerology "Sacred text"
  %(prog)s --symbolic "fire water earth"
  %(prog)s --phrase "Universal message"
        """,
    )

    parser.add_argument(
        "text",
        nargs="*",
        help="Text to translate (or sign IDs with --harappan)",
    )

    parser.add_argument(
        "--mode",
        "-m",
        choices=["standard", "full", "simple"],
        default="standard",
        help="Translation mode (default: standard)",
    )

    parser.add_argument(
        "--harappan",
        "-H",
        action="store_true",
        help="Decode Harappan sign IDs instead of text",
    )

    parser.add_argument(
        "--numerology",
        "-n",
        action="store_true",
        help="Perform numerological analysis only",
    )

    parser.add_argument(
        "--symbolic",
        "-s",
        action="store_true",
        help="Get symbolic meanings only",
    )

    parser.add_argument(
        "--phrase",
        "-p",
        action="store_true",
        help="Get only the Universal 0/0 phrase",
    )

    parser.add_argument(
        "--format",
        "-f",
        choices=["json", "simple"],
        default="json",
        help="Output format (default: json)",
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="Universal Translation Engine 0/0 v0.1.0",
    )

    args = parser.parse_args()

    if not args.text:
        parser.print_help()
        sys.exit(1)

    try:
        if args.harappan:
            # Interpret text as sign IDs
            sign_ids = [int(s) for s in args.text]
            result = decode_harappan(sign_ids)

        elif args.numerology:
            text = " ".join(args.text)
            result = analyze_numerology(text)

        elif args.symbolic:
            text = " ".join(args.text)
            result = get_symbolic_meaning(text)

        elif args.phrase:
            text = " ".join(args.text)
            phrase = get_universal_phrase(text)
            result = {"input": text, "universal_phrase": phrase}

        else:
            text = " ".join(args.text)
            result = translate(text, args.mode)

        print(format_output(result, args.format))

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
