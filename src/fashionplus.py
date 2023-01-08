from bs4 import BeautifulSoup as bs
import os
import pandas as pd
import json
import re
import requests
from crawl.driver import DriverManager
from io import BytesIO
from PIL import Image
from datetime import datetime

from config import *

BASE_URL = 'https://seller.fashionplus.co.kr/login'


driver = DriverManager(BASE_URL, hidden_browser_option=False)

save_data = {}


def save(key, value):
    if key not in save_data:
        save_data[key] = []

    save_data[key].append(value)


def login(id, password):
    login_type = driver.find_select_element_by_id('loginType')
    login_type.select_by_index(1)   # 브랜드 관리자로 변경

    # 아이디, 패스워드 입력
    driver.find_element_by_id('loginId').send_keys(id)
    driver.find_element_by_id('loginPassword').send_keys(password)

    # 로그인 버튼 클릭
    driver.find_element_by_id('btn_login').click()


def get_color(source):
    soup = bs(source, features='html.parser')
    table = soup.find('tbody', {'id': 'option_box'})
    rows = table.find_all('tr')
    color = [row.find_all('td')[1].find('b').get_text() for row in rows]
    return ','.join(set(color))


def get_category(source):
    soup = bs(source, features='html.parser')
    category_box = soup.find('dd', {'id': 'selected_category_box'})
    categorys = category_box.find_all('li')
    category_list = [category.find('span').get_text()
                     for category in categorys]
    return ','.join(category_list)


def save_img(source, product_code):
    soup = bs(source, features='html.parser')
    file_list = soup.find(
        'div', {'class': 'mm_image-list'}).attrs['data-filelist']
    json_object = json.loads(file_list.replace("\'", "\""))
    urls = json_object['items']
    urls = map(lambda url: url.split('?')[0], urls)

    for url in urls:
        res = requests.get(url)
        if res.ok:
            split_url = url.split('/')
            image_name = split_url[-1]
            if not os.path.isdir('img'):
                os.mkdir('img')
            if not os.path.isdir(f'img/{product_code}'):
                os.mkdir(f'img/{product_code}')
            # 이미지 저장
            Image.open(BytesIO(res.content)).save(
                f'img/{product_code}/{image_name}')
    pass


def start_crawling(productIDs):
    for productID in productIDs:
        driver.move_to(
            f'https://seller.fashionplus.co.kr/goods/edit/{productID}')

        # 요소 추출
        product_code = driver.find_element_by_id(
            'goods_code').get_attribute('value')
        product_name = driver.find_element_by_id(
            'goods_name').get_attribute('value')
        goods_price = driver.find_element_by_id(
            'goods_price').get_attribute('value')
        goods_salesprice = driver.find_element_by_id(
            'goods_salesprice').get_attribute('value')
        goods_display_name = driver.find_element_by_id(
            'goods_display_name').get_attribute('value')
        goods_content = driver.find_element_by_id('goods_content_source').text
        category = get_category(driver.page_source)
        product_color = get_color(driver.page_source)
        print(product_code, product_name, goods_price, goods_salesprice,
              goods_display_name, product_name, goods_content, product_color, category)
        with open('source.txt', 'w') as f:
            f.write(driver.page_source)
        save_img(driver.page_source, product_code)

        save('상품코드', product_code)
        save('상품이름', product_name)
        save('소비자단가', goods_price)
        save('판매가', goods_salesprice)
        save('진열상품명', goods_display_name)
        save('상세설명', goods_content)
        save('색깔', product_color)
        save('카테고리', category)


def action_register_product(product):
    product_code = product['상품코드']
    product_category = product['카테고리']
    os.startfile(f'img\\{product_code}')
    print(f'타입: {product_category}')
    register_product(product, '68')


def action_request_size():
    print('제품을 보고 상품 사이즈를 입력하세요')
    print(f'- {KEY_MAN_UP_SIZE}: 남자 상의')
    print(f'- {KEY_MAN_BOTTOM_SIZE}: 남자 하의')
    print(f'- {KEY_WOMAN_UP_SIZE}: 여자 상의')
    print(f'- {KEY_WOMAN_BOTTOM_SIZE}: 여자 하의')
    print(f'- {KEY_HAT_SIZE}: 모자류')
    print(f'- {KEY_ETC_SIZE}: 악세사리')
    print(f'- {KEY_QUIT}: 입력하지 않기')
    while True:
        user_input = input('입력: ')
        if not user_input.isdigit:
            continue
        user_input = int(user_input)
        if not user_input in SIZE_DATA_SET.keys():
            continue

        size_data = SIZE_DATA_SET[user_input]
        if not size_data:
            break
        insert_size(size_data)
        break


