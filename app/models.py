from . import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Unicode(256))
    timestamp = db.Column(db.DateTime, index=True)
    email = db.Column(db.Unicode(128))


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(64))
    topic = db.Column(db.Unicode(64))
    body = db.Column(db.Unicode(1024))
    timestamp = db.Column(db.DateTime, index=True)
