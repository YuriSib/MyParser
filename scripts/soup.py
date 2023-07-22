from bs4 import BeautifulSoup


def for_ya_search(html):
    soup = BeautifulSoup(html, 'lxml')
    link = ''
    blocks = soup.find_all('div', class_='Organic') #.find('a', class_='link')
    for block in blocks:
        if 'vseinstrumenti.ru' in block.text:
            link = block.text
        # if 'vseinstrumenti.ru' in block.text or 'market.yandex.ru' in block.text:
        #     link_list.append(block.find('a')['href'])

    return link


def for_goo_search(html):
    soup = BeautifulSoup(html, 'lxml')
    link = ''
    blocks = soup.find_all('div', class_='yuRUbf')# .find('a', class_='link')
    for block in blocks:
        if 'vseinstrumenti.ru' in block.text:
            link = block.text
        # if 'vseinstrumenti.ru' in block.text or 'market.yandex.ru' in block.text:
        #     link_list.append(block.find('a')['href'])

    return link


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

    block = [f'{x} : {y}' for x, y in zip(list_name, list_value)]

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


def for_ya_m():
    pass


# html1 = html_obj('https://www.google.com/search?q=%D0%90%D0%B4%D0%B0%D0%BF%D1%82%D0%B5%D1%80+STAYER+%D0%B3%D0%B8%D0%B1%D0%BA%D0%B8%D0%B9%2C+400%D0%BC%D0%BC+25512-40&hl=Ru&sxsrf=AB5stBjC2iRUFCnjB93GmH-IBBlK6Ln0yA%3A1689947159093&ei=F4y6ZPejBYfBgAb95504&ved=0ahUKEwi3i-3g95-AAxWHIMAKHf1zBwcQ4dUDCA8&oq=%D0%90%D0%B4%D0%B0%D0%BF%D1%82%D0%B5%D1%80+STAYER+%D0%B3%D0%B8%D0%B1%D0%BA%D0%B8%D0%B9%2C+400%D0%BC%D0%BC+25512-40&gs_lp=Egxnd3Mtd2l6LXNlcnAiNNCQ0LTQsNC_0YLQtdGAIFNUQVlFUiDQs9C40LHQutC40LksIDQwMNC80LwgMjU1MTItNDAyBRAhGKABMgUQIRigATIFECEYoAFI5ihQAFjnJnAAeACQAQCYAfgCoAGmBqoBBTItMi4xuAEMyAEA-AEC-AEB4gMEGAAgQYgGAQ&sclient=gws-wiz-serp')
#
# test = for_goo_search(html1)
# print(test)
