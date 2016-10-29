# -*- coidng: utf-8 -*-


import requests
import lxml
import os
from flask import jsonify
from bs4 import BeautifulSoup


def weekends():
    try:
        index_r = requests.get('https://www.mafengwo.cn/cy/10133/tese.html').text
    except:
        with open('/'.join(os.path.abspath('index.html').split('/')[:-1]+['app', 'spiders', 'index.html'])) as f:
            index_r = ''.join(f.readlines())

    index_soup = BeautifulSoup(index_r, 'lxml')

    food_reco = []
    shop_reco = []

    # Get top foods
    top_foods_list = index_soup.select('[class~=top-guide-list]')
    top_foods = top_foods_list[0]
    foods_list = top_foods.find_all('li')

    for food in foods_list:
        food_url = ''.join(['https://www.mafengwo.cn', food.find_all('a')[0]['href']])
        food_img = food.find_all('a')[0].find_all('img')[0]['src']
        food_name = food.find_all('a')[0].select('[class~=mask]')[0].find('h3').string
        food_liked = food.find_all('a')[0].select('[class~=mask]')[0].span.strings.next()

        food_reco.append({
            'food_url': food_url,
            'food_img': food_img,
            'food_name': food_name,
            'food_liked': food_liked
            })

    # Get top shops
    top_shops_list = index_soup.select('[class~=poi-list]')
    top_shops = top_shops_list[0]
    shops_list = top_shops.find_all('li')

    for shop in shops_list:
        shop_url = ''.join(['https://www.mafengwo.cn', shop.h3.a['href']])
        shop_img = shop.a.img['src']
        shop_name = shop.h3.a.text
        shop_point = shop.em.text

        shop_reco.append({
            'shop_url': shop_url,
            'shop_img': shop_img,
            'shop_name': shop_name,
            'shop_point': shop_point
            })

    result = jsonify({'food_reco': food_reco, 'shop_reco': shop_reco})
    return result
