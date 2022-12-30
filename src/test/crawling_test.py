import unittest
from crawl import crawling
from config import *

def add(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    
    def setUp(self):
        self.crawling = crawling.CrawlingManager(BASE_URL, DEFAULT_SEARCH_KEYWORD, hidden_browser_option=True)
    
    def test_search_file(self):
        self.crawling.start_crawling(1, 1)
        
        
if __name__ == '__mainn__':
    unittest.main()