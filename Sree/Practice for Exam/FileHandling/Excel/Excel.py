import openpyxl

def write_excel_file(file_path, sheet_name, cell_name, cell_value):
    wb = openpyxl.load_workbook(file_path)
    # get specific sheet
    sheet = wb[sheet_name]
    # get specific cell
    cell = sheet[cell_name]
    # add new value to the cell
    cell.value = cell_value
    ## save the excel file
    wb.save(file_path)


write_excel_file(r"C:\Sree\FileHandling\Read()method\\Excel.xlsx", "Sheet1", "B1", "2025")