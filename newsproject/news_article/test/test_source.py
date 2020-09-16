import unittest
from newsproject.models import Source


class TestArticle(unittest.TestCase):

    def setUp(self):
        '''
        SetUp method that will run before every Test
        '''
        # (self, category, country, description, id, language, name, url):
        return Source("general", "us",
                      "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos "
                      "at ABCNews.com.",
                      "abc-news", "en", "ABC News", "https://abcnews.go.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.setUp(), Source))


if __name__ == '__main__':
    unittest.main()
