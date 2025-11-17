#1.Python oops program to create a class with the constructor.

class Employee:
    def __init__(self):
        print("Welcome")


    def Show_Employee_name(self):
        print("Rohit Chavan")


obj = Employee()
obj.Show_Employee_name()
'''
Welcome
Rohit Chavan
'''

print("-"*50)
##############################################
#2.Python oops program to create a class with Instance methods

class user_details:
    def __init__(self,user_name,user_ph_number):
        self.user_name = user_name
        self.user_ph_number = user_ph_number

    def show_user_name(self):
        print("User name :",self.user_name)

    def show_ph_number(self):
        print("User phone number :", self.user_ph_number)

obj = user_details("Rohit Chavan","9158520006")
obj.show_user_name()
obj.show_ph_number()
'''
User name : Rohit Chavan
User phone number : 9158520006
'''
print("-"*50)
##############################################################
#3.Python oops program to create a class with an instance variable

class customer():
    def __init__(self):
        self.customer_name = "Rahul"

obj = customer()
print(obj.customer_name) # Rahul

print("-"*50)
###############################################################
#4.Python oops program to create a class with class variables.

class Myclass():
      class_var = "Hello Learning Python"

print(Myclass.class_var)  # Hello Learning Python

print("-"*50)

