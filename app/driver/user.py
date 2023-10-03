#!/usr/bin/env python3
"""Driver code to add user or delete and other functionality related user."""
from __future__ import annotations

import datetime

from app.models import User


def create_user():
    """Creating single user"""
    user = User()
    _dict = {
        "name": "krupesh",
        "email": "krupesh.patel@yudiz.com",
        "access_token": "ochgkATmUTfXNRG3tyc6RuOCr=eD99ToA2c!YuNxDZ?LZms/KTyUe2!2luh?61a5aXh!e/Mj8h8ki2" +
                        "!U0VhBYToUj2za=6FLFsv8ne?JQWkFk--IyaYOo1Qdr93kCEKGA?c4Ng3BLqv?lhzDQtrU1E/0eGclsG",
        "dob": datetime.datetime(1999, 7, 12, 12, 12, 0),
        "multi_playlist": {
            "Happy Hits": [0, 1, 2, 3, 4]
        }
    }
    user.set_user(**_dict)

create_user()
