import requests
from bs4 import BeautifulSoup


def search_xml(qwery):
    url = f'https://xmlstock.com/yandex/xml/?user=11362&key=2a81ea2bf46144411cc5e8c148f5fcfa&query={qwery}' \
          f'&groupby=attr%3D%22%22.mode%3Dflat.groups-on-page%3D100.docs-in-group%3D1'
    response = requests.get(url)
    dirty_list_link = BeautifulSoup(response.text, features="xml").find_all('url')
    list_link = [link.text.strip('</url>') for link in dirty_list_link]
    link_vi = []
    link_ku = []
    link_po = []
    for lnk in list_link:
        if 'vseinstrumenti.ru/product' in lnk and 'otzyvy' not in lnk:
            if len(link_vi) == 0:
                link_vi.append(lnk)
                link_vi = ''.join(link_vi)
        elif 'https://www.kuvalda.ru/' in lnk and '/product' in lnk:
            if len(link_ku) == 0:
                link_ku.append(lnk)
                link_ku = ''.join(link_ku)
        elif 'poryadok.ru' in lnk and lnk.count('/') > 4:
            if len(link_po) == 0:
                link_po.append(lnk)
                link_po = ''.join(link_po)

    return link_vi, link_ku, link_po



