import openpyxl


def import_xl():
    catalog = openpyxl.open("Шаблон для парсера(Биты, адаптеры, торцевые головки).xlsx", read_only=True)
    sheet = catalog.active
    list_category = []

    #sheet.max_row + 1 в range - для выводода всего ряда
    for row in range(5, 10):
        name = sheet[row][0].value
        article = sheet[row][1].value if sheet[row][1].value is not None else ' '
        search_query = name + ' ' + article if article not in name else name
        list_category.append(search_query)

    return list_category

