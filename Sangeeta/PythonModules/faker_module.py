from faker import Faker
import openpyxl

fk = Faker()

print("first name :", fk.first_name())
print("last name :", fk.last_name())
print("email :", fk.email())
print("phone # :", fk.phone_number())
print("Address :", fk.address())

def create_fake_data_in_text(filepath):
    for i in range(1, 20):
        print("count :", i)
        print("first name :", fk.first_name())
        print("last name :", fk.last_name())
        print("email :", fk.email())
        print("phone # :", fk.phone_number())
        print("Address :", fk.address())
        fake_data = f"{fk.first_name()},{fk.last_name()}, {fk.phone_number()}, {fk.email()}, {fk.address()}\n"
        with open(filepath, "a") as file:
            file.write(fake_data)

create_fake_data_in_text("fake_data.txt")

def create_fake_Data_in_excel(filepath):
    cell_no = 1
    for i in range(50):
        wb = openpyxl.load_workbook(filepath)
        sheet = wb["Sheet1"]
        cell1 = sheet[f"A{cell_no}"]
        cell2 = sheet[f"B{cell_no}"]
        cell3 = sheet[f"C{cell_no}"]
        cell4 = sheet[f"D{cell_no}"]
        cell5 = sheet[f"E{cell_no}"]
        cell1.value = fk.first_name()
        cell2.value = fk.last_name()
        cell3.value = fk.email()
        cell4.value = fk.address()
        cell5.value = fk.phone_number()
        wb.save(filepath)
        cell_no += 1

#create_fake_Data_in_excel(r"C:\Users\salia\OneDrive\Desktop\SangsPythonfiles\fake_data.xlsx")



