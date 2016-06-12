# coding: utf-8
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


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
    print article.body
    print 'title:', article.title
    print 'topic:', article.topic


def save_mkd(file, title, topic):
    with open(file, 'r') as mkd_open:
        mkd_open_read = mkd_open.read().decode('utf-8')
        mkd_article = Article()
        mkd_article.body = mkd_open_read
        mkd_article.title = title
        mkd_article.topic = topic
        mkd_article.timestamp = datetime.utcnow()

        session.add(mkd_article)
        session.commit()
        print 'create ok!'


def update_mkd(file, title, topic):
    article = session.query(Article).filter_by(title=title).first()
    print article.title
    with open(file, 'r') as new_mkd:
        new_mkd_read = new_mkd.read().decode('utf-8')
    article.body = new_mkd_read
    article.title = title
    article.topic = topic
    session.add(article)
    session.commit()
    print 'update ok!'


basedir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
datadir = '/'.join(['sqlite://', basedir, 'data.sqlite'])
engine = create_engine(datadir)

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    # save_mkd('main.md', u'序言', 'main')
    # save_mkd('awesome.md', u'Awesome Github Project', 'bookmark')
    # save_mkd('philosophy.md', u'Program Philosophy', 'thoughts')
    update_mkd('main.md', u'序言', 'main')
    # query_mkd(u'序言', 'main')
