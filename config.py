"""
Impliment funflix application with flask framework.
Flask configuration.
"""
from __future__ import annotations

import os
import json
import sys
import unittest

from flask import Flask
from alembic import op


__verions__ = '0.1'

server = Flask(__name__)

server.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("MYSQL_URL"),
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)


def build_table():
    """
    We import all tables from models 
    and use alembic commands to build tables.
    """
    from models import import_all_models
    
    op.create_table()
    

op.create_table()