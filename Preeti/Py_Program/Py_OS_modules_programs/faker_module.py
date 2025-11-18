#pip install faker
from faker import Faker
import openpyxl
fk=Faker()

print("first name:", fk.first_name)
print("last name:", fk.last_name())
print("email:", fk.email())
print("phone:",fk.phone_number())

def create_user_data_in_text():
    for i in range(1,50):
        print("count:",i)
        print("first name:", fk.first_name)
        print("last name:", fk.last_name())
        print("email:", fk.email())
        print("phone:", fk.phone_number())
        user_data=f"{fk.first_name()},{fk.last_name()},{fk.email()},{fk.phone_number()}"
        with open("users_details.txt","a") as file:
            file.write(user_data)
            file.write("\n")







