import xlrd
file_name = "/Users/thisdjango/Desktop/Учеба/Python/ИИТ_2к_20-21_осень_6_уч.н..xlsx"
book = xlrd.open_workbook(file_name)

sheet = book.sheet_by_index(0)
groups = {}
shedule = {}
index = 0
for cell in sheet.row(1):
    if str(cell.value).count('-') == 2:
        groups[index] = cell.value
    index += 1
print(groups)
for key, value in groups.items():
    shedule[value] = []
    for cell in sheet.col(key):
        if cell.value != "":
            shedule[value].append(cell.value)
print(shedule[groups[5]])
