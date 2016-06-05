# coding: utf-8

import os
import re
import json
from datetime import datetime
from functools import wraps

from flask import request, jsonify, abort, session, make_response
from .. models import Comment, Article, Book, Course
from .. import db

from markdown import markdown
from render import splite_code
from mail163 import LoginUser, jsonfy_mail_info
from library import Libook


from . import api

# import logging
# path = '/'.join([os.path.dirname(__file__), 'api.log'])
# logging.basicConfig(
#     filename=path, filemode='wb', level=logging.DEBUG)

# logging.warn(path)


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers[
            'Access-Control-Allow-Methods'] = 'POST, GET, '\
            'PUT, PATCH, DELETE, OPTIONS'
        allow_headers = 'Referer,Accept,Origin,User-Agent,'\
            'Content-Type, X-Requested-With'
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


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
@allow_cross_domain
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
@allow_cross_domain
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
@allow_cross_domain
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


@api.route('/lib/info', methods=['GET'])
@allow_cross_domain
def lib_search():
    table = {
        'callnum': '索书号',
        'barcode': '条码号',
        'year': '   年卷期',
        'location': '校区—馆藏地',
        'status': '书刊状态'
    }
    marc_no = request.args.get('marc_no')
    if marc_no and re.match(r'\d{10}', marc_no):
        book = Book.query.filter_by(marc_no=marc_no).first()
    else:
        return jsonify({'message': 'Bad request'}), 400

    if book:
        time_diff = datetime.now() - book.timestamp
        diff = time_diff.total_seconds()
    else:
        info, lib = Libook(marc_no).get_book()
        book_info = {
            'table': table,
            'info': info,
            'lib': lib
        }
        timestamp = datetime.now()
        book = Book(
            marc_no=marc_no,
            content=unicode(json.dumps(book_info)),
            timestamp=timestamp)
        db.session.add(book)
        db.session.commit()
        return jsonify({'book': book_info}), 200

    if diff < 3600:
        book_info = json.loads(book.content)
        return jsonify({'book': book_info}), 200
    else:
        info, lib = Libook(marc_no).get_book()
        book_info = {
            'table': table,
            'info': info,
            'lib': lib
        }
        timestamp = datetime.now()
        book.content = unicode(json.dumps(book_info))
        book.timestamp = timestamp
        db.session.add(book)
        db.session.commit()
        return jsonify({'book': book_info}), 200


@api.route('/course/info', methods=['GET'])
@allow_cross_domain
def query_course():
    page = request.args.get('page') or 0
    step = request.args.get('step') or 10
    all_course = Course.query.all()
    total = len(all_course)

    if int(page) is not 0:
        try:
            start = (int(page) - 1) * int(step)
            end = int(page) * int(step)
            all_course = all_course[start:end]
        except IndexError as e:
            print e

    filter_fun = lambda course: {
        'id': course.id,
        'classify': course.classify,
        'topic': course.topic,
        'teacher': course.teacher,
        'introduction': course.introduction,
        'form': course.form,
        'frequency': course.frequency,
        'dispass': course.dispass
    }
    course_list = [filter_fun(course) for course in all_course]
    return jsonify(
        courses=course_list,
        total=total,
        message=u'获取成功',
        status=1), 200
