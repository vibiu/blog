from flask import request, jsonify, render_template, abort
from .. models import Article
from .. import db

from . import main

from markdown import markdown


@main.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@main.route('/archive', methods=['GET'])
def archive():
    # return render_template('archive.html')
    return render_template('index.html')


@main.route('/categories', methods=['GET'])
def categories():
    # return render_template('categories.html')
    return render_template('index.html')


@main.route('/pages', methods=['GET'])
def pages():
    # return render_template('tags.html')
    return render_template('index.html')


@main.route('/tags', methods=['GET'])
def tags():
    # return render_template('tags.html')
    return render_template('index.html')


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = Article.query.filter_by(id=id).first()
    if article:
        count = Article.query.count()
        article.body = markdown(article.body.decode('utf-8'))
        return render_template('article.html', article=article, count=count)
    else:
        abort(404)
