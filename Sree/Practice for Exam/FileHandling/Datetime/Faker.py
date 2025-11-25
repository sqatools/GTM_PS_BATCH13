from faker import Faker
import openpyxl

def create_user_details_in_excel(file_path):
    fk = Faker()
    cell_no = 1
    wb = openpyxl.load_workbook(file_path)
    sheet = wb['Sheet1']
    for i in range(1,50):
        print("Count :",i)

        first_name = fk.first_name()
        last_name = fk.last_name()
        email = fk.email()
        phone = fk.phone_number()

        print("first_name :", first_name)
        print("last_name :", last_name)
        print("email :", email)
        print("phone number :", phone)


        sheet[f"A{cell_no}"] = first_name
        sheet[f"B{cell_no}"] = last_name
        sheet[f"C{cell_no}"] = email
        sheet[f"D{cell_no}"] = phone

        cell_no +=1
    wb.save(file_path)
    print("Data successfully inserted :",file_path)

create_user_details_in_excel("user_details_1.xlsx")