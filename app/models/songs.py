"""Create user for maintain profile for funflix."""
import enum

from app.extensions import alchemy as db


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


    def set_song(self, **kwargs):
        """
        A method to add single song

        >>> kwargs = {
            "name": song_name,
            "language": language,
            "artist_id": artist_id,
            "dfs_path": dfs_path,
            "picture_path": picture_path
        }
        >>> set_songs(**kwargs)
        "success"

        :type kwargs: dict
        :rtype: str
        """
        songs: tuple(Songs) = Songs(
            name=kwargs.get("name", None),
            language=kwargs.get("language", None),
            artist_id=kwargs.get("artist_id", None),
            dfs_path=kwargs.get("dfs_path", None),
            picture_path=kwargs.get("picture_path", None)
        )
        assert None not in songs.__dict__, "All field are required."

        db.session.add(songs)
        db.session.commit()
        return "success", 201, {}
        

    def set_songs(self, songs):
        """
        A method to multiple song

        :type songs: list(tuple)
        :type kwargs: dict
        :rtype: str
        """
        assert not isinstance(songs, list), "param require in list"

        db.session.add_all(songs)
        db.session.commit()
        return "success", 201, {}


class Artist(db.Model):
    """
    A table to stores artis details.
    """
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=40), nullable=False)
    picture_path = db.Column(db.String(length=50), nullable=False)


    def set_artist(self, **kwargs):
        """
        A method insert artist data

        >>> kwargs = {
            "name": song_name,
            "picture_path": picture_path,
        }
        >>> set_songs(**kwargs)
        "success"

        :type kwargs: dict
        :rtype: str
        """
        artist: tuple(Artist) = Artist(
            name=kwargs.get("name", None),
            picture_path=kwargs.get("picture_path", None)
        )
        assert None not in artist.__dict__, "All field are required."

        db.session.add(artist)
        db.session.commit()
        return "success", 201, {}
