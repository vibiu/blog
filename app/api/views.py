from flask import request

from . import api


@api.route('/comment', methods=['POST'])
def comment_post():
    return 'ok'
