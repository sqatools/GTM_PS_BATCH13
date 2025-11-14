import openpyxl
from faker import Faker

fk = Faker()
print("First Name :", fk.first_name())
print("Last Name :", fk.last_name())
print("Email :", fk.email())
print("Phone Number :", fk.phone_number())

# print in bulk

for i in range(1, 51):
    print("Count:", i)
    print("First Name :", fk.first_name())
    print("Last Name :", fk.last_name())
    print("Email :", fk.email())
    print("Phone Number :", fk.phone_number())

# import random data in txt file

users_data = f"{fk.first_name()}, {fk.last_name()}, {fk.email()}, {fk.phone_number()} \n"

with open("users_details.txt", "a") as file:
    file.write(users_data)

# import in excel

#def create_users_data(filename):
    cell_no=1

    for i in range(1 , 50):
        wb = openpyxl.load_workbook("users_data.xlsx")
        sheet = wb["Sheet1"]
        cell1 = sheet[f"A{cell_no}"]
        cell2 = sheet[f"B{cell_no}"]
        cell3 = sheet[f"C{cell_no}"]
        cell4 = sheet[f"D{cell_no}"]

        cell1.value=fk.first_name()
        cell2.value=fk.last_name()
        cell3.value=fk.email()
        cell4.value=fk.phone_number()

        cell_no+=1
        wb.save("users_data.xlsx")
#create_users_data("user_data.xlsx")







