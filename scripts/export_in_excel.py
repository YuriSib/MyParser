import openpyxl


def export_excel(table, values_list, column, row):
    workbook = openpyxl.load_workbook(table)
    sheet = workbook.active
    combined_values = ', '.join(values_list)
    sheet[row][column].value = combined_values
    workbook.save(table)


def quantity_row(table):
    workbook = openpyxl.open(table, read_only=True)
    sheet = workbook.active

    return sheet.max_row + 1
