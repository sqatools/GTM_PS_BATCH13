"""
Inheritance: when one class aquire the property of another class, then it is called inheritance.
1.  single inheritance :  class A(Father) ->  class B(son)
2.  multilevel inheritance :  class A(Grand Father) ->  class B(Father) -> Class C (son)
3.  multiple inheritance : class A(Father class) -> class B (Son),  class C (Mother) -> class B(Son)
                           class A (Father), class C (Mother)  -> B (son)(A, C)

4.  Hierarchical inheritance : class A (Father) -> class B (Son1), class A(Father) -> class C (Son2)
"""

# single inheritance
# parent/super class

class father:
    def __init__(self,f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_father_name(self):
        print("Father Name :", self.father_name)

    def show_father_business(self):
        print("Father Business :", self.father_business)

    def show_father_car(self):
        print("Father Car :", self.father_car)

    def show_all_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

# child/base class
class Son(father):
    """
       When we set inheritance between 2 classes, then parent class constructor has to initialiaze in child class constructor
       with the help of super keyword.

       """
    def __init__(self,s_name,f_name, f_business, f_car):
        super().__init__(f_name, f_business, f_car)
        self.son_name = s_name

    def show_Son_name(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.show_all_father_details()
        self.show_Son_name()

obj = Son('Rohit','Mr.Ramchandra','Medical Store','Swift Dzire')
obj.family_details()

'''
Father Name : Mr.Ramchandra
Father Business : Medical Store
Father Car : Swift Dzire
Son Name : Rohit
'''


