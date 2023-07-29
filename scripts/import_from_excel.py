import openpyxl


def import_xl(table, start, finish):
    catalog = openpyxl.open(table, read_only=True)
    sheet = catalog.active
    list_category = []

    #sheet.max_row + 1 в range - для вывода всего ряд
    for row in range(start, finish):
        search_query = ''
        name = sheet[row][0].value
        article = sheet[row][1].value
        if article is None:
            search_query = name
        else:
            search_query = name + ' ' + article

        list_category.append(search_query)

    return list_category
