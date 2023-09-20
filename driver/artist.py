#!/usr/bin/env python3
"""Driver code to add artist or delete and other functionality related artist."""
from __future__ import annotations

from models.songs import Artist


def create_artist_profile():
    """
    Create single Artist profile

    :rtype: None
    """
    artist_obj = Artist()
    _dict = {
        "name": "Atif Asalam",
        "picture_path": "/artist/pictures/",
    }
    artist_obj.set_artist(**_dict)
    return

create_artist_profile()
