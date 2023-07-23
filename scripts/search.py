import requests
from bs4 import BeautifulSoup


def search_xml(qwery):
    url = f'http://xmlproxy.ru/search/xml?query={qwery}&groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D5.' \
          f'docs-in-group%3D3&maxpassages=3&page=1-15&user=itproj31%40gmail.com&key=aaaa12bc9d966caf7c4b66fc4fd0ac46'
    response = requests.get(url)
    dirty_list_link = BeautifulSoup(response.text, features="xml").find_all('url')
    list_link = [link.text.strip('</url>') for link in dirty_list_link]
    link = []
    for lnk in list_link:
        if 'www.vseinstrumenti.ru/product' in lnk and 'otzyvy' not in lnk:
            link.append(lnk)
    if len(link) == 1:
        link = ''.join(link)

    return link


# qwery = '%D0%A1%D1%82%D0%B5%D0%BA%D0%BB%D0%BE%D1%80%D0%B5%D0%B7%201-%D1%80%D0%BE%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D1%8' \
#         'B%D0%B9%20STARTUL%20PROFI%20ST4960-01'
# test = search_xml(qwery)
# print(test)
