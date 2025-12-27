"""
Inheritance: when one class aquire the property of another class, then it is called inheritance.
1.  single inheritance :  class A(Father) ->  class B(son)
2.  multilevel inheritance :  class A(Grand Father) ->  class B(Father) -> Class C (son)
3.  multiple inheritance : class A(Father class) -> class B (Son),  class C (Mother) -> class B(Son)
                           class A (Father), class C (Mother)  -> B (son)(A, C)

4.  Hierarchical inheritance : class A (Father) -> class B (Son1), class A(Father) -> class C (Son2)
"""

# multilevel inheritance
class GrandFather():
    def __init__(self, GF_name, GF_property):
        self.grand_father_name = GF_name
        self.grand_father_property = GF_property

    def show_grand_father_name(self):
        print("Grand Father name :", self.grand_father_name)

    def show_grand_father_property(self):
        print("Grand Father property :", self.grand_father_property)

    def Grand_Father_details(self):
        self.show_grand_father_name()
        self.show_grand_father_property()

# parent/super class
class Father(GrandFather):
    def __init__(self, f_name, f_business, f_Car, GF_name, GF_property):
        super().__init__(GF_name, GF_property)
        self.father_name = f_name
        self.father_business = f_business
        self.father_Car = f_Car

    def show_father_name(self):
        print("Father name :", self.father_name)

    def show_father_business(self):
        print("Father Business :", self.father_business)

    def show_father_car(self):
        print("father car :", self.father_Car)

    def father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

# child/base class
class son(Father):
    """
       When we set inheritance between 2 classes, then parent class constructor has to initialiaze in child class constructor
       with the help of super keyword.

       """
    def __init__(self,s_name,f_name,f_business,f_Car,GF_name,GF_property):
        super().__init__(f_name,f_business,f_Car,GF_name,GF_property)
        self.son_name = s_name

    def show_son_name(self):
        print("Son name :", self.son_name)

    def all_family_Details(self):
        self.Grand_Father_details()
        self.father_details()
        self.show_son_name()

obj = son('Rohit','Ramchandra','Medical Store','BMW','Haribhau','10 Acrs')
obj.all_family_Details()

'''
Grand Father name : Haribhau
Grand Father property : 10 Acrs
Father name : Ramchandra
Father Business : Medical Store
father car : BMW
Son name : Rohit
'''

