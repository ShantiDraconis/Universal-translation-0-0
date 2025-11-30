"""
tools/create_universal_structure.py

Bootstrap script to create the base directory structure for the
Universal Translation Engine 0/0 project.

Run this from the repository root:

    python tools/create_universal_structure.py

This script creates all necessary directories and placeholder files
for the complete project structure.
"""

import os
from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parent.parent


def mkdir(path: Path) -> None:
    """Create a directory if it does not exist."""
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {path}")


def write_if_missing(path: Path, content: str) -> None:
    """
    Write a file only if it does not exist yet.

    This avoids accidentally overwriting user edits.
    """
    if not path.exists():
        path.write_text(dedent(content).lstrip(), encoding="utf-8")
        print(f"Created file: {path}")
    else:
        print(f"Skipped (exists): {path}")


def create_package_init(path: Path, package_name: str = "") -> None:
    """
    Create a minimal __init__.py for a package.
    """
    content = f'"""{"Package " + package_name if package_name else "Package"}."""\n'
    write_if_missing(path / "__init__.py", content)


def main():
    """Create the complete directory structure."""
    print("=" * 60)
    print("Universal Translation Engine 0/0 - Bootstrap Script")
    print("=" * 60)
    
    # Main package directories
    directories = [
        "universal_translation/core",
        "universal_translation/mappings",
        "universal_translation/datasets/harappan/images",
        "universal_translation/datasets/universal",
        "universal_translation/api",
        "universal_translation/evaluation/benchmark_dataset",
        "universal_translation/utils",
        "docs/pipelines",
        "docs/prompts",
        "tests",
        ".github/workflows",
        "examples",
        "tools",
    ]
    
    print("\nCreating directories...")
    for d in directories:
        mkdir(REPO_ROOT / d)
    
    # Create __init__.py files
    print("\nCreating __init__.py files...")
    packages = [
        "universal_translation",
        "universal_translation/core",
        "universal_translation/mappings",
        "universal_translation/datasets",
        "universal_translation/api",
        "universal_translation/evaluation",
        "universal_translation/utils",
    ]
    
    for pkg in packages:
        pkg_path = REPO_ROOT / pkg
        if not (pkg_path / "__init__.py").exists():
            create_package_init(pkg_path, pkg.split("/")[-1])
    
    # Create placeholder README files
    print("\nCreating placeholder files...")
    
    placeholders = {
        "universal_translation/datasets/harappan/README.md": """
            # Harappan Datasets
            
            Place Harappan sign datasets here.
            See harappan-00-universal/data/ for existing data.
        """,
        "universal_translation/datasets/universal/README.md": """
            # Universal Datasets
            
            Place universal phoneme, root, and symbol datasets here.
        """,
        "universal_translation/evaluation/benchmark_dataset/README.md": """
            # Benchmark Dataset
            
            Place benchmark evaluation datasets here.
        """,
    }
    
    for path, content in placeholders.items():
        write_if_missing(REPO_ROOT / path, content)
    
    print("\n" + "=" * 60)
    print("Bootstrap complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Run: pip install -e .")
    print("  2. Run: pytest tests/")
    print("  3. Run: python -m universal_translation.api.cli --help")


if __name__ == "__main__":
    main()
