#!/usr/bin/env python3
"""Driver code to add songs, del songs & more functionalitys with hdfs path."""
from __future__ import annotations

from models.songs import Songs


class _Songs:
    """A class create, delete or update songs"""


    def __init__(
        self,
        name,
        language,
        artist_id,
        dfs_path,
        picture_path
    ):
        """
        Initialize songs properties
        
        :type name: str
        :type language: str
        :type artist_id: int
        :type dfs_path: url | any
        :type picture_path: url | any
        :rtype: None
        """
        self.name = name
        self.language = language
        self.artist_id = artist_id
        self.dfs_path = dfs_path
        self.picture_path = picture_path


    def insert_song(self):
        """Set single song"""
        song = Songs()
        _dict = {
            "name": self.name,
            "language": self.language,
            "artist_id": self.artist_id,
            "dfs_path": self.dfs_path,
            "picture_path": self.picture_path
        }
        song.set_song(**_dict)
        return

# For create data
"""
sg = _Songs(
    name="Maan meri jaan",
    language="hindi",
    artist_id=1,
    dfs_path="/songs/song_2.mp3",  # hdfs (Hadoop distributed file system) path
    picture_path="/songs_pics/song_pic_1.jpeg"  # hdfs (Hadoop distributed file system) path
)
sg.insert_song()
"""
