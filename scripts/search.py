import requests
from bs4 import BeautifulSoup

from ya_search import list_of_requests

def search_xml():
    url = 'http://xmlproxy.ru/search/xml?query=' \
          '%D0%A1%D1%82%D0%B5%D0%BA%D0%BB%D0%BE%D1%80%D0%B5%D0%B7%201-' \
          '%D1%80%D0%BE%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9%20STARTUL%20PROFI%20ST4960-01&' \
          'groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D5.docs-in-group%3D3&maxpassages=3&page=1-15&' \
          'user=itproj31%40gmail.com&key=aaaa12bc9d966caf7c4b66fc4fd0ac46'
    response = requests.get(url)
    print(response.text)
    a = BeautifulSoup(response.text, features="xml")
    print(a.find_all('url'))

    return a


test = search_xml()