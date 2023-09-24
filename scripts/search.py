import requests
from bs4 import BeautifulSoup


def search_xml(qwery):
    url = f'https://xmlstock.com/yandex/xml/?user=11362&key=2a81ea2bf46144411cc5e8c148f5fcfa&query={qwery}' \
          f'&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D50.docs-in-group%3D1'
    response = requests.get(url)
    dirty_list_link = BeautifulSoup(response.text, features="xml").find_all('url')
    list_link = [link.text.strip('</url>') for link in dirty_list_link]

    sima_link = []
    ozon_link = []
    for lnk in list_link:
        # if 'https://www.OZON.ru/product/' in lnk or 'https://www.ozon.ru/product/' in lnk:
        #     ozon_link.append(lnk)
        if 'https://www.sima-land.ru/' in lnk or 'https://www.SIMA-LAND.ru/' in lnk:
            sima_link.append(lnk)
        elif 'https://fkniga.ru/catalog/' in lnk:
            pass

    return sima_link
