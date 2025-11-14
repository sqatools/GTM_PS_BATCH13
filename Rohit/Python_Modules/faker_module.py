# pip install faker
from faker import Faker
import openpyxl

fk = Faker()

print("First_name :", fk.first_name())
print("Last_name :", fk.last_name())
print("Email address :", fk.email())
print("phone_number :", fk.phone_number())

print("-"*50)

# create data for 50
def create_user_details_in_text():
    for i in range(1,50):
        print("count :",i)
        print("first_name :", fk.first_name())
        print("last_name :", fk.last_name())
        print("email :", fk.email())
        print("phone_number :", fk.phone_number())
        users_data = f"{fk.first_name()},{fk.last_name()},{fk.email()},{fk.phone_number()}\n"
        with open("user_details.txt",'a') as file:
            file.write(users_data)

#create_user_details_in_text()

#create_user_data_in_excel()
def create_user_data_in_excel(filepath):
    cell_no = 1
    for i in range(1,50):
        wb = openpyxl.load_workbook(filepath)
        sheet = wb["Sheet"]
        cell1 = sheet[f"A{cell_no}"]
        cell2 = sheet[f"B{cell_no}"]
        cell3 = sheet[f"C{cell_no}"]
        cell4 = sheet[f"D{cell_no}"]
        cell1.value = fk.first_name()
        cell2.value = fk.last_name()
        cell3.value = fk.email()
        cell4.value = fk.phone_number()
        wb.save(filepath)
        cell_no +=1

create_user_data_in_excel("users_details.xlsx")

