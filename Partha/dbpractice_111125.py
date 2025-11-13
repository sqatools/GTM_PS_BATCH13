from faker import Faker
import openpyxl

fk = Faker()

print("first name :", fk.first_name())
print("last name :", fk.last_name())
print("email :", fk.email())
print("phone :", fk.phone_number())
print("DOB:", fk.date_of_birth())

def create_user_data_in_text():
    for i in range(1, 50):
        print("count :", i)
        print("first name :", fk.first_name())
        print("last name :", fk.last_name())
        print("email :", fk.email())
        print("phone :", fk.phone_number())
        print("DOB :", fk.date_of_birth())
        print("_"*50)
        users_data = f"{fk.first_name()}, {fk.last_name()}, {fk.email()}, {fk.phone_number()}, {fk.date_of_birth()}\n"
        with open("users_details.txt", "a") as file:
            file.write(users_data)

create_user_data_in_text()

def create_users_data_in_excel(file_path):
    cell_no = 1
    for i in range(1, 50):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb["Sheet"]
        cell1 = sheet[f"A{cell_no}"]
        cell2 = sheet[f"B{cell_no}"]
        cell3 = sheet[f"C{cell_no}"]
        cell4 = sheet[f"D{cell_no}"]
        cell5 = sheet[f"E{cell_no}"]
        cell1.value = fk.first_name()
        cell2.value = fk.last_name()
        cell3.value = fk.email()
        cell4.value = fk.phone_number()
        cell5.value = fk.date_of_birth()
        wb.save(file_path)
        cell_no += 1

create_users_data_in_excel("users_details.xlsx")

print(dir(fk))

##connection = create_database_connect()
##create_table_query = """create table student(name char[10], email char [10], phone int)"""
##create_table(con=connection, query=create_table_query)
