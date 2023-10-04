"""Load music data in front-end"""
from __future__ import annotations

from app.models import *

from flask import (
    Blueprint,
    render_template
)


home = Blueprint("home", __name__)

@home.route('/', methods=['POST', 'GET'])
def get_songs():
    songs = Songs.query.all()

    from algorithms.doubly_linked_list import DoublyLinkedList

    dll = DoublyLinkedList()

    # Link all songs withing a linked-list.
    for itr in songs:
        dll.insert_at_tail(itr.id)

    return render_template(
        "load_music.html",
    )


@home.route('/playlist', methods=['POST', 'GET'])
def playlist():
    user_playlist = User.query.filter_by(id=1).first()

    print(user_playlist)
    return render_template()
