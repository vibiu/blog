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

def save_mkd():
    with open('main.md', 'r') as mkd_open:
        mkd_open_read = mkd_open.read().decode('utf-8')
        mkd_article = Article()
        mkd_article.body = mkd_open_read
        mkd_article.title = 'main'
        mkd_article.topic = 'aboutme'
        mkd_article.timestamp = datetime.utcnow()

        session.add(mkd_article)
        session.commit()
        print 'ok'

basedir = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
datadir = '/'.join(['sqlite://', basedir, 'data.sqlite'])
engine = create_engine(datadir)

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    save_mkd()
