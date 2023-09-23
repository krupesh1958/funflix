"""
Impliment funflix application with flask framework.
Flask configuration.
"""
from __future__ import annotations

import os
import redis

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import import_all_models
from app import import_all_apis

__verions__ = '0.1'

server = Flask(__name__)

server.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("MYSQL_URL"),
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

# Database configurations
db = SQLAlchemy(server)
Migrate(server, db)
import_all_models()

# Cofig all apis
import_all_apis()

# Flask redis
redist_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    decode_responses=True
)
