"""
command to install the openpyxl module
-> pip install openpyxl
"""
import openpyxl

def read_excel_file(file_path, sheet_name, cell_name):
    wb = openpyxl.load_workbook(file_path)
    # get specific sheet
    sheet = wb[sheet_name]
    # get specific cell
    cell = sheet[cell_name]
    # get cell value
    print(cell.value)


read_excel_file("user_data.xlsx", "Sheet1", "A1") # Pune
#read_excel_file("user_data.xlsx", "Sheet1", "E1") # India

#read_excel_file("userdata.xlsx", "Batch13", f"A1") # Rose

for i in range(1, 6):
    read_excel_file(r"user_data.xlsx", "Sheet1", f"A{i}")


def write_excel_file(file_path, sheet_name, cell_name, cell_value):
    wb = openpyxl.load_workbook(file_path)
    # get specific sheet
    sheet = wb[sheet_name]
    # get specific cell
    cell = sheet[cell_name]
    # add new value to the cell
    cell.value = cell_value
    # save the excel file
    wb.save(file_path)


write_excel_file("user_data.xlsx", "Sheet1", "B1", "2025")
