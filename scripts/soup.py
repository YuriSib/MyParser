from bs4 import BeautifulSoup


def for_ya_search(html):
    soup = BeautifulSoup(html, 'lxml')
    link_list = []
    blocks = soup.find_all('div', class_='Organic') #.find('a', class_='link')
    for block in blocks:
        link = block.find('a', class_='link').get('href')
        if 'vseinstrumenti.ru' in link or 'market.yandex.ru' in link:
            link_list.append(link)
    return link_list


def for_vi(html):
    soup = BeautifulSoup(html, 'lxml')
    div_element_name = soup.find_all('div', class_='mbBW2z')
    div_element_value = soup.find_all('div', class_='WUiBXs')

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


def for_ya_m():
    pass