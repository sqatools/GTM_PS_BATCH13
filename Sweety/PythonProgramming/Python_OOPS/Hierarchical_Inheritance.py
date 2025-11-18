"""
Inheritance: when one class aquire the property of another class, then it is called inheritance.
1.  single inheritance :  class A(Father) ->  class B(son)
2.  multilevel inheritance :  class A(Grand Father) ->  class B(Father) -> Class C (son)
3.  multiple inheritance : class A(Father class) -> class B (Son),  class C (Mother) -> class B(Son)
                           class A (Father), class C (Mother)  -> B (son)(A, C)

4.  Hierarchical inheritance : class A (Father) -> class B (Son1), class A(Father) -> class C (Son2)
"""
# Hierarchical inheritance
# parent/super class

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
        print("Father Car: ", self.father_car)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

# child/sub class 1
class Son1(Father):
    def __init__(self, s_name, f_name, f_business, f_car):
        super().__init__(f_name, f_business, f_car)
        self.son_name = s_name

    def show_son1_details(self):
        print("Son1 Name: ", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son1_details()

# child/sub class 2
class Son2(Father):
    def __init__(self, s_name, s_job, f_name, f_business, f_car):
        super().__init__(f_name, f_business, f_car)
        self.son_name = s_name
        self.son_job = s_job

    def show_son2_details(self):
        print("Son2 Name: ", self.son_name)
        print("Son 2 Job: ", self.son_job)

    def show_family_details(self):
        self.show_father_details()
        self.show_son2_details()

obj1 = Son1('Rahul', 'Mr Mohan', 'Construction', 'Audi Q3')
obj1.show_family_details()

obj2 = Son2('Mohit', "Software Engineer", 'Mr Mohan', 'Construction', 'Audi Q3')
obj2.show_family_details()



