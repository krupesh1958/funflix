# -*- coding: utf-8 -*-
"""
Extensions module. Each extension is initialized in the app
factory located in app.py
"""
from __future__ import annotations

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


alchemy = SQLAlchemy()
migrate = Migrate()

__all__ = [
    "annotations",
    "Flask",
    "migrate",
    "alchemy",
]
