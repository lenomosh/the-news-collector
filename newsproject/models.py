class Article:
    def __init__(self, author, content, description, publishedAt, source, title, url, urlToImage):
        self.author = author
        self.content = content
        self.description = description
        self.publishedAt = publishedAt
        self.source = source
        self.title = title
        self.url = url
        self.urlToImage = urlToImage


class Source:
    def __init__(self, category, country, description, id, language, name, url):
        self.category = category
        self.country = country
        self.description = description
        self.id = id
        self.language = language
        self.name = name
        self.url = url
