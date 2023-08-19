import requests

from import_from_excel import import_xl
from ya_search import list_of_requests
from search import search_xml
from html_master import html_obj
from soup import for_vi, vi_photo, for_po, po_photo, for_ku, ku_photo
from export_in_excel import export_excel, quantity_row


def main(table, start, finish):
    qwery = list_of_requests(import_xl(table, start, finish))

    link_vi, link_ku, link_po = search_xml(qwery)
    counter = start
    if link_vi:
        html = html_obj(link_vi)
        specifications = for_vi(html)
        export_excel(table, specifications, 2, counter)
        photos = vi_photo(html)
        export_excel(table, photos, 3, counter)
    elif link_po:
        html = requests.get(link_po).text
        specifications = for_po(html)
        export_excel(table, specifications, 2, counter)
        photos = po_photo(html)
        export_excel(table, photos, 3, counter)
    elif link_ku:
        html = requests.get(link_ku).text
        specifications = for_po(html)
        export_excel(table, specifications, 2, counter)
        photos = ku_photo(html)
        export_excel(table, photos, 3, counter)
    else:
        export_excel(table, '0', 2, counter)
        export_excel(table, '0', 3, counter)
    counter += 1

    return 'Программа выполнена успешно!'


path_in_table = 'Электроды, припой.xlsx'

start_ = 78
for i in range(10):
    try:
        test = main(path_in_table, start_, start_ + 1)
        start_ += 1
        print(start_)
    except Exception:
        print(f'Неизвестная ошибка!')
        test = main(path_in_table, start_, start_ + 1)
        start_ += 1

