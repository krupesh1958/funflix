"""
Impliment funflix application with flask framework.
Flask configuration.
"""
from __future__ import annotations

import os

from typing import Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import import_all_models

__verions__ = '0.1'

server = Flask(__name__)

server.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("MYSQL_URL"),
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

db = SQLAlchemy(server)
Migrate(server, db)
import_all_models()
