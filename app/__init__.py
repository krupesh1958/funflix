"""Initialize all views apis"""
from __future__ import annotations

def import_all_apis() -> None:
    """Initialize all apis"""
    from app.views import get_songs
    from app.views import playlist
