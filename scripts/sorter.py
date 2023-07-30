from openpyxl import load_workbook, Workbook

workbook = load_workbook('test.xlsx')
sheet = workbook.active

list_types = []
for column_cells in sheet.iter_rows(min_col=1, min_row=2, values_only=True):
    list_types.append(column_cells)


sorted_list = sorted(list_types, key=lambda x: x[2])
print(sorted_list)

sorted_workbook = Workbook()
sheet_ = sorted_workbook.active

headers = ['Товар', 'Описание', 'Тип']
sheet_.append(headers)

for row in sorted_list:
    sheet.append(row)

workbook.save('test2.xlsx')









