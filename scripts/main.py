from import_from_excel import import_xl, import_xl_test
from ya_search import list_of_requests
from search import search_xml
from html_master import sima_master
from export_in_excel import export_excel, quantity_row


def main(table, start):
    qwery = list_of_requests(import_xl_test(table, start))

    sima_link = search_xml(qwery)

    if sima_link:
        property_, image_list = sima_master(sima_link[0])
        export_excel(table, [property_], 2, start)
        export_excel(table, image_list, 3, start)
    # elif ozon_link:
    #     property_, image_list = ozon_master(ozon_link[0])
    #     export_excel(table, [property_], 2, start)
    #     export_excel(table, image_list, 3, start)


path_in_table = 'Ластики, резинки стиральные.xlsx'

start_ = 1
for i in range(50):
    try:
        main(path_in_table, start_)
    except Exception:
        print(f'Неизвестная ошибка!')
    print(start_)
    start_ += 1

