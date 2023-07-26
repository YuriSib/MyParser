from bs4 import BeautifulSoup

# from html_master import html_obj
# from import_from_excel import import_xl
# from ya_search import list_of_requests
# from search import search_xml

# def for_ya_search(html):
#     soup = BeautifulSoup(html, 'lxml')
#     link = ''
#     blocks = soup.find_all('div', class_='Organic') #.find('a', class_='link')
#     for block in blocks:
#         if 'vseinstrumenti.ru' in block.text:
#             link = block.text
#         # if 'vseinstrumenti.ru' in block.text or 'market.yandex.ru' in block.text:
#         #     link_list.append(block.find('a')['href'])
#
#     return link
#
#
# def for_goo_search(html):
#     soup = BeautifulSoup(html, 'lxml')
#     link = ''
#     blocks = soup.find_all('div', class_='yuRUbf')# .find('a', class_='link')
#     for block in blocks:
#         if 'vseinstrumenti.ru' in block.text:
#             link = block.text
#         # if 'vseinstrumenti.ru' in block.text or 'market.yandex.ru' in block.text:
#         #     link_list.append(block.find('a')['href'])
#
#     return link


def for_vi(html):
    soup = BeautifulSoup(html, 'lxml')
    div_element_name = soup.find_all('div', class_='mbBW2z')
    div_element_value = soup.find_all('span', class_='typography text v2 -no-margin zUz8NX')

    list_name = []
    list_value = []

    for row in div_element_name:
        span_element_name = row.find('span', class_='typography text v2 -no-margin')
        list_name.append(span_element_name.get_text(strip=True))

    for row in div_element_value:
        span_element_value = row.find('span')
        list_value.append(span_element_value.get_text(strip=True))

    block = [f'• {x} : {y} \n' for x, y in zip(list_name, list_value)]

    return block


def vi_photo(html):
    photo_list = []
    soup = BeautifulSoup(html, 'lxml')

    div_element_name_1 = soup.find('div', class_='item -selectable -active')

    link_to_the_photo = div_element_name_1.find('a')['href']
    photo_list.append(link_to_the_photo)

    div_element_names = soup.find_all('div', class_='item -selectable')

    for element in div_element_names:
        link = element.find('a')
        if link:
            photo_list.append(link['href'])

    return photo_list


# def for_ya_m(table):
#     specifications = []
#     qwery_list = list_of_requests(import_xl(table))
#     for qwery in qwery_list:
#         vi, ym = search_xml(qwery)
#         html = html_obj(ym)
#         soup = BeautifulSoup(html, 'lxml')
#         div_element_name_1 = soup.find('div', class_='_1AayP')
#         specifications.append(div_element_name_1.get_text(strip=True))
#
#     return specifications
#
#
# def ya_m_photo(table):
#     photo_list = []
#     qwery_list = list_of_requests(import_xl(table))
#     for qwery in qwery_list:
#         vi, ym = search_xml(qwery)
#         html = html_obj(ym)
#         soup = BeautifulSoup(html, 'lxml')
#         div_element_name_1 = soup.find('div', class_='_3Wp6V')
#         photo_list.append(div_element_name_1)
#
#     return photo_list
#
#
# table_ = 'Стеклорезы.xlsx'
# test = for_ya_m(table_)
# print(test)
