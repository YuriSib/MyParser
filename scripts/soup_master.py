import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from gpt_help import gpt_helper


def useragent_soup(url_):
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    response = requests.get(url_, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def fkniga_scrapper(url_):
    soup = useragent_soup(url_)

    html_photo_list = soup.find('div', {'class': 'swiper-wrapper'}).find_all('div', {'class': 'swiper-slide'})
    photo_list = ['https://fkniga.ru/' + photo.select_one('.MagicZoom')['href'] for photo in html_photo_list]

    dirty_specification = soup.find('div', {'class': 'section section--descriptionArticle'}).get_text(strip=True)
    dirty_specification = dirty_specification.strip('Описание товара')
    specification_ = gpt_helper(dirty_specification)

    return photo_list, specification_


def maguss_scrapper(url_):
    url_ = url_.split('/')
    url_[-1] = '#props'
    url_ = '/'.join(url_)

    soup = useragent_soup(url_)

    html_photo_list = soup.find_all('div', {'class': 'product-detail-gallery__item product-detail-gallery__item--big '
                                                     'text-center'})
    photo_list = ['https://maguss.ru/' + photo.a['href'] for photo in html_photo_list]

    specification_ = str
    dirty_specifications = soup.find_all('tr', {'class': 'js-prop-replace'})
    for specification in dirty_specifications:
        property_name = specification.find('div', {'class': 'props_item'}).get_text(strip=True)
        if 'трихкод' not in property_name and 'ренд' not in property_name and 'овары комплекта' not in property_name \
        and 'собенность_' not in property_name and 'од товара' not in property_name and 'наличии' not in property_name:
            property_value = specification.find('td', {'class': 'char_value'}).get_text(strip=True)
            property_ = f"• {property_name} : {property_value} \n"
            specification_ = f'{specification_} {property_}'

    return photo_list, specification_


url = 'https://maguss.ru/catalog/299676/#desc'
result, specification_ = maguss_scrapper(url)
print(specification_)

