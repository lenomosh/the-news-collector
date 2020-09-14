from newsapi import NewsApiClient
from newsproject import app
from newsproject.models import Article,Source


class News:
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=fe0577b9a2f64260a0f3286c2467bff2"
    news_api = NewsApiClient(api_key=app.config.get('API_KEY'))

    def get_top_headlines(self, category=None, **kwargs):
        # print(**kwargs)
        top_headlines: dict
        if category is None:
            top_headlines = self.news_api.get_top_headlines(**kwargs)
        else:
            top_headlines = self.news_api.get_top_headlines(category=category, country='us', **kwargs)

        response = dict(articles=[])
        for article in top_headlines['articles']:
            response['articles'].append(Article(**article).__dict__)
        return response

    def get_news(self, **kwargs):
        return self.news_api.get_everything(**kwargs)

    def get_sources(self, **kwargs):
        response: dict = self.news_api.get_sources(country='us',**kwargs)
        sources: dict = dict(sources=[])
        if response['sources']:
            for source in response['sources']:
                sources['sources'].append(Source(**source).__dict__)
        return sources