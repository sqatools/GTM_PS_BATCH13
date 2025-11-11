#to work on excel - we need to import - openpyxl library
"""
command to install the openpyxl module
-> pip install openpyxl
pip is package manager in python - which helps us to install the openpyxl package
->open terminal and type - pip install openpyxl
"""
#cannot create excel in pycharm,
#excel file considered as a workbook

import openpyxl
def read_excel_file(file_path, sheet_name, cell_name):
    wb = openpyxl.load_workbook(file_path)
    # get specific sheet
    sheet = wb[sheet_name]
    # get specific cell
    cell = sheet[cell_name]
    # get cell value
    print(cell.value)


read_excel_file("users_data.xlsx", "Sheet1", "A1") # Chennai
#specify the cell value
read_excel_file("users_data.xlsx", "Sheet1", "E1") # India

#now want data from differnt sheet
read_excel_file("users_data.xlsx", "Batch13", f"A1") # Rose

#now want to read all the values in sheet1 under A column
for i in range(1,6):
    read_excel_file("users_data.xlsx", "Sheet1",f"A{i}" )

"""
Chennai
pune
hydreabad
bangalore
delhi
"""
#################################################################################################

#write data to the file, here extra paramter is cell_value
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


write_excel_file("users_data.xlsx", "Sheet1", "B1", "2025")