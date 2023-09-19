"""Load music data in front-end"""
from flask import (
    render_template
)

from config import server
from models.user import User
from models.songs import Songs


@server.route('/music', methods=['POST', 'GET'])
def load_music():
    musics = Songs.query.all()
    return render_template('/load_music.html', context=musics)
