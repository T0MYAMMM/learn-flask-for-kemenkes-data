"""Vercel serverless entry point.

Vercel's @vercel/python builder imports the ``app`` object from this module.
The real application lives in the ``hospital_search`` package under ``src/``;
this file only wires the import path and exposes the WSGI app.
"""

from __future__ import annotations

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

from hospital_search import create_app  # noqa: E402

app = create_app()
