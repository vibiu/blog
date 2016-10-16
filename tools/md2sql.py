# coding: utf-8
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

basedir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
datadir = '/'.join(['sqlite://', basedir, 'data.sqlite'])
engine = create_engine(datadir)

Session = sessionmaker(bind=engine)
session = Session()


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    body = Column(Unicode(256))
    timestamp = Column(DateTime, index=True)
    email = Column(Unicode(128))


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(64))
    topic = Column(Unicode(64))
    body = Column(Unicode(1024))
    timestamp = Column(DateTime, index=True)


def query_mkd(title, topic):
    article = session.query(Article).filter_by(title=title).first()
    print(article.body)
    print('title:', article.title)
    print('topic:', article.topic)


def save_mkd(file, title, topic):
    path = '/'.join(['article', file])
    with open(path, 'r') as mkd_open:
        mkd_open_read = mkd_open.read()
        mkd_article = Article()
        mkd_article.body = mkd_open_read
        mkd_article.title = title
        mkd_article.topic = topic
        mkd_article.timestamp = datetime.utcnow()

        session.add(mkd_article)
        session.commit()
        print('create ok!')


def update_mkd(file, title, topic):
    article = session.query(Article).filter_by(title=title).first()
    path = '/'.join(['article', file])
    with open(path, 'r') as new_mkd:
        new_mkd_read = new_mkd.read()
    import pdb
    pdb.set_trace()
    article.body = new_mkd_read
    article.title = title
    article.topic = topic
    session.add(article)
    session.commit()
    print('update ok!')


def list_save():
    pass


if __name__ == '__main__':
    # save_mkd('main.md', u'序言', 'main')
    save_mkd('awesome.md', u'Awesome Github Project', u'bookmark')
    save_mkd('philosophy.md', u'Program Philosophy', u'thoughts')
    save_mkd('sublime.md', 'Python Coding in Sublime', 'sublime')
    # update_mkd('main.md', u'序言', u'main')
    # update_mkd('sublime.md', u'Python Coding in Sublime', u'sublime')
    # query_mkd(u'序言', 'main')
    pass
