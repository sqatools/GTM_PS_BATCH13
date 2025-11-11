"""
command to install the openpyxl module
-> pip install openpyxl
"""

import openpyxl

def read_excel_file(filepath,sheet_name,cell_name):
    wb = openpyxl.load_workbook(filepath)
    # get specific sheet
    sheet = wb[sheet_name]
    # get specific cell
    cell = sheet[cell_name]
    # get cell value
    print(cell.value)

#read_excel_file("user_data.xlsx","Sheet1","A2") # Rohit
#read_excel_file("user_data.xlsx","Sheet1","E4") # 3000
#read_excel_file("user_data.xlsx","Batch13","A4") #Apple
 # With For loop
for i in range(1,6):
    read_excel_file("user_data.xlsx","Batch13",f"A{i}")

'''
Food Name
Banana
Potato
Apple
Mango
'''
print("-"*50)
######################################################################################
def write_excel_file(filepath,sheet_name,cell_name,cell_value):
    wb = openpyxl.load_workbook(filepath)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    cell.value = cell_value
    wb.save(filepath)

write_excel_file("user_data.xlsx","Batch13","B1","Pune")