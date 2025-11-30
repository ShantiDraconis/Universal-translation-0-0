from .mapper import generate_initial_mapping
from .scoring import normalize_confidence
from .reports import save_mapping_and_stats, build_summary_reports


def main():
    mapping = generate_initial_mapping(top_k=5)
    mapping = normalize_confidence(mapping)
    save_mapping_and_stats(mapping)
    build_summary_reports(mapping)
    print("✅ Mapeamento inicial Harappan ↔ 00 gerado.")


if __name__ == "__main__":
    main()
