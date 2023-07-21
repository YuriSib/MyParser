import openpyxl


def export_excel(values_list, column, row):
    workbook = openpyxl.load_workbook('Стеклорезы.xlsx')
    sheet = workbook.active
    combined_values = ', '.join(values_list)
    sheet[row][column].value = combined_values   #sheet[строка][колонка].value
    workbook.save('Стеклорезы.xlsx')


def quantity_row():
    workbook = openpyxl.open('Стеклорезы.xlsx', read_only=True)
    sheet = workbook.active

    return sheet.max_row + 1
