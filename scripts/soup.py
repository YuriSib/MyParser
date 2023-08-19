from bs4 import BeautifulSoup


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

    if div_element_name_1 is not None:
        link_to_the_photo = div_element_name_1.find('a')['href']
        photo_list.append(link_to_the_photo)
        div_element_names = soup.find_all('div', class_='item -selectable')
        for element in div_element_names:
            link = element.find('a')
            if link:
                photo_list.append(link['href'])
    else:
        photo_list = ['Изображение не найдено']

    return photo_list


def for_po(html):
    soup = BeautifulSoup(html, 'lxml')
    descriptions = soup.find('div', {'itemprop': 'description'}).find_all('li')
    block = []
    for description in descriptions:
        block.append(('• ' + description.get_text(strip=True) + '\n'))

    return block


def po_photo(html):
    photo_list = []
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find('div', class_='col-12 col-md-7 col-lg-5 col-xl-5 product-image').find('img')['src']
    photo_list.append(f'https:{link}')

    return photo_list


def for_ku(html):
    soup = BeautifulSoup(html, 'lxml')
    descriptions = soup.find('div', class_='product-specs__table').find_all('tr')
    block = []
    for description in descriptions:
        text_list = description.find_all('td')
        all_td = []
        count = 0
        for text in text_list:
            if count == 0:
                all_td.append('• ' + text)
            else:
                all_td.append((' : ' + text + '\n'))
        block.extend(all_td)

    return block


def ku_photo(html):
    photo_list = []
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find('div', class_='product-gallery__slider-item '
                                   'swiper-slide swiper-slide-visible swiper-slide-active').find('img')['src']
    photo_list.append(f'https:{link}')

    return photo_list
