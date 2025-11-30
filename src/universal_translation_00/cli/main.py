"""
Command Line Interface for Universal Translation 0/0.

Provides CLI commands for translation, search, and analysis.
"""

import json
import sys
from typing import Optional

import click

from universal_translation_00 import __version__
from universal_translation_00.core.pipeline_manager import UniversalTranslator
from universal_translation_00.harappan.mapping import HarappanMapping
from universal_translation_00.harappan.renderer import HarappanRenderer
from universal_translation_00.dict00.search import Dict00Search


@click.group()
@click.version_option(version=__version__, prog_name="universal-translate-00")
def main() -> None:
    """
    Universal Translation 0/0 - Motor de Tradução Universal.

    A cross-linguistic analysis system for reconstructing Harappan phonemes
    through comparative phonetic analysis.
    """
    pass


@main.command()
@click.argument("text")
@click.option("--format", "-f", type=click.Choice(["text", "json", "detailed"]),
              default="text", help="Output format")
@click.option("--include-etymology/--no-etymology", default=True,
              help="Include etymological information")
def translate(text: str, format: str, include_etymology: bool) -> None:
    """
    Translate text to Harappan phonetic representation.

    TEXT is the input text in any supported language.
    """
    translator = UniversalTranslator(include_etymology=include_etymology)
    result = translator.translate(text)

    if format == "json":
        click.echo(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
    elif format == "detailed":
        click.echo(f"\n{'='*60}")
        click.echo(f" Universal Translation 0/0")
        click.echo(f"{'='*60}")
        click.echo(f"\n Original:  {result.original_text}")
        click.echo(f" Normalized: {result.normalized_text}")
        click.echo(f"\n Phonetic:  {result.phonetic_reading}")
        click.echo(f" Harappan:  {result.harappan_sequence}")
        click.echo(f"\n Metadata:")
        for key, value in result.metadata.items():
            if key != "etymology":
                click.echo(f"   {key}: {value}")
        if include_etymology and "etymology" in result.metadata:
            click.echo(f"\n Etymology:")
            for phoneme, meaning in result.metadata["etymology"].items():
                click.echo(f"   {phoneme}: {meaning}")
        click.echo(f"\n{'='*60}")
    else:
        click.echo(f"Phonetic: {result.phonetic_reading}")
        click.echo(f"Harappan: {result.harappan_sequence}")


@main.command()
@click.argument("sign_id")
@click.option("--format", "-f", type=click.Choice(["text", "json", "detailed"]),
              default="detailed", help="Output format")
def search(sign_id: str, format: str) -> None:
    """
    Search for a Harappan sign by ID.

    SIGN_ID is the sign identifier (e.g., H001, H417).
    """
    harappan = HarappanMapping()
    renderer = HarappanRenderer()

    sign = harappan.get_sign(sign_id)

    if not sign:
        click.echo(f"Sign {sign_id} not found.", err=True)
        sys.exit(1)

    if format == "json":
        click.echo(json.dumps(sign.to_dict(), indent=2, ensure_ascii=False))
    elif format == "detailed":
        click.echo(renderer.render_detailed(sign))
    else:
        click.echo(f"{sign.id}: {sign.phoneme} ({sign.group})")


@main.command("list-group")
@click.argument("group")
@click.option("--format", "-f", type=click.Choice(["table", "json"]),
              default="table", help="Output format")
def list_group(group: str, format: str) -> None:
    """
    List all signs in a semantic group.

    GROUP is the group code (e.g., NUM, CON, GRID).
    """
    harappan = HarappanMapping()
    renderer = HarappanRenderer()

    signs = harappan.get_signs_by_group(group)

    if not signs:
        click.echo(f"No signs found in group {group}.", err=True)
        click.echo("Available groups: NUM, CON, GRID, CHEV, CIRC, OPER, HUM, ANIM, PLANT, ABSTR, RIT, ARCH, MISC")
        sys.exit(1)

    if format == "json":
        click.echo(json.dumps([s.to_dict() for s in signs], indent=2, ensure_ascii=False))
    else:
        click.echo(renderer.render_table(signs))


@main.command("analyze-phoneme")
@click.argument("phoneme")
@click.option("--similar/--no-similar", default=True, help="Show similar phonemes")
def analyze_phoneme(phoneme: str, similar: bool) -> None:
    """
    Analyze a phoneme and show related information.

    PHONEME is the phoneme to analyze (e.g., ta, ma, ka).
    """
    harappan = HarappanMapping()
    dict_search = Dict00Search()

    # Get Harappan signs for this phoneme
    signs = harappan.phoneme_to_signs(phoneme)

    click.echo(f"\n{'='*50}")
    click.echo(f" Phoneme Analysis: {phoneme}")
    click.echo(f"{'='*50}")

    click.echo(f"\n Harappan Signs ({len(signs)} total):")
    for sign in signs[:10]:  # Show first 10
        click.echo(f"   {sign.id} - {sign.group} ({sign.semantic_field[:30]})")
    if len(signs) > 10:
        click.echo(f"   ... and {len(signs) - 10} more")

    # Get dictionary entries
    dict_entries = dict_search.search_by_phoneme(phoneme)
    if dict_entries:
        click.echo(f"\n Dictionary Entries:")
        for entry in dict_entries[:5]:
            click.echo(f"   {entry['phoneme']}: {entry['meaning_en']} ({entry['semantic_class']})")

    # Show similar phonemes
    if similar:
        similar_phonemes = dict_search.find_similar(phoneme)
        if similar_phonemes:
            click.echo(f"\n Similar Phonemes:")
            for sim_phoneme, score in similar_phonemes:
                click.echo(f"   {sim_phoneme}: {score:.2f}")

    click.echo(f"\n{'='*50}")


@main.command()
def stats() -> None:
    """Show statistics about the Harappan mapping."""
    harappan = HarappanMapping()
    statistics = harappan.get_statistics()

    click.echo(f"\n{'='*50}")
    click.echo(f" Harappan Mapping Statistics")
    click.echo(f"{'='*50}")
    click.echo(f"\n Total Signs:     {statistics['total_signs']}")
    click.echo(f" Unique Phonemes: {statistics['unique_phonemes']}")
    click.echo(f" Groups:          {statistics['groups']}")

    click.echo(f"\n Group Sizes:")
    for group, size in sorted(statistics['group_sizes'].items()):
        click.echo(f"   {group:6s}: {size:3d} signs")

    click.echo(f"\n Top Phonemes:")
    sorted_phonemes = sorted(
        statistics['phoneme_distribution'].items(),
        key=lambda x: x[1],
        reverse=True
    )
    for phoneme, count in sorted_phonemes[:10]:
        click.echo(f"   {phoneme:6s}: {count:3d} occurrences")

    click.echo(f"\n{'='*50}")


@main.command("search-meaning")
@click.argument("query")
@click.option("--language", "-l", type=click.Choice(["en", "pt"]),
              default="en", help="Search language")
@click.option("--max-results", "-n", default=10, help="Maximum results")
def search_meaning(query: str, language: str, max_results: int) -> None:
    """
    Search dictionary by meaning.

    QUERY is the search term.
    """
    dict_search = Dict00Search()
    results = dict_search.search_by_meaning(query, language, max_results)

    if not results:
        click.echo(f"No results found for '{query}'", err=True)
        sys.exit(1)

    click.echo(f"\n Results for '{query}':")
    click.echo(f" {'-'*40}")
    for entry in results:
        meaning = entry['meaning_en'] if language == 'en' else entry['meaning_pt']
        click.echo(f" {entry['phoneme']:8s} | {meaning} ({entry['semantic_class']})")


@main.command("export-json")
@click.option("--output", "-o", type=click.Path(), default="harappan_export.json",
              help="Output file path")
def export_json(output: str) -> None:
    """Export all Harappan data to JSON."""
    harappan = HarappanMapping()
    signs = harappan.get_all_signs()

    data = {
        "version": __version__,
        "total_signs": len(signs),
        "signs": [s.to_dict() for s in signs],
        "statistics": harappan.get_statistics(),
    }

    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    click.echo(f"Exported {len(signs)} signs to {output}")


if __name__ == "__main__":
    main()
