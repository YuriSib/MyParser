import openpyxl


def export_excel(values_list, row):
    workbook = openpyxl.load_workbook('Шаблон для парсера(Биты, адаптеры, торцевые головки).xlsx')
    sheet = workbook.active
    combined_values = ', '.join(values_list)
    sheet[row][2].value = combined_values   #sheet[строка][колонка].value
    workbook.save('Шаблон для парсера(Биты, адаптеры, торцевые головки).xlsx')


def quantity_row():
    workbook = openpyxl.open("Шаблон для парсера(Биты, адаптеры, торцевые головки).xlsx", read_only=True)
    sheet = workbook.active

    return sheet.max_row + 1
