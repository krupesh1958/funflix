"""Create user for maintain profile for funflix."""
import enum
import sqlalchemy as sa


class Choice(enum.Enum):
    """Sqlalchemy utils for choice class"""
    english = 1
    hindi = 2


class Songs:
    """
    A table to stores songs details.

    Table stores songs details and songs stored on
    hadoop distributed file system (HDFS).
    """
    __tablename__ = "songs"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(length=40), nullable=False)
    language = sa.Column(sa.Enum(Choice))
    artist_id = sa.Column(
        "artist_id",
        sa.ForeignKey("artist.id")
    )
    dfs_path = sa.Column(sa.String(length=50), nullable=False)
    picture_path = sa.Column(sa.String(length=50), nullable=False)


class Artist:
    """
    A table to stores artis details.
    """
    __tablename__ = "artist"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(length=40), nullable=False)
    picture_path = sa.Column(sa.String(length=50), nullable=False)
