from crawling import CrawlingManager

base_url = 'https://www.dlm1947.com'
search_keyword = '6i7'

if __name__ == '__main__':
    crawlingManager = CrawlingManager(base_url, search_keyword, hidden_browser_option=True)
    crawlingManager.start_crawling(start_page=1, end_page=1)
    crawlingManager.save_csv()