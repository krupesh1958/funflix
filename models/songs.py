"""Create user for maintain profile for funflix."""
import enum

from config import db

class Choice(enum.Enum):
    """Sqlalchemy utils for choice class"""
    english = 1
    hindi = 2


class Songs(db.Model):
    """
    A table to stores songs details.

    Table stores songs details and songs stored on
    hadoop distributed file system (HDFS).
    """
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=40), nullable=False)
    language = db.Column(db.Enum(Choice))
    artist_id = db.Column(
        "artist_id",
        db.ForeignKey("artist.id")
    )
    dfs_path = db.Column(db.String(length=50), nullable=False)
    picture_path = db.Column(db.String(length=50), nullable=False)


class Artist(db.Model):
    """
    A table to stores artis details.
    """
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=40), nullable=False)
    picture_path = db.Column(db.String(length=50), nullable=False)
