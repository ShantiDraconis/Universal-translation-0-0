import pandas as pd
from .loader import load_harappan_signs, load_dictionary_00


def simple_phonetic_distance(a: str, b: str) -> float:
    """Simplified phonetic distance (0 = different, 1 = very similar)."""
    a = a.lower()
    b = b.lower()
    if a == b:
        return 1.0
    # simple heuristic to start with
    common = len(set(a) & set(b))
    max_len = max(len(a), len(b))
    return common / max_len if max_len > 0 else 0.0


def generate_initial_mapping(top_k: int = 5) -> pd.DataFrame:
    har = load_harappan_signs()
    d00 = load_dictionary_00()

    rows = []
    for _, hrow in har.iterrows():
        hcode = hrow["code"]
        # phonetic_guess field can be added later; using label_short here
        h_label = str(hrow.get("label_short", hcode))

        scores = []
        for _, drow in d00.iterrows():
            token = drow["token"]
            score = simple_phonetic_distance(h_label, token)
            scores.append((token, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        for rank, (token, score) in enumerate(scores[:top_k], start=1):
            rows.append({
                "harappan_code": hcode,
                "token_00": token,
                "candidate_rank": rank,
                "confidence_score": round(float(score), 4),
                "match_type": "phonetic-heuristic",
                "justification_short": "letter intersection heuristic",
                "notes": "",
            })

    return pd.DataFrame(rows)
