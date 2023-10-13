import openpyxl


def import_xl(table, start=None, finish=None):
    catalog = openpyxl.open(table, read_only=True)
    sheet = catalog.active
    list_category = []

    #sheet.max_row + 1 в range - для вывода всего ряда (start, finish) - для диапазона
    for row in range(1, sheet.max_row + 1):
        search_query = ''
        name = sheet[row][0].value
        if name is None:
            break
        article = sheet[row][1].value
        if article is None:
            search_query = name
        else:
            try:
                search_query = name + ' ' + article
            except TypeError:
                search_query = ''
        list_category.append(search_query)

    return list_category


def import_xl_test(table, row):
    catalog = openpyxl.open(table, read_only=True)
    sheet = catalog.active

    name = sheet[row][0].value
    if name is None:
        name = 0
    article = sheet[row][1].value
    if article is None:
        search_query = name
    else:
        try:
            search_query = name + ' ' + article
        except TypeError:
            search_query = ''

    return search_query
