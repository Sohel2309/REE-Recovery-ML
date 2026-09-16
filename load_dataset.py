"""
load_dataset.py

Reproducibility / QC utility for the Stage-1 REE acid-leaching evidence pool.

This script ONLY loads and summarises the current primary evidence pool
(data/raw/REE_Stage1_MASTER_All_Claude_Datasets_Unique.xlsx, sheet
"MASTER_Unique_Data"). It performs no imputation, no filtering to a "final"
dataset, and no modelling — it exists so anyone cloning this repository can
independently verify the row/column counts and QC summary quoted in the
README and docs.

Usage:
    python src/load_dataset.py
"""

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "data" / "raw" / "REE_Stage1_MASTER_All_Claude_Datasets_Unique.xlsx"

TARGET_COLS = [
    "target_Nd_stage1_pct",
    "target_Pr_stage1_pct",
    "target_Dy_stage1_pct",
    "target_Tb_stage1_pct",
    "target_Y_stage1_pct",
]


def load_master(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the MASTER_Unique_Data sheet as-is (no cleaning applied)."""
    if not path.exists():
        raise FileNotFoundError(
            f"Could not find {path}. Make sure the raw evidence-pool file "
            "is present in data/raw/ (see data/README.md)."
        )
    return pd.read_excel(path, sheet_name="MASTER_Unique_Data")


def summarise(df: pd.DataFrame) -> None:
    print(f"Total rows: {len(df)}")
    print(f"Total columns: {df.shape[1]}")
    print(f"Unique DOIs: {df['DOI'].nunique()}")
    print(f"Unique 'Paper' labels: {df['Paper'].nunique()} (not fully DOI-normalised)")

    print("\n--- Feedstock (raw 'Feedstock' column, top values) ---")
    print(df["Feedstock"].value_counts().head(10))

    print("\n--- Acid (raw 'Leaching acid' column, top values) ---")
    print(df["Leaching acid"].value_counts().head(10))

    print("\n--- Per-element target completeness (non-null counts) ---")
    for col in TARGET_COLS:
        print(f"  {col}: {df[col].notna().sum()} / {len(df)}")

    has_any_element = df[TARGET_COLS].notna().any(axis=1)
    has_aggregate_only = (~has_any_element) & df["target_total_REE_stage1_pct"].notna()
    needs_review = df["flag_target_needs_manual_review"] == 1

    print("\n--- Approximate CORE / REVIEW split (see data/README.md) ---")
    print(f"  Rows with >=1 specific per-element recovery value: {has_any_element.sum()}")
    print(f"  Rows with only an aggregate total-REE value: {has_aggregate_only.sum()}")
    print(f"  Rows flagged flag_target_needs_manual_review=1: {int(needs_review.sum())}")

    print("\n--- pH reporting (Stage-1 variable, currently a known gap) ---")
    ph_reported = (df["flag_pH_reported"] == 1).sum()
    print(f"  Rows with pH explicitly reported: {ph_reported} / {len(df)}")

    print(
        "\nNOTE: This is a QC summary of the raw evidence pool only. "
        "No filtering, imputation, or modelling has been applied. "
        "See data/README.md and docs/scope.md before using this data for "
        "any downstream analysis."
    )


if __name__ == "__main__":
    master_df = load_master()
    summarise(master_df)
