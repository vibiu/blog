from . import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Unicode(256))
    timestamp = db.Column(db.Datetime, index=True)
    email = db.Column(db.Unicode(128))
