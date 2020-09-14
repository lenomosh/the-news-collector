from flask import Blueprint, render_template
from newsproject.request import News

news_article_blueprint = Blueprint('news_article', __name__, template_folder='templates/news_article')


@news_article_blueprint.route('/<category>')
def article_category(category):
    n = News().get_top_headlines(category)
    return render_template('category.html', news=n['articles'], title=category)
