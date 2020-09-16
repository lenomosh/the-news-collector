import unittest
# import sys
# sys.path.append('.')
from newsproject.models import Article
class TestArticle(unittest.TestCase):


    def setUp(self):
        '''
        SetUp method that will run before every Test
        '''
        return Article("David Leonhardt","College students returning to campuses around the country face a dilemma: to snitch or not to snitch?\r\nSome students are feeling pressure to tell university administrators if they see their classmate… [+970 chars]","And what else you need to know today","2020-09-02T10:34:41Z","New York Times","Trump, Unbound","https://www.nytimes.com/2020/09/02/briefing/ed-markey-jet-pack-khmer-rouge-your-wednesday-briefing.html","https://static01.nyt.com/images/2020/09/01/us/2ambriefing-promo/2ambriefing-trump-facebookJumbo-v2.jpg")

    def test_instance(self):
        self.assertTrue(isinstance(self.setUp(), Article))


if __name__ == '__main__':
    unittest.main()