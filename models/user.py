"""Create user for maintain profile for funflix."""
import sqlalchemy as sa

from funflix.utils.sqlalchemy import UtcDateTime
from funflix.utils.timezone import utcnow

class User:
    """
    A table store user data.
    """

    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(length=25), nullable=False)
    email = sa.Column(sa.String(length=25), nullable=False)
    dob = sa.Column(UtcDateTime, default=utcnow, nullable=False)
    access_token = sa.Column(sa.String(250), default=None)
