from flask import request, jsonify, render_template
from .. models import Article
from .. import db

from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
