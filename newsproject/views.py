from flask import render_template, request
from newsproject.request import News
from newsproject import app

newsAPI = News()


@app.route('/')
def index():
    top_headlines = newsAPI.get_top_headlines(None)
    business_news = newsAPI.get_top_headlines('business', language='en')
    health_news = newsAPI.get_top_headlines('health')
    sports_news = newsAPI.get_top_headlines('sports', country='gb')

    return render_template('home.html', top_headlines=top_headlines['articles'],
                           business_news=business_news['articles'],
                           sports_news=sports_news['articles'],
                           health_news=health_news['articles'])


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search')
    result = News().get_news(q=query)
    return result


@app.route('/src')
def src():
    return newsAPI.get_sources()
