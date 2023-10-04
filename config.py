"""
Impliment funflix application with flask framework.
Flask configuration.
"""
import os

from app.models import *
from app.api import home
from app.extensions import (
    Flask,
    alchemy,
    migrate
)

__author__ = "https://github.com/Krupeshgithub?tab=repositories"
__verions__ = '0.1'

server = Flask(__name__)

server.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("MYSQL_URL"),
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)


# Database configurations
alchemy.init_app(server)
migrate.init_app(server, alchemy)


# Bind all backend end points in 
# flask application with blueprint
server.register_blueprint(
    blueprint=home,
    url_prefix="/api/v1/"
)
