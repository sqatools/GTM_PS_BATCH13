#1.Python oops program to create a class with the constructor.
from ssl import get_protocol_name




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

print("-" * 50)


##############################################
#2.Python oops program to create a class with Instance methods

class user_details:
    def __init__(self, user_name, user_ph_number):
        self.user_name = user_name
        self.user_ph_number = user_ph_number

    def show_user_name(self):
        print("User name :", self.user_name)

    def show_ph_number(self):
        print("User phone number :", self.user_ph_number)


obj = user_details("Rohit Chavan", "9158520006")
obj.show_user_name()
obj.show_ph_number()
'''
User name : Rohit Chavan
User phone number : 9158520006
'''
print("-" * 50)


##############################################################
#3.Python oops program to create a class with an instance variable

class customer():
    def __init__(self):
        self.customer_name = "Rahul"


obj = customer()
print(obj.customer_name)  # Rahul

print("-" * 50)


###############################################################
#4.Python oops program to create a class with class variables.

class Myclass():
    class_var = "Hello Learning Python"


print(Myclass.class_var)  # Hello Learning Python

print("-" * 50)


#########################################################
#5.Python oops program to create a class with a static method.
class Employee():
    @staticmethod
    def show_employee_details():
        print(" Employee is from karad")


obj = Employee()
obj.show_employee_details()  # Employee is from karad

print("-" * 50)


###################################################################
#6.Python class with Single Inheritance.

class Department():
    def __init__(self, d_name, d_ph_number):
        self.department_name = d_name
        self.department_ph_number = d_ph_number

    def show_department_name(self):
        print("Department Name :", self.department_name)

    def show_department_ph_number(self):
        print("Department Phone number is :", self.department_ph_number)

    def Details_of_Department(self):
        self.show_department_name()
        self.show_department_ph_number()


class Employee(Department):
    def __init__(self, e_name, e_email, d_name, d_ph_number):
        super().__init__(d_name, d_ph_number)
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


obj = Employee('Rohit', 'rohit35673@gmail.com', 'CSE', '6546865664')
obj.details()

'''
Department Name : CSE
Department Phone number is : 6546865664
Employee Name : Rohit
Employee Email : rohit35673@gmail.com
'''

print("-" * 50)


##########################################################
#6. Python Class with Multilevel Inheritance

class School:
    def __init__(self, s_name, s_address):
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
    def __init__(self, t_name, t_subject, s_name, s_address):
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
    def __init__(self, st_name, st_class, t_name, t_subject, s_name, s_address):
        super().__init__(t_name, t_subject, s_name, s_address)
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


obj = Student('mahesh', '11th', 'ms.Jadhav Madam', 'Maths', 'Podar School', 'Karad')
obj.details_all()

'''
School name : Podar School
School address : Karad
Teacher Name : ms.Jadhav Madam
Teacher Subject : Maths
Student Name : mahesh
Student Class : 11th

'''
print("-" * 50)


##########################################################
#7.Python oops program to create a class with the class method.

class City():
    clss_var = "Karad"

    @classmethod
    def show_city_name(cls):
        print("City name :", cls.clss_var)


obj = City()
obj.show_city_name()  # City name : Karad

print("-" * 50)


###############################################################
#8.Python Class with Multiple Inheritance

class Father:
    def __init__(self, f_name, f_car, f_phone):
        self.father_name = f_name
        self.father_car = f_car
        self.father_phone = f_phone

    def show_father_details(self):
        print("father name :", self.father_name)
        print("father car :", self.father_car)
        print("father phone number :", self.father_phone)


class Mother():
    def __init__(self, m_name, m_business):
        self.mother_name = m_name
        self.mother_business = m_business

    def show_mother_details(self):
        print("mother Name :", self.mother_name)
        print("mother business :", self.mother_business)

class Son(Father, Mother):
    def __init__(self, s_name, s_business, f_name, f_car, f_phone,m_name,m_business):
        super().__init__(f_name, f_car, f_phone)
        self.Son_name = s_name
        self.Son_business = s_business
        self.mother_name = m_name
        self.mother_business = m_business

    def show_son_details(self):
        print("Son Name :", self.Son_name)
        print("Son Business :", self.Son_business)

    def family_details(self):
        self.show_father_details()
        self.show_mother_details()
        self.show_son_details()


obj = Son('Rohit','IT Engineer','Ramchandra','BMW','74893733884','Rajashri','housewife')
obj.family_details()

'''
father name : Ramchandra
father car : BMW
father phone number : 74893733884
mother Name : Rajashri
mother business : housewife
Son Name : Rohit
Son Business : IT Engineer
'''

print("-"*50)
######################################################
#9.Python Class with Hierarchical Inheritance.

class Animal:
    def __init__(self,A_name):
        self.animal_name = A_name

    def show_animal(self):
        print("Animal Name :", self.animal_name)

