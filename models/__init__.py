"""Funflix models."""
from __future__ import annotations


def import_all_models() -> None:
    """
    Importing songs, users and artist models.
    """
    import models.songs
    import models.user
