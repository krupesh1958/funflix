"""Load music data in front-end"""
from __future__ import annotations

from flask import jsonify

from config import server
from models.user import User
from models.songs import Songs


@server.route('/songs', methods=['POST', 'GET'])
def get_songs():
    songs = Songs.query.all()
    return jsonify(songs, status=201, mimetype="application/json")


@server.route('/playlist', methods=['POST', 'GET'])
def playlist():
    user_playlist = User.query.filter_by(id=1).first()

    # Bind linked list nodes.

    return jsonify()
