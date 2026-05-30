"""Hospital search engine: a small Flask application over a CSV dataset."""

from __future__ import annotations

from flask import Flask

from .config import Config
from .routes import bp


def create_app(config: type[Config] = Config) -> Flask:
    """Application factory.

    Args:
        config: Configuration class to apply to the app.

    Returns:
        A configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(bp)
    return app


__all__ = ["create_app", "Config"]
