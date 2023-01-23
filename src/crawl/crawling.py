from bs4 import BeautifulSoup as bs
import os
import pandas as pd
from crawling_gagip import DriverManager

from utils import *
from config import *


class CrawlingManager():
    """
    크롤링 매니저
    """

    def __init__(self, base_url: str, search_keyword: str, hidden_browser_option: bool):
        self.driver = DriverManager(base_url, hidden_browser_option=hidden_browser_option)
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
                    info = self.__get_common_info(product)
                    print(
                        f'페이지#{page} {idx+1}/{products_size}: {info[KEY_TITLE]}'
                    )

                    # 상품 세부 항목으로 이동
                    detail_soup = self.__move_to(info[KEY_LINK], wait_time=3)
                    info[KEY_COLORS] = self.__get_colors(detail_soup)
                    info[KEY_DETAIL_IMAGES_LINK] = self.__get_detail_images(
                        detail_soup)

                    self.__save_info(info)
        except Exception as e:
            print(e)
            print('크롤링 도중 문제가 생겼습니다.')

        self.driver.close()
        print('크롤링 종료')

    def save_csv(self, dir_name):
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        save_file_name = os.path.join(dir_name, f'{self.search_keyword}.csv')
        print(f'{save_file_name} 파일 저장')
        pd.DataFrame(self.data).to_csv(save_file_name, encoding='utf-8-sig')

    def __get_common_info(self, product):
        info = {}
        title = self.__get_title(product)
        info[KEY_TITLE] = title
        info[KEY_LINK] = self.__get_link(product)
        info[KEY_PRODUCT_NAME] = ' '.join(title.split()[:-1])
        info[KEY_PRODUCT_NUM] = title.split()[-1]
        info[KEY_REGULAR_PRICE] = self.__get_regular_price(product)
        info[KEY_SALE_PRICE] = self.__get_sale_price(product)
        info[KEY_IMAGE_LINK] = self.__get_image(product)
        return info

    def __save_info(self, info):
        link = info[KEY_LINK]
        product_name = info[KEY_PRODUCT_NAME]
        product_num = info[KEY_PRODUCT_NUM]
        title = f'엘르골프-{product_name}-{product_num}'
        regular_price = info[KEY_REGULAR_PRICE]
        sale_price = info[KEY_SALE_PRICE]
        image = info[KEY_IMAGE_LINK]
        colors = ','.join(info[KEY_COLORS])
        detail_images = ','.join(info[KEY_DETAIL_IMAGES_LINK])

        self.__save(KEY_LINK, link)
        self.__save(KEY_TITLE, title)
        self.__save(KEY_PRODUCT_NAME, f'{product_name}-{product_num}')
        self.__save(KEY_PRODUCT_NUM, product_num)
        self.__save(KEY_REGULAR_PRICE, regular_price)
        self.__save(KEY_SALE_PRICE, sale_price)
        self.__save(KEY_IMAGE_LINK, image)
        self.__save(KEY_COLORS, colors)
        self.__save(KEY_DETAIL_IMAGES_LINK, detail_images)

    def __save(self, key, value):
        if key not in self.data:
            self.data[key] = []

        self.data[key].append(value)

    def __move_to(self, url, wait_time=5) -> bs:
        self.driver.move_to(url, wait_time=wait_time)
        return bs(self.driver.page_source, features='html.parser')

    def __get_link(self, product):
        return self.base_url + product.select_one('a').attrs['href'][2:]

    def __get_title(self, product):
        title = product.select_one(
            'div > div.item_info_cont > div.item_tit_box > a > strong'
        ).get_text().strip()
        # 타이틀 [] 삭제
        return to_string_removed_square_brackets(title).strip()

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
        colors = [to_string_removed_parentheses(color_option.attrs['value'])
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
