from crawling import CrawlingManager

base_url = 'https://www.dlm1947.com'
default_search_keyword = '6i7'
default_start_page = 1
default_end_page = 5


if __name__ == '__main__':
    print(f'{base_url} 사이트 크롤링 시작')
    input_search_keyword = input(f'사용할 검색어 (default: {default_search_keyword}): ')
    if input_search_keyword:
        search_keyword = input_search_keyword
    else:
        search_keyword = default_search_keyword
    search_keyword = input_search_keyword if input_search_keyword else default_search_keyword
    
    input_start_page = input(f'시작 페이지 (default: {default_start_page}): ')
    input_end_page = input(f'종료 페이지 (default: {default_end_page}): ')
    start_page = int(input_start_page) if input_start_page else default_start_page
    end_page = int(input_end_page) if input_end_page else default_end_page
    
    crawlingManager = CrawlingManager(base_url, search_keyword, hidden_browser_option=True)
    print('크롤링 시작')
    crawlingManager.start_crawling(
        start_page=start_page, 
        end_page=end_page
    )
    crawlingManager.save_csv()