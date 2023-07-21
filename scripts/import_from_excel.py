import openpyxl


def import_xl():
    catalog = openpyxl.open("Стеклорезы.xlsx", read_only=True)
    sheet = catalog.active
    list_category = []

    #sheet.max_row + 1 в range - для вывода всего ряда
    for row in range(2, sheet.max_row + 1):
        name = sheet[row][0].value
        article = sheet[row][1].value if sheet[row][1].value is not None else None
        if article is None:
            search_query = name
        else:
            search_query = name + ' ' + article
        list_category.append(search_query)

    return list_category


# test = import_xl()
# print(test)