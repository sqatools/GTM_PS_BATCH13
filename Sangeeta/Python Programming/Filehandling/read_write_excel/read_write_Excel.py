import openpyxl

def read_write(filepath, sheet_name, cell_name):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb(sheet_name)
    cell = sheet(cell_name)
    print(cell.value)

read_write("C:\Users\salia\Downloads\read_write_excel.xlsx", "sheet1", "A2")

for i in range (1,6):
    read_write("C:\Users\salia\Downloads\read_write_excel.xlsx", "sheet1", f"A{i}")