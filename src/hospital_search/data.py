"""Dataset loading helpers.

The hospital dataset is loaded once and cached in memory. The CSV is wide
(many columns), but the application only needs a small, well-named subset for
display and search.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import pandas as pd

# Columns surfaced to the UI, mapped to the keys the template expects.
DISPLAY_COLUMNS: dict[str, str] = {
    "Nama Rumah Sakit": "Nama Rumah Sakit",
    "Jenis Rumah Sakit": "Jenis Rumah Sakit",
    "Alamat": "Alamat",
}

# Columns used as search targets.
SEARCHABLE_COLUMNS: tuple[str, ...] = (
    "Nama Rumah Sakit",
    "Jenis Rumah Sakit",
    "Alamat",
    "Kab/Kota",
)


@lru_cache(maxsize=1)
def load_dataset(data_file: str) -> pd.DataFrame:
    """Load and normalise the hospital dataset.

    The result is cached so the CSV is read from disk only once per process.

    Args:
        data_file: Absolute path to the CSV file.

    Returns:
        A cleaned DataFrame containing only the columns the app uses.
    """
    path = Path(data_file)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    frame = pd.read_csv(path, dtype=str).fillna("")

    # Keep only the columns we actually use, ignoring any that are missing.
    keep = [column for column in SEARCHABLE_COLUMNS if column in frame.columns]
    frame = frame[keep].copy()

    # Trim surrounding whitespace that is common in the scraped source data.
    for column in frame.columns:
        frame[column] = frame[column].str.strip()

    return frame
