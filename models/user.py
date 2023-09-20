"""Create user model for maintain profile for funflix."""
from __future__ import annotations

import datetime

from config import db, server


class User(db.Model):
    """
    A table store user data.
    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=25), nullable=False)
    email = db.Column(db.String(length=25), nullable=False)
    access_token = db.Column(db.String(250), default=None)
    dob = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        nullable=False
    )
    multi_playlist = db.Column(
        db.String(250),
        default=None
    )


    def set_user(self, **kwargs):
        """
        This function add any single user

        >>> kwargs = {
            "name": username,
            "email": user_email,
            "access_token": auth_token,
            "dob": date_of_birth,
            "multi_playlist": {
                "Happy Hits": list(songs_id), 
                "Indie Mix": list(songs_id)
            }
        }
        >>> set_user(**kwargs)
        "success"

        :type kwargs: dict
        :rtype: str
        """
        with server.app_context():
            user_data: tuple(User) = User(
                name=kwargs.get("name", None),
                email=kwargs.get("email", None),
                access_token=kwargs.get("access_token", None),
                dob=kwargs.get("dob", None),
                multi_playlist=str(kwargs.get("multi_playlist", None))
            )
            assert None not in user_data.__dict__, "All field are required."

            db.session.add(user_data)
            db.session.commit()
            return "success", 201, {}
