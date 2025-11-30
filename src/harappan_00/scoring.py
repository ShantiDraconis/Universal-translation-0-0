import pandas as pd


def normalize_confidence(df: pd.DataFrame) -> pd.DataFrame:
    grouped = []
    for hcode, sub in df.groupby("harappan_code"):
        max_score = sub["confidence_score"].max()
        if max_score > 0:
            sub = sub.copy()
            sub["confidence_score"] = sub["confidence_score"] / max_score
        grouped.append(sub)
    return pd.concat(grouped, ignore_index=True)


def compute_confidence_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Alias for normalize_confidence for backward compatibility."""
    return normalize_confidence(df)


def compute_stats(df: pd.DataFrame) -> pd.DataFrame:
    stats = (
        df.groupby("harappan_code")
        .agg(
            total_candidates=("token_00", "count"),
            top_confidence=("confidence_score", "max"),
            avg_confidence=("confidence_score", "mean"),
        )
        .reset_index()
    )
    # best token_00 (highest confidence)
    idx = df.sort_values(["harappan_code", "confidence_score"], ascending=[True, False])
    idx = idx.groupby("harappan_code").head(1)
    stats = stats.merge(
        idx[["harappan_code", "token_00"]],
        on="harappan_code",
        how="left"
    )
    stats = stats.rename(columns={"token_00": "best_token_00"})
    return stats
