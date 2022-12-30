import crawl
from crawl.crawling import CrawlingManager

from config import *


if __name__ == '__main__':
    print(f'{BASE_URL} 사이트 크롤링 시작')
    input_search_keyword = input(f'사용할 검색어 (default: {DEFAULT_SEARCH_KEYWORD}): ')
    if input_search_keyword:
        search_keyword = input_search_keyword
    else:
        search_keyword = DEFAULT_SEARCH_KEYWORD
    search_keyword = input_search_keyword if input_search_keyword else DEFAULT_SEARCH_KEYWORD
    
    input_start_page = input(f'시작 페이지 (default: {DEFAULT_START_PAGE}): ')
    input_end_page = input(f'종료 페이지 (default: {DEFAULT_END_PAGE}): ')
    start_page = int(input_start_page) if input_start_page else DEFAULT_START_PAGE
    end_page = int(input_end_page) if input_end_page else DEFAULT_END_PAGE
    
    crawlingManager = CrawlingManager(BASE_URL, search_keyword, hidden_browser_option=True)
    print('크롤링 시작')
    crawlingManager.start_crawling(
        start_page=start_page, 
        end_page=end_page
    )
    crawlingManager.save_csv(dir_name='data')