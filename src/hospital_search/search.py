"""Search logic over the hospital dataset."""

from __future__ import annotations

import pandas as pd

from .data import SEARCHABLE_COLUMNS


def search_hospitals(
    frame: pd.DataFrame,
    query: str,
    limit: int,
) -> list[dict[str, str]]:
    """Return hospital records matching a free-text query.

    The match is a case-insensitive substring search across the searchable
    columns. An empty query returns the first ``limit`` records so the table
    is never blank.

    Args:
        frame: The hospital dataset.
        query: The user-supplied search term.
        limit: Maximum number of records to return.

    Returns:
        A list of records as plain dictionaries, ready for templating/JSON.
    """
    cleaned = query.strip()
    if not cleaned:
        return frame.head(limit).to_dict(orient="records")

    columns = [column for column in SEARCHABLE_COLUMNS if column in frame.columns]

    mask = pd.Series(False, index=frame.index)
    for column in columns:
        mask |= frame[column].str.contains(cleaned, case=False, na=False, regex=False)

    return frame[mask].head(limit).to_dict(orient="records")
