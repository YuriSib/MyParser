import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

#from gpt_help import gpt_helper


# def for_vi(html):
#     soup = BeautifulSoup(html, 'lxml')
#     div_element_name = soup.find_all('div', class_='mbBW2z')
#     div_element_value = soup.find_all('span', class_='typography text v2 -no-margin zUz8NX')
#
#     list_name = []
#     list_value = []
#
#     for row in div_element_name:
#         span_element_name = row.find('span', class_='typography text v2 -no-margin')
#         list_name.append(span_element_name.get_text(strip=True))
#
#     for row in div_element_value:
#         span_element_value = row.find('span')
#         list_value.append(span_element_value.get_text(strip=True))
#
#     block = [f'• {x} : {y} \n' for x, y in zip(list_name, list_value)]
#
#     return block
#
#
# def vi_photo(html):
#     photo_list = []
#     soup = BeautifulSoup(html, 'lxml')
#
#     div_element_name_1 = soup.find('div', class_='item -selectable -active')
#
#     if div_element_name_1 is not None:
#         link_to_the_photo = div_element_name_1.find('a')['href']
#         photo_list.append(link_to_the_photo)
#         div_element_names = soup.find_all('div', class_='item -selectable')
#         for element in div_element_names:
#             link = element.find('a')
#             if link:
#                 photo_list.append(link['href'])
#     else:
#         photo_list = ['Изображение не найдено']
#
#     return photo_list
#

# def for_po(html):
#     soup = BeautifulSoup(html, 'lxml')
#     descriptions = soup.find('div', {'itemprop': 'description'}).find_all('li')
#     block = []
#     for description in descriptions:
#         block.append(('• ' + description.get_text(strip=True) + '\n'))
#
#     return block

#
# def po_photo(html):
#     photo_list = []
#     soup = BeautifulSoup(html, 'lxml')
#     link = soup.find('div', class_='col-12 col-md-7 col-lg-5 col-xl-5 product-image').find('img')['src']
#     photo_list.append(f'https:{link}')
#
#     return photo_list
#
#
# def for_ku(html):
#     soup = BeautifulSoup(html, 'lxml')
#     descriptions = soup.find('div', class_='product-specs__table').find_all('tr')
#     block = []
#     for description in descriptions:
#         text_list = description.find_all('td')
#         all_td = ''
#         count = 0
#         for text in text_list:
#             if count == 0:
#                 all_td += ('• ' + text.get_text(strip=True))
#             else:
#                 all_td += (' : ' + text.get_text(strip=True) + '\n')
#             count += 1
#         block.append(all_td)
#
#     return block
#
#
# def ku_photo(html):
#     photo_list = []
#     soup = BeautifulSoup(html, 'lxml')
#     link = soup.find('img')['src']
#     # link = soup.find('div', class_='product-gallery__slider-item swiper-slide swiper-slide-visible swiper-slide-active')
#     photo_list.append(f'https:{link}')
#
#     return photo_list


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
    specification_list = dirty_specification.strip('Описание товара')
    # specification_list = gpt_helper(dirty_specification)

    return photo_list, specification_list


def maguss_scrapper(url_):
    if '#reviews' in url_:
        url_ = url_.split('/')
        url_[-1] = '#props'
        url_ = '/'.join(url_)
    elif '#props' not in url_:
        url_ = url_ + '/#props'

    soup = useragent_soup(url_)

    html_photo_list = soup.find_all('div', {'class': 'product-detail-gallery__item product-detail-gallery__item--big '
                                                     'text-center'})
    photo_list = ['https://maguss.ru/' + photo.a['href'] for photo in html_photo_list]

    specification_ = str
    dirty_specifications = soup.find_all('tr', {'class': 'js-prop-replace'})
    if dirty_specifications:
        for specification in dirty_specifications:
            property_name = specification.find('div', {'class': 'props_item'}).get_text(strip=True)
            if 'трихкод' not in property_name and 'ренд' not in property_name and 'овары комплекта' not in property_name \
            and 'собенность_' not in property_name and 'од товара' not in property_name and 'наличии' not in property_name:
                property_value = specification.find('td', {'class': 'char_value'}).get_text(strip=True)
                property_ = f"• {property_name} : {property_value} \n"
                specification_ = f'{specification_} {property_}'
    else:
        specification_ = soup.find('div', {'class': 'content detail-text-wrap'})
        # specification_ = gpt_helper(html_specification_.get_text(strip=True)) if html_specification_ else specification_ is False

    return photo_list, specification_


def anytos_scrapper(url_):
    soup = useragent_soup(url_)

    html_photo = soup.find('div', {'id': 'anitos-catalog-element-photos'})
    photo_ = 'https://anytos.ru/' + html_photo.a['href']

    specifications = soup.find('div', {'class': 's7sbp--marketplace--catalog-element-detail-product--tabs--body--item '
                                               'active'}).get_text(strip=True)
    # specification_list = gpt_helper(specifications)
    # if '!DOCTYPE html' in specification_list:
    #     specification_list = gpt_helper(specifications)
    # if '!DOCTYPE html' in specification_list:
    #     specification_list = specifications

    return photo_, specifications


# def wb_master(url_):
#     soup = useragent_soup(url_)
#
#     html_photo = soup.find('div', {'class': 'zoom-image-container'})
#     photo_ = html_photo.img['src']
#
#     specifications = soup.find('div', {'class': 'collapsable__content j-description'}).get_text(strip=True)
#
#     return photo_, specifications


if __name__ == "__main__":
    url = 'https://www.wildberries.ru/catalog/180450715/detail.aspx'
    response = wb_master(url)
    print(response)
