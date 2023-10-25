from import_from_excel import import_xl, import_xl_test
from search import search_xml
from export_in_excel import export_excel, quantity_row


def main(table, start):
    qwery = import_xl_test(table, start)

    try:
        image, property_ = search_xml(qwery)
        export_excel(table, property_, 2, start)
        export_excel(table, image, 3, start)
    except TypeError:
        image, property_ = 0, 0


path_in_table = 'Канцтовары.xlsx'

# for i in (166, 167, 168, 169, 173, 174, 176, 178, 180):
#     try:
#         main(path_in_table, i)
#     except Exception as E:
#
#         print(f'Неизвестная ошибка {E}!')
#     print(i)

start_ = 1
for i in range(4000):
    try:
        main(path_in_table, start_)
    except Exception as E:
        print(f'Неизвестная ошибка {E}!')
    print(start_)
    start_ += 1
