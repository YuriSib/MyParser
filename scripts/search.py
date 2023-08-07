import requests
from bs4 import BeautifulSoup

from import_from_excel import import_xl
from ya_search import list_of_requests


def search_xml(qwery):
    # url = f'http://xmlproxy.ru/search/xml?query={qwery}&groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D5.' \
    #       f'docs-in-group%3D3&maxpassages=3&page=1-15&user=itproj31%40gmail.com&key=aaaa12bc9d966caf7c4b66fc4fd0ac46'
    url = f'https://xmlstock.com/yandex/xml/?user=11362&key=2a81ea2bf46144411cc5e8c148f5fcfa&query={qwery}' \
          f'&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D50.docs-in-group%3D1'
    response = requests.get(url)
    dirty_list_link = BeautifulSoup(response.text, features="xml").find_all('url')
    list_link = [link.text.strip('</url>') for link in dirty_list_link]
    link_vi = []
    link_ym = []
    for lnk in list_link:
        if 'vseinstrumenti.ru/product' in lnk and 'otzyvy' not in lnk:
            if len(link_vi) == 0:
                link_vi.append(lnk)
                link_vi = ''.join(link_vi)
        elif 'market.yandex.ru/product--' in lnk:
            if len(link_ym) == 0:
                link_ym.append(lnk)
                link_ym = ''.join(link_ym)

    return link_vi, link_ym


# table = 'Ключи.xlsx'
# qwery = import_xl(table, 5, 6)
# code_qwery = list_of_requests(qwery)
#
# test1, test2 = search_xml(code_qwery)
# print(qwery)
# print(test1, test2)


