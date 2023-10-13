import openpyxl


def export_excel(table, value, column, row):
    workbook = openpyxl.load_workbook(table)
    sheet = workbook.active
    if type(value) == list:
        value = ', '.join(value)
    sheet[row][column].value = value
    workbook.save(table)


def quantity_row(table):
    workbook = openpyxl.open(table, read_only=True)
    sheet = workbook.active

    return sheet.max_row + 1
