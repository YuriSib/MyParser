import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

from analiz_category import compare_similarity
from html_master import sima_master, relefopt_master, yandex_market_master, ozon_master
from soup_master import fkniga_scrapper, maguss_scrapper, anytos_scrapper, wb_master


def search_xml(qwery):
    product = quote(qwery)
    url = f'https://xmlstock.com/yandex/xml/?user=11362&key=2a81ea2bf46144411cc5e8c148f5fcfa&query=' \
          f'{product}&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D30.docs-in-group%3D1'
    response = requests.get(url)
    dirty_list_link = BeautifulSoup(response.text, features="xml").find_all('url')
    list_link = [link.text.strip('</url>') for link in dirty_list_link]

    dirty_list_name = BeautifulSoup(response.text, features="xml").find_all('title')

    list_name = [name.get_text() for name in dirty_list_name]
    filtered_list_name = compare_similarity(qwery, list_name)
    name_and_index_list = [(item, list_name.index(item[0])) for item in filtered_list_name]
    filtered_link_list = [list_link[item[1]] for item in name_and_index_list]

    for filtered_link in filtered_link_list:
        if 'maguss' in filtered_link:
            image_list, property_list = maguss_scrapper(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'fkniga' in filtered_link:
            image_list, property_list = fkniga_scrapper(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'anytos' in filtered_link:
            image_list, property_list = anytos_scrapper(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'wildberries' in filtered_link or 'WildBerries' in filtered_link:
            image_list, property_list = wb_master(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'SIMA-LAND' in filtered_link or 'sima-land' in filtered_link:
            image_list, property_list = sima_master(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'relefopt' in filtered_link:
            image_list, property_list = relefopt_master(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'ozon' in filtered_link:
            image_list, property_list = ozon_master(filtered_link)
            if property_list:
                return image_list, property_list

        elif 'yandex' in filtered_link:
            image_list, property_list = yandex_market_master(filtered_link)
            if property_list:
                return image_list, property_list


