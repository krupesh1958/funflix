"""Impliment timzone"""
from __future__ import annotations

import datetime as dt

import pendulum

utc = pendulum.tz.timezone("UTC")


def utcnow() -> dt.datetime:
    """Get the current date and time in UTC."""
    result = dt.datetime.utcnow()
    result = result.replace(tzinfo=utc)

    return result
