from flask import request, jsonify, render_template
from .. models import Article
from .. import db

from . import main


@main.route('/', methods=['GET'])
def index():
    markdown_object = Article.query.first()
    if markdown_object:
        markdown_content = markdown_object.body
    else:
        markdown_content = "No content"
    return render_template('index.html', markdown_content=markdown_content)
