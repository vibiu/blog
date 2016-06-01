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


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    marc_no = db.Column(db.Unicode(10), index=True)
    content = db.Column(db.Unicode(2048))
    timestamp = db.Column(db.DateTime)


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    classify = db.Column(db.String(64))
    topic = db.Column(db.String(64))
    teacher = db.Column(db.String(64))
    introduction = db.Column(db.Text)
    form = db.Column(db.String(64))
    frequency = db.Column(db.String(64))
    dispass = db.Column(db.String(64))
