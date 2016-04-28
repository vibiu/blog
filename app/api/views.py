from flask import request, jsonify
from .. models import

from . import api


@api.route('/comment', methods=['POST'])
def comment_post():
    return 'ok'
