from flask import request, jsonify, render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')
