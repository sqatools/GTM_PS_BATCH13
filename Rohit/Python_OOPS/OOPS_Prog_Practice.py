#1.Python oops program to create a class with the constructor.
from ssl import get_protocol_name

from Preeti.Py_Program.Python_Variable.py_variable import sur_name


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
#########################################################
#5.Python oops program to create a class with a static method.
class Employee():
    @staticmethod
    def show_employee_details():
        print(" Employee is from karad")

obj = Employee()
obj.show_employee_details() # Employee is from karad

print("-"*50)
###################################################################
#6.Python class with Single Inheritance.

class Department():
    def __init__(self,d_name, d_ph_number):
        self.department_name = d_name
        self.department_ph_number = d_ph_number

    def show_department_name(self):
        print("Department Name :",self.department_name)

    def show_department_ph_number(self):
        print("Department Phone number is :", self.department_ph_number)

    def Details_of_Department(self):
        self.show_department_name()
        self.show_department_ph_number()

class Employee(Department):
    def __init__(self, e_name, e_email,d_name, d_ph_number):
        super().__init__(d_name,d_ph_number)
        self.employee_name = e_name
        self.employee_email = e_email

    def show_employee_name(self):
        print("Employee Name :", self.employee_name)

    def show_employee_email(self):
        print("Employee Email :", self.employee_email)

    def employee_details(self):
        self.show_employee_name()
        self.show_employee_email()


    def details(self):
        self.Details_of_Department()
        self.employee_details()

obj = Employee('Rohit','rohit35673@gmail.com','CSE','6546865664')
obj.details()

'''
Department Name : CSE
Department Phone number is : 6546865664
Employee Name : Rohit
Employee Email : rohit35673@gmail.com
'''

print("-"*50)
##########################################################
#6. Python Class with Multilevel Inheritance

class School:
    def __init__(self,s_name,s_address):
        self.school_name = s_name
        self.school_address = s_address

    def show_School_name(self):
        print("School name :", self.school_name)

    def show_school_address(self):
        print("School address :", self.school_address)

    def school_details(self):
        self.show_School_name()
        self.show_school_address()

class Teacher(School):
    def __init__(self,t_name,t_subject,s_name,s_address):
        super().__init__(s_name, s_address)
        self.teacher_name = t_name
        self.teacher_subject = t_subject

    def show_teacher_name(self):
        print("Teacher Name :", self.teacher_name)

    def show_teacher_subject(self):
        print("Teacher Subject :", self.teacher_subject)

    def teacher_details(self):
        self.show_teacher_name()
        self.show_teacher_subject()

class Student(Teacher):
    def __init__(self,st_name,st_class,t_name,t_subject,s_name,s_address):
        super().__init__(t_name,t_subject,s_name,s_address)
        self.student_name = st_name
        self.student_class = st_class

    def show_student_name(self):
        print("Student Name :", self.student_name)

    def show_student_class(self):
        print("Student Class :", self.student_class)


    def student_details(self):
        self.show_student_name()
        self.show_student_class()

    def details_all(self):
        self.school_details()
        self.teacher_details()
        self.student_details()

obj = Student('mahesh','11th','ms.Jadhav Madam','Maths','Podar School','Karad')
obj.details_all()

'''
School name : Podar School
School address : Karad
Teacher Name : ms.Jadhav Madam
Teacher Subject : Maths
Student Name : mahesh
Student Class : 11th

'''
print("-"*50)
##########################################################
#7.Python oops program to create a class with the class method.

class City():
    clss_var= "Karad"

    @classmethod
    def show_city_name(cls):
        print("City name :",cls.clss_var)

obj = City()
obj.show_city_name()   # City name : Karad



