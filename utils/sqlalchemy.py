"""For modules use case."""
from __future__ import annotations

import pendulum

from sqlalchemy import TIMESTAMP
from sqlalchemy.types import TypeDecorator

utc = pendulum.tz.timezone("UTC")


class UtcDateTime(TypeDecorator):
    """
    Similar to :class:`~sqlalchemy.types.TIMESTAMP` with `timezone=True` option, with some differences.

    - Unlike SQLAlchemy's built-in :class:`~sqlalchemy.types.TIMESTAMP`,
      it never return naive :class:`~datetime.datetime`, but time zone
      aware value, even with SQLite or MySQL.
    - Always returns TIMESTAMP in UTC.
    """
    impl = TIMESTAMP(timezone=True)
