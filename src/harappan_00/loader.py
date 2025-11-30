import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]  # repo root


def load_harappan_signs() -> pd.DataFrame:
    path = BASE_DIR / "data" / "harappan_signs" / "harappan_417_signs_template.csv"
    return pd.read_csv(path)


def load_dictionary_00() -> pd.DataFrame:
    path = BASE_DIR / "data" / "dictionary_00" / "00_dictionary_1000.csv"
    return pd.read_csv(path)
