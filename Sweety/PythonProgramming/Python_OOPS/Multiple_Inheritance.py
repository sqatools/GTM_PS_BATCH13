"""
Inheritance: when one class aquire the property of another class, then it is called inheritance.
1.  single inheritance :  class A(Father) ->  class B(son)
2.  multilevel inheritance :  class A(Grand Father) ->  class B(Father) -> Class C (son)
3.  multiple inheritance : class A(Father class) -> class B (Son),  class C (Mother) -> class B(Son)
                           class A (Father), class C (Mother)  -> B (son)(A, C)

4.  Hierarchical inheritance : class A (Father) -> class B (Son1), class A(Father) -> class C (Son2)
"""
# Multiple inheritance
# parent/super class

# parent/super class 1
class Father:
    def __init__(self, f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_father_name(self):
        print("Father Name: ", self.father_name)

    def show_father_business(self):
        print("Father Business: ", self.father_business)

    def show_father_car(self):
        print("Father Car", self.father_car)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

# parent/super class 2
class Mother:

    def __init__(self, m_name, m_business, m_car):
        self.mother_name = m_name
        self.mother_business = m_business
        self.mother_car = m_car

    def show_mother_name(self):
        print("Mother Name:", self.mother_name)

    def show_mother_business(self):
        print("Mother Business: ", self.mother_business)

    def show_mother_car(self):
        print("Mother Car: ", self.mother_car)

    def show_mother_details(self):
        self.show_mother_name()
        self.show_mother_business()
        self.show_mother_car()

# child/base class
#MRO (Method Resolution order) :
class Son(Father, Mother):
    """
       When we set inheritance between 2 classes, then parent class constructor has to initialiaze in child class constructor
       with the help of super keyword.

       MRO (Method Resolution order) :  in multiple inheritance the order of class name will decide which constructor will get
       priority.

       """
    def __init__(self, s_name, f_name, f_business, f_car, m_name, m_business, m_car):
        super().__init__(f_name, f_business, f_car)
        self.mother_name = m_name
        self.mother_business = m_business
        self.mother_car = m_car
        self.son_name = s_name

    def show_son_name(self):
        print("Son Name", self.son_name)

    def family_details(self):
        self.show_father_details()
        self.show_mother_details()
        self.show_son_name()

obj = Son('Rahul', 'Mr Mohan', 'Construction', 'Audi Q3', 'Mrs Swati', 'Fashion', 'Mercedes')
obj.family_details()








