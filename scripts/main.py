from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException

from import_from_excel import import_xl
from ya_search import list_of_requests
from search import search_xml
from html_master import html_obj
from soup import for_vi, vi_photo
from export_in_excel import export_excel, quantity_row


def main(table, start, finish):
    qwery_list = list_of_requests(import_xl(table, start, finish))
    link_list = []
    for qwery in qwery_list:
        vi, ym = search_xml(qwery)
        link_list.append(vi)

    list_html = []
    counter = start
    for link in link_list:
        if link != []:
            html = html_obj(link)
            list_html.append(html)
        else:
            html = 0
            list_html.append(0)

        if html != 0:
            specifications = for_vi(html)
            export_excel(table, specifications, 2, counter)
            photos = vi_photo(html)
            export_excel(table, photos, 3, counter)
        else:
            export_excel(table, '0', 2, counter)
            export_excel(table, '0', 3, counter)
        counter += 1

    return 'Программа выполнена успешно!'


path_in_table = 'Биты, адаптеры.xlsx'

start_ = 364
for i in range(1):
    try:
        test = main(path_in_table, start_, start_ + 1)
        start_ += 1
    except SessionNotCreatedException:
        print(f'Ошибка создания сессии WebDriver на {start_}-й строчке!')
        test = main(path_in_table, start_, start_ + 1)
        start_ += 1

