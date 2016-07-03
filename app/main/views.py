from flask import request, jsonify, render_template, abort
from .. models import Article
from .. import db

from . import main


# this is for markdown parse init
import houdini as h
import misaka as m
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name


class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(
                h.escape_html(text.strip()))

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(text, lexer, formatter)

renderer = HighlighterRenderer()
md = m.Markdown(renderer, extensions=('fenced-code',))
# end init for markdown


@main.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@main.route('/archive', methods=['GET'])
def archive():
    # return render_template('archive.html')
    return render_template('index.html')


@main.route('/categories', methods=['GET'])
def categories():
    # return render_template('categories.html')
    return render_template('index.html')


@main.route('/pages', methods=['GET'])
def pages():
    # return render_template('tags.html')
    return render_template('index.html')


@main.route('/tags', methods=['GET'])
def tags():
    # return render_template('tags.html')
    return render_template('index.html')


@main.route('/article/<int:id>', methods=['GET'])
def article(id):
    article = Article.query.filter_by(id=id).first()
    if article:
        count = Article.query.count()
        body = md(article.body)
        return render_template('article.html',
                               article=article, count=count, body=body)
    else:
        abort(404)
