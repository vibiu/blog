#!/usr/bin/env python
# coding: utf-8

import os
import flask
from app import create_app, db
from flask_script import Manager, Shell, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)

manage.add_command('shell', Shell(make_contextmake_shell_context))


@manager.command
def createall():
    db.create_all()


@manager.command
def dropall():
    db.dropall()

if __name__ == '__main__':
    manage.run()
