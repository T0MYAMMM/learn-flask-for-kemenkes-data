"""Application configuration.

Values are read from environment variables where it makes sense, with
reasonable defaults so the application runs out of the box for local use.
"""

from __future__ import annotations

import os
from pathlib import Path

# Project root resolved relative to this file:
# src/hospital_search/config.py -> parents[2] is the repository root.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_DATA_FILE = PROJECT_ROOT / "data" / "rumahsakit_medicalclinicid_cleaned.csv"


class Config:
    """Base configuration shared across environments."""

    # Path to the hospital dataset (CSV). Overridable via the DATA_FILE env var.
    DATA_FILE: Path = Path(os.environ.get("DATA_FILE", str(DEFAULT_DATA_FILE)))

    # Number of rows rendered on first page load.
    INITIAL_RESULTS: int = int(os.environ.get("INITIAL_RESULTS", "50"))

    # Maximum number of matches returned by a single search request.
    MAX_SEARCH_RESULTS: int = int(os.environ.get("MAX_SEARCH_RESULTS", "100"))

    # Flask secret key. A throwaway default is fine for this read-only app,
    # but it can be overridden in production via the environment.
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev-secret-key")