class Dog(Animal):
    def __init__(self,d_name,d_dogsbreeds, A_name):
        super().__init__(A_name)
        self.dog_name = d_name
        self.dog_dogsbreeds = d_dogsbreeds


    def show_dogs_details(self):
        print("Dog Name :", self.dog_name)
        print("Don breeds :", self.dog_dogsbreeds)

    def animal_details(self):
        self.show_animal()
        self.show_dogs_details()

class Cat(Animal):
    def __init__(self, c_name, c_breed, A_name):
        super().__init__(A_name)
        self.cat_name = c_name
        self.cat_breed = c_breed

    def show_cats_details(self):
        print("Cat Name :", self.cat_name)
        print("Cat breeds :", self.cat_breed)

    def animal_details(self):
        self.show_animal()
        self.show_cats_details()

obj = Cat('Mani','Asian_cat','Tiger')
obj.animal_details()

print("-"*50)

obj = Dog('Raj','German Shepherd','Tiger')
obj.animal_details()

'''
Animal Name : Tiger
Cat Name : Mani
Cat breeds : Asian_cat
--------------------------------------------------
Animal Name : Tiger
Dog Name : Raj
Don breeds : German Shepherd

'''

print("-"*50)
#########################################################
#10.Python Class with Method Overloading

class Animal():
    def __init__(self,A_name,A_breed):
        self.animal_name = A_name
        self.animal_breed = A_breed

    def show_animal_details(self):
        print("Animal Name :", self.animal_name)
        print("Animal Breed :", self.animal_breed)

    def cat(self,c_name,c_breed):
        print(f"{c_name}{c_breed}")

    def cat(self,c_name):
        print("Cat Name :"f"{c_name}")

class Dog():
    def __init__(self,d_name,d_breeds):
        self.dog_name = d_name
        self.dog_breed = d_breeds

    def dogs_details(self):
        print("Dog Name :", self.dog_name)
        print("Dog Breed :", self.dog_breed)

obj = Animal('Tiger','Bengal')
obj.show_animal_details()
#obj.cat('Mini','American cat')
obj.cat('Mini')
obj = Dog('Raja','German shepherd')
obj.dogs_details()
'''
Animal Name : Tiger
Animal Breed : Bengal
Cat Name :Mini
Dog Name : Raja
Dog Breed : German shepherd

'''
print("-"*50)
#######################################################
#11.Python Class with Method Overriding

class A():
    def __init__(self,a_name,a_city):
        self.a_name = a_name
        self.a_city = a_city

    def show_a_details(self):
        print("A Name is :", self.a_name)
        print("A City is :", self.a_city)

    def substraction(self,n1,n2):
        print("Substraction :", n1-n2)

class B(A):
    def __init__(self, b_name, a_name, a_city):
        super().__init__(a_name, a_city)
        self.b_name = b_name


    def show_b_details(self):
        print("B name is :", self.b_name)

    def substraction(self,x1,x2):
        print("Substraction is :",x1-x2)

obj = B('Mahadev','Jaykumar','City')
obj.substraction(10,5)
obj.show_b_details()
obj.show_a_details()

'''
Substraction is : 5
B name is : Mahadev
A Name is : Jaykumar
A City is : City

'''

print("-"*50)
#############################################################
#12.Write a Python Class Program with an Abstract method

class family():
    def Name(self):
        pass

    def address(self):
        pass

    def phone(self):
        pass

class Chavan(family):
     def show_name(self):
         print("Family Name is: Kulkari")

     def show_address(self):
         print("Family Address is: Pune")

     def show_phone(self):
         print("Phone number is : 6863773736")

     def chavan_family(self):
         self.show_name()
         self.show_address()
         self.show_phone()

class Pawar(family):
     def show_name(self):
         print("Family Name is : Yadhav")

     def show_address(self):
         print("Family address is : Mumbai")

     def show_phone(self):
         print("phone number is : 76376736673")

     def Pawar_family(self):
         self.show_name()
         self.show_address()
         self.show_phone()

obj = Chavan()
obj.chavan_family()

print("-"*20)

obj = Pawar()
obj.Pawar_family()

'''
Family Name is: Kulkari
Family Address is: Pune
Phone number is : 6863773736
--------------------
Family Name is : Yadhav
Family address is : Mumbai
phone number is : 76376736673

'''

print("-"*50)
############################################################
#13. Write a Python Class program to create a class with data hiding

class Student():
    def __init__(self,st_name,st_standard,st_age):
        self.student_name = st_name
        self._student_standard = st_standard
        self.__student_age = st_age

    def show_student_name(self):
        print("Student Name :", self.student_name)

    def _show_student_standard(self):
        print("Student in which standard :", self._student_standard)

    def __show_student_age(self):
        print("Student Age :", self.__student_age)

obj = Student('James','8th','13')
obj.show_student_name()
obj._show_student_standard()
obj._Student__show_student_age()

'''
Student Name : James
Student in which standard : 8th
Student Age : 13
'''

print("-"*50)
#################################################################################
#14.

class myproperty:
    def __init__(self,name):
        self.name = name

@myproperty

def property(self):
    return self.property

obj = myproperty("20 CRS")
print(obj.name) # 20 CRS

