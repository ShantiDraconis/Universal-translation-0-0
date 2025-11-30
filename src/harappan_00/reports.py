from pathlib import Path
import pandas as pd
from .scoring import compute_stats

BASE_DIR = Path(__file__).resolve().parents[2]


def save_mapping_and_stats(mapping: pd.DataFrame) -> None:
    mapping_dir = BASE_DIR / "data" / "mappings"
    mapping_dir.mkdir(parents=True, exist_ok=True)

    # mapping completo
    mapping_path = mapping_dir / "mapping_harappan_to_00.csv"
    mapping.to_csv(mapping_path, index=False)

    # stats
    stats = compute_stats(mapping)
    stats_path = mapping_dir / "mapping_harappan_to_00_stats.csv"
    stats.to_csv(stats_path, index=False)


def build_summary_reports(mapping: pd.DataFrame) -> None:
    """Gera um relatório simples em Markdown com resumo das associações."""
    docs_dir = BASE_DIR / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    stats = compute_stats(mapping)
    lines = ["# Relatório de Mapeamento Harappan ↔ 00\n"]
    for _, row in stats.iterrows():
        lines.append(
            f"- {row['harappan_code']}: best = {row['best_token_00']} "
            f"(top_conf={row['top_confidence']:.2f}, avg={row['avg_confidence']:.2f})"
        )

    (docs_dir / "harappan_00_summary.md").write_text("\n".join(lines), encoding="utf-8")
