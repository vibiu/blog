from flask import request, jsonify, abort, session
from markdown import markdown
from .. models import Comment, Article
from .. import db
from datetime import datetime
from render import splite_code
from mail163 import LoginUser, jsonfy_mail_info

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


@api.route('/test/login', methods=['POST'])
def email_login():
    request_json = request.get_json()
    if request_json.get("username"):
        username = request_json.get("username")
    else:
        return jsonify({"error": "no username"}), 400
    if request_json.get("password"):
        password = request_json.get("password")
    else:
        return jsonify({"error": "no password"}), 400
    user = LoginUser(username, password)
    loginuser = user.login()
    if loginuser:
        session[username] = password
        return jsonify({"message": "login success"}), 200
    else:
        return jsonify({"message": "login fail, invalid password"}), 401


@api.route('/test/getmail', methods=['GET'])
def email_get():
    if request.args.get('username'):
        username = request.args.get('username')
    else:
        return jsonify({"message": "no username in query words"}), 400
    if session.get(username):
        user = LoginUser(username, session.get(username))
        loginuser = user.login()
        data = loginuser.get_mails_info().content
        email_list = jsonfy_mail_info(data)
    else:
        return jsonify({"message": "not login"}), 401
    return jsonify({"emails": email_list}), 200


@api.route('/test/logout', methods=['GET'])
def email_logout():
    if request.args.get('username'):
        username = request.args.get('username')
    else:
        return jsonify({"message": "no username in query words"}), 400
    if session.get(username):
        session.pop(username)
        return jsonify({"message": "logout success"}), 200
    else:
        return jsonify({"message": "please login first"}), 200


@api.route('/test/logoutall', methods=['GET'])
def email_logoutall():
    try:
        for username in session:
            session.pop(username)
        return jsonify({"message": "delete all login user done"}), 200
    except Exception as e:
        return jsonify({"message": "internal server error"}), 500
