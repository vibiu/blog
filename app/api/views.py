from flask import request, jsonify, abort
from .. models import Comment
from .. import db
from datetime import datetime

from . import api


@api.route('/comment', methods=['POST'])
def comment_post():
    if not request.method == 'POST':
        abort(400)
    request_content = request.get_json(True)
    comment = Comment()
    comment.body = request_content.get('body')
    comment.email = request_content.get('email')
    comment.timestamp = datetime.utcnow()
    try:
        db.session.add(comment)
        db.session.commit()
    except Exception:
        return jsonify({"message": "comment fail."}), 500
    return jsonify({"message": "comment success."}), 201
