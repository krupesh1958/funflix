"""Create user for maintain profile for funflix."""
import datetime

from config import db


class User(db.Model):
    """
    A table store user data.
    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=25), nullable=False)
    email = db.Column(db.String(length=25), nullable=False)
    access_token = db.Column(db.String(250), default=None)
    multi_playlist = db.Column(
        db.String(250),
        default=None
    )
    dob = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        nullable=False
    )
