from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import re

def to_numeric(string):
    return re.sub(r'[^0-9]', '', string)

class CrawlingManager():

    def __init__(self, base_url: str, search_keyword: str, hidden_browser_option: bool):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        # 창 숨기는 옵션
        if hidden_browser_option: 
            self.options.add_argument("headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.set_window_size(1920, 1080)
        self.base_url = base_url
        self.search_keyword = search_keyword
        self.data = {}

    def start_crawling(self, start_page=1, end_page=99):
        try:
            for page in range(start_page, end_page+1):
                print(f'페이지#{page} 진행 중...')
                url = self.base_url + \
                    f'/goods/goods_search.php?keyword={self.search_keyword}&x=0&y=0&recentCount=10&page={page}'
                soup = self.__move_to(url)

                products = soup.select('div.item_gallery_type > ul > li')
                products_size = len(products)

                for idx, product in enumerate(products):
                    title = self.__get_title(product)
                    link = self.__get_link(product)
                    product_name = ' '.join(title.split()[:-2])
                    product_num = title.split()[-1]
                    regular_price = self.__get_regular_price(product)
                    sale_price = self.__get_sale_price(product)
                    image = self.__get_image(product)
                    print(f'페이지#{page} {idx+1}/{products_size}: {title}')

                    # 상품 세부 항목으로 이동
                    detail_soup = self.__move_to(link, wait_time=3)
                    colors = self.__get_colors(detail_soup)
                    detail_images = self.__get_detail_images(detail_soup)

                    self.__save('link', link)
                    self.__save('title', f'엘르골프-{product_name}-{product_num}')
                    self.__save('product_title',
                                f'{product_name}-{product_num}')
                    self.__save('product_num', product_num)
                    self.__save('regular_price', regular_price)
                    self.__save('sale_price', sale_price)
                    self.__save('image', image)
                    self.__save('color', ','.join(colors))
                    self.__save('detail_image', ','.join(detail_images))
        except Exception as e:
            print(e)

        self.driver.close()
        print('크롤링 종료')

    def save_csv(self):
        save_file_name = f'{self.search_keyword}.csv'
        print(f'{save_file_name} 파일 저장')
        pd.DataFrame(self.data).to_csv(save_file_name, encoding='utf-8-sig')

    def __save(self, key, value):
        if key not in self.data:
            self.data[key] = []

        self.data[key].append(value)

    def __move_to(self, url, wait_time=5) -> bs:
        self.driver.get(url)
        self.driver.implicitly_wait(wait_time)
        return bs(self.driver.page_source, features='html.parser')

    def __get_link(self, product):
        return self.base_url + product.select_one('a').attrs['href'][2:]

    def __get_title(self, product):
        title = product.select_one(
            'div > div.item_info_cont > div.item_tit_box > a > strong'
        ).get_text().strip()
        # 타이틀 [] 삭제
        return re.sub('\[(.*?)\]', '', title).strip()

    def __get_regular_price(self, product):
        regular_price = product.select_one('del').get_text().strip()
        return to_numeric(regular_price)

    def __get_sale_price(self, product):
        sale_price = product.select_one(
            'strong.item_price').get_text().strip()
        return to_numeric(sale_price)

    def __get_image(self, product):
        return product.select_one(
            'img').attrs['data-original'].strip()

    def __get_colors(self, soup):
        color_options = soup.find(
            'select', {'name': 'optionNo_0'}).find_all('option')
        colors = [color_option.attrs['value']
                  for color_option in color_options 
                  if color_option.attrs['value']]
        return colors

    def __get_detail_images(self, soup):
        imgs = soup.find(
            'div', {'class': 'txt-manual'}).find_all('img')
        detail_images = [img.attrs['src'] 
                         for img in imgs 
                         if 'product' in img.attrs['src']]
        return detail_images