from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)
base_url = 'https://www.dlm1947.com'
search_keyword = '6i7'


data = {}

def save(key: str, value): 
    if key not in data:
        data[key] = []
    
    data[key].append(value)
    
def move_to(url: str, wait_time: int=5) -> bs:
    driver.get(url)
    driver.implicitly_wait(wait_time)
    return bs(driver.page_source, features='html.parser')

try:
    for page in range(1, 2):
        print(f'페이지#{page} 진행 중...')
        url = base_url + f'/goods/goods_search.php?keyword={search_keyword}&x=0&y=0&recentCount=10&page={page}'
        soup = move_to(url)
        
        products = soup.select('div.item_gallery_type > ul > li')
        products_size = len(products)
        
        for idx, product in enumerate(products):
            print(f'페이지#{page} {idx+1}/{products_size}')
            
            link = base_url + product.select_one('a').attrs['href'][2:]
            title = product.select_one('div > div.item_info_cont > div.item_tit_box > a > strong').get_text().strip()
            # 타이틀 [] 삭제
            title = re.sub('\[(.*?)\]', '', title).strip()
            product_name = ' '.join(title.split()[:-2])
            product_num = title.split()[-1]
            regular_price = product.select_one('del').get_text().strip()
            sale_price = product.select_one('strong.item_price').get_text().strip()
            image = product.select_one('img').attrs['data-original'].strip()
            
            # 상품 세부 항목으로 이동
            detail_soup = move_to(link, wait_time=3)
            
            color_options = detail_soup.find('select', {'name': 'optionNo_0'}).find_all('option')
            colors = []
            for color_option in color_options:
                color_value = color_option.attrs['value']
                if color_value:
                    colors.append(color_value)
            
            detail_images = []
            imgs = detail_soup.find('div', {'class': 'txt-manual'}).find_all('img')
            for img in imgs:
                src: str = img.attrs['src']
                if 'product' in src:
                    detail_images.append(src)
            
            
            save('link', link)
            save('title', f'엘르골프-{product_name}-{product_num}')
            save('product_title', f'{product_name}-{product_num}')
            save('product_num', product_num)
            save('regular_price', regular_price)
            save('sale_price', sale_price)
            save('image', image)
            save('color', ','.join(colors))
            save('detail_image', ','.join(detail_images))
except Exception as e: 
    print(e)

driver.close()
print('크롤링 종료')

save_file_name = f'{search_keyword}.csv'
print(f'{save_file_name} 파일 저장')
pd.DataFrame(data).to_csv(save_file_name, encoding='utf-8-sig')