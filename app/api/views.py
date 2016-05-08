from flask import request, jsonify, abort
from markdown import markdown
from .. models import Comment, Article
from .. import db
from datetime import datetime
from render import splite_code

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


@api.route('/markdown', methods=['GET'])
def markdown_get():
    markdown_article = Article.query.first()
    parsed_markdown = markdown(markdown_article.body)
    beautify_markdown = splite_code(parsed_markdown)
    # return parsed_markdown, 200
    return beautify_markdown, 200
