"""HTTP routes for the hospital search engine."""

from __future__ import annotations

import time

from flask import Blueprint, current_app, jsonify, render_template, request

from .data import load_dataset
from .search import search_hospitals

bp = Blueprint("hospitals", __name__)


def _get_dataset():
    """Load the dataset using the path configured on the current app."""
    return load_dataset(str(current_app.config["DATA_FILE"]))


@bp.route("/")
def index():
    """Render the search page with an initial set of records."""
    frame = _get_dataset()
    limit = current_app.config["INITIAL_RESULTS"]
    results = frame.head(limit).to_dict(orient="records")
    return render_template("index.html", results=results, total=len(frame))


@bp.route("/api/search")
def api_search():
    """Return hospitals matching a query as JSON.

    Query parameters:
        query: The free-text search term (optional).
    """
    query = request.args.get("query", "")
    limit = current_app.config["MAX_SEARCH_RESULTS"]

    frame = _get_dataset()
    started = time.perf_counter()
    results = search_hospitals(frame, query, limit)
    elapsed_ms = (time.perf_counter() - started) * 1000

    return jsonify(
        {
            "query": query,
            "count": len(results),
            "processing_time_ms": round(elapsed_ms, 2),
            "results": results,
        }
    )