def register_product(product, code_prefix: str = ''):
    driver.move_to('https://seller.fashionplus.co.kr/goods/create')

    product_code = product['상품코드']
    product_name = product['상품이름']
    if code_prefix:
        product_code += f'-{code_prefix}'
        product_name += f'-{code_prefix}'
    driver.find_select_element_by_id('seller_id').select_by_index(1)
    driver.insert_text_to_element_by_id('goods_code', product_code)
    driver.insert_text_to_element_by_id('goods_name', product_name)
    driver.insert_text_to_element_by_id('goods_price', str(product['소비자단가']))
    driver.insert_text_to_element_by_id(
        'goods_salesprice', str(product['판매가']))
    driver.insert_text_to_element_by_id('goods_display_name', product['진열상품명'])
    driver.insert_text_to_element_by_id(
        'goods_content_source', product['상세설명'])
    driver.insert_text_to_element_by_id('option1_concat', product['색깔'])
    try:
        for category in product['카테고리'].split(','):
            category1, category2, category3 = category.split('>')
            category1_btns = driver.find_elements_by_class('category1_btn')
            for btn in category1_btns:
                text = btn.get_attribute('innerText')
                if text == category1.strip():
                    btn.click()
            category2_btns = driver.find_elements_by_class('category2_btn')
            for btn in category2_btns:
                text = btn.get_attribute('innerText')
                if text == category2.strip():
                    btn.click()
            category3_btns = driver.find_elements_by_class('category3_btn')
            for btn in category3_btns:
                text = btn.get_attribute('innerText')
                if text == category3.strip():
                    btn.click()
            driver.find_element_by_class('btn_add').click()
    except:
        pass


def insert_size(size: str):
    if driver.url != 'https://seller.fashionplus.co.kr/goods/create':
        return

    driver.find_element_by_id('option2_concat').send_keys(size)


def save_history(product):
    file_name = 'history.csv'
    data = {
        '상품코드': product['상품코드'],
        '상품이름': product['상품이름'],
        '등록날짜': datetime.now()
    }
    try:
        history: pd.DataFrame = pd.read_csv(file_name)
        history =history.append(data, ignore_index=True)
        history.to_csv(file_name)
    except:        
        pd.DataFrame(data, index=[0]).to_csv(file_name)


if __name__ == '__main__':
    # with open('source.txt', 'r') as f:
    #     source = f.read()
    #     get_category(source)

    # 아이디, 패스워드 입력
    id = input('아이디: ')
    password = input('패스워드: ')
    login(id, password)

    action_type = input('크롤링?상품등록?')

    if action_type == '크롤링':
        # 새 탭
        driver.make_new_tab()
        driver.switch_to_tab(-1)

        data = pd.read_csv('./data/data.csv')
        productIDs = data['품목ID']
        start_crawling(productIDs)
        print('크롤링 끝')
        pd.DataFrame(save_data).to_csv('products.csv', encoding='utf-8-sig')
        print('products.csv 저장 성공')
    elif action_type == '상품등록':
        data = pd.read_csv('products.csv')
        # 중복 데이터 제거
        try:
            products_uploaded = pd.read_csv('./data/data68.csv')
            products_num_uploaded = map(lambda code: code.split(
                '_')[1].split('-')[0], products_uploaded['품목번호'])
            products_num_not_uploaded = set.difference(
                set(map(lambda s: s[:7], data['상품코드'])),
                set(products_num_uploaded))
            unique_products = data['상품코드'].map(lambda x: any(
                string in x for string in products_num_not_uploaded))
            print('아래와 같은 상품들이 제외되었습니다. (사유: 중복 코드)')
            print(data[~unique_products]['상품코드'])
            data = data[unique_products]
            data = data.reset_index()
        except:
            print('중복 데이터 로직 검증 실패')
            pass
        index = 0

        while True:
            product = data.loc[index]
            product_name = product['상품이름']
            is_history = False
            try:
                history = pd.read_csv('history.csv')
                is_history = any(history['상품코드'].isin([product['상품코드']]))
            except:
                pass
            
            str_is_history = 'O' if is_history else 'X'
            print('================================================')
            print(f'상품이름: {product_name}   ({index+1}/{len(data)})     ({str_is_history})')
            print('선택해주세요')
            print('- y: 제품등록')
            print('- z: 이전 상품')
            print('- x: 다음 상품')
            print('- s: 사이즈 입력')
            select = input(f'선택: ')
            if select == 'y':
                action_register_product(product)
                action_request_size()
                save_history(product)
            elif select == 'z':
                if index == 0:
                    continue
                index -= 1
            elif select == 'x':
                if index >= len(data) - 1:
                    continue
                index += 1
            elif select == 's':
                action_request_size()
            else:
                print('잘못된 입력입니다.')

    input()
