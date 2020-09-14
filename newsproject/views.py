from flask import render_template
from newsproject.request import News
from newsproject import app
newsAPI = News()


@app.route('/')
def index():
    top_headlines = newsAPI.get_top_headlines(None)
    business_news = newsAPI.get_top_headlines('business', language='en')
    health_news = newsAPI.get_top_headlines('health')
    sports_news = newsAPI.get_top_headlines('sports')

    # return  top_headlines
    return render_template('home.html', top_headlines=top_headlines['articles'],
                           business_news=business_news['articles'],
                           sports_news=sports_news['articles'],
                           health_news=health_news['articles'])


@app.route('/top')
def json_response():
    return newsAPI.get_sources()

