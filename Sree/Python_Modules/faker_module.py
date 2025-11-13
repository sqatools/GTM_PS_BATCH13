# pip install faker
from faker import Faker
import openpyxl

fk=Faker()    # need to get Faker Object

print("First name:",fk.first_name()) # Have to give only small letter of first,last,email,phone
print("Last name:",fk.last_name())  # all these r methods - should be in parentheses
print("Email id:",fk.email())
print("Phone number:",fk.phone_number())

def createuserdataintext():
    for i in range(1,20):
        print("count:",i)
        print("First name:", fk.first_name())
        print("Last name:", fk.last_name())
        print("Email id:", fk.email())
        print("Phone number:", fk.phone_number())
        Userdata=f"{fk.first_name()},{fk.last_name()},{fk.email()},{fk.phone_number()}\n"
        with open("Usersdetail.txt","a") as file:   ##f-string allows you to insert variables directly inside a string using { }
            file.write(Userdata)
createuserdataintext()
