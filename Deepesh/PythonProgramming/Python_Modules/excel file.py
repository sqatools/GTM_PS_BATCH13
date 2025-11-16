from faker import Faker
import openpyxl
import os
def create_user_data_in_excel(file_path):
    fk = Faker()
    cell_no = 1
    for i in range(1,50):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb["Sheet"]
        cell1 = sheet[f"A{cell_no}"]
        cell2 = sheet[f"B{cell_no}"]
        cell3 = sheet[f"C{cell_no}"]
        cell4 = sheet[f"D{cell_no}"]
        cell1.value = fk.first_name()
        cell2.value = fk.last_name()
        cell3.value = fk.email()
        cell4.value = fk.phone_number()
        wb.save(file_path)
        cell_no += 1

create_user_data_in_excel("users_details1.xlsx")
