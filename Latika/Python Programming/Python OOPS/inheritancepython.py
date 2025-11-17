"""
Inheritance : When one class accuire the property of another class, then it is called inheritance.

Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Hierarchical Inheritance
"""

# Single Inheritance
# Super Class
# Multilevel Inheritance

class Grandfather():
        def __init__(self,gf_name,gf_property):
            self.grandfather_name=gf_name
            self.grandfather_property=gf_property
        def show_grandfather_details(self):
            print("Grandfather name is:",self.grandfather_name)
            print("Grandfather property is:", self.grandfather_property)


class Father(Grandfather):

        def __init__(self,gf_name,gf_property,f_name,f_business,f_car):
            super().__init__(gf_name,gf_property)

            self.father_name=f_name
            self.father_business=f_business
            self.father_car=f_car

        def show_father_name(self):
            print("Father name is:",self.father_name)

        def show_father_business(self):
            print("Father business is:",self.father_business)

        def show_father_car(self):
            print("Father Car name is:",self.father_car)

        def show_all_details_of_father(self):
            self.show_father_name()
            self.show_father_business()
            self.show_father_car()

# Child/Base Class
class Son(Father):

        def __init__(self,gf_name,gf_property, s_name, f_name, f_business, f_car):

            super().__init__(gf_name,gf_property,f_name,f_business,f_car)
            self.son_name=s_name

        def show_son_name(self):
            print("Son name is:",self.son_name)

        def family_Details(self):
            print("\n -- Family Details --")
            self.show_grandfather_details()
            self.show_all_details_of_father()
            self.show_son_name()

sonobj=Son("Mr. Vithal", "Farm Land", "Manav. Patil", "Mr.Patil", "Electronics Engg", "Audi")
sonobj.family_Details()