from flask import jsonify

from .. models import Article
from .import rest


@rest.route('/', methods=['GET'])
def rest_start():
    return jsonify({'message': 'try to be restful!'})


@rest.route('/article', methods=['GET'])
def get_articles():
    article_list = []
    articles = Article.query.all()
    for article in articles:
        article_info = {
            'id': article.id,
            'title': article.title,
            'time': article.timestamp,
        }
        article_list.append(article_info)
    return jsonify({
        'articles': article_list,
        'message': 'success.',
        'status': 0
    })
