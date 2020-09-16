from flask import Blueprint, render_template
from newsproject.request import News

news_source_blueprint = Blueprint('news_source', __name__, template_folder='templates/news_source')


@news_source_blueprint.route('/')
def index():
    sources = News().get_sources()

    return render_template('index2.html', sources=sources['sources'])


@news_source_blueprint.route('/<name>')
def source_articles(name):
    articles = News().get_top_headlines(sources=name)
    # return  articles
    return render_template('sources.news.view.html', articles=articles['articles'])
