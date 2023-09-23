"""Load music data in front-end"""
from __future__ import annotations

from flask import jsonify

from config import server
from models.user import User
from models.songs import Songs



@server.route('/songs', methods=['POST', 'GET'])
def get_songs():
    songs = Songs.query.all()

    # Import traversal algorithm
    from algorithms.doubly_linked_list import DoublyLinkedList

    dll = DoublyLinkedList()

    # Link all songs withing a linked-list.
    for itr in songs:
        dll.insert_at_tail(itr.id)
   
    return jsonify(songs, status=201, mimetype="application/json")


@server.route('/playlist', methods=['POST', 'GET'])
def playlist():
    user_playlist = User.query.filter_by(id=1).first()

    print(user_playlist)
    return jsonify()
