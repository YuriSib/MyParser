from import_from_excel import import_xl
from ya_search import list_of_requests
from search import search_xml
from html_master import html_obj
from soup import for_vi, vi_photo, for_ya_m
from export_in_excel import export_excel, quantity_row



# def pars_in_vi():

# def search(first, second, int_):
#     html = html_obj(first, second)
#     link = for_goo_search(html) if int_ % 2 == 1 else for_ya_search(html)
#
#     return link
#     # link_list = []
#     # # first = 'https://www.google.com/search?q='
#     # # first = 'https://yandex.ru/search/?'
#     # second_list = list_of_requests()
#     # for second in second_list:
#     #     html = html_obj(first, second)
#     #     links = for_goo_search(html)
#     #     link_list.append(links)
#     #
#     # return link_list


# def vi(link):
#     html = html_obj(link)
#     specifications = for_vi(html)
#     list_photo = vi_photo(html)
#
#     return specifications, list_photo
#     # links_list = search()
#     # specifications = []
#     # quantity_iter = 2
#     # for row in range(2, quantity_row()):
#     #     for links in links_list:
#     #         for link in links:
#     #             if 'vseinstrumenti.ru' in link:
#     #                 html = html_obj(link)
#     #                 export_excel(for_vi(html), 2, quantity_iter)
#     #                 export_excel(vi_photo(html), 3, quantity_iter)
#     #                 quantity_iter += 1
#     #
#     # return specifications


# def main():
#     requests = list_of_requests()
#     for request in requests:
#         first = f'http://xmlproxy.ru/search/xml?{request}user=itproj31%40gmail.com&key=aaaa12bc9d966caf7c4b66fc4fd0ac46'
#         link = search(first, request, count)
#         specifications, list_photo = vi(link)
#         export_excel(specifications, 2, count)
#         export_excel(list_photo, 3, count)
#     # count = 2
#     # requests = list_of_requests()
#     # for request in requests:
#     #     first = 'https://www.google.com/search?q=' if count % 2 == 1 else 'https://yandex.ru/search/?'
#     #     link = search(first, request, count)
#     #     specifications, list_photo = vi(link)
#     #     export_excel(specifications, 2, count)
#     #     export_excel(list_photo, 3, count)
#     #     count += 1
#     #
#     # return f'{count} строк, успешно закружено в таблицу'
path_in_table = 'Стеклорезы.xlsx'


def main(table):
    qwery_list = list_of_requests(import_xl(table))
    link_list = []
    for qwery in qwery_list:
        link_list.append(search_xml(qwery))

    list_html = []
    for link in link_list:
        if link != []:
            html = html_obj(link)
            list_html.append(html)
        else:
            list_html.append(0)

    counter = 2
    for html in list_html:
        if html != 0:
            specifications = for_vi(html)
            export_excel(table, specifications, 2, counter)
            photos = vi_photo(html)
            export_excel(table, photos, 3, counter)
        else:
            export_excel(table, 'Не найдено!', 2, counter)
            export_excel(table, 'Не найдено!', 3, counter)
        counter += 1

    return 'Программа выполнена успешно!'


test = main(path_in_table)
print(test)
