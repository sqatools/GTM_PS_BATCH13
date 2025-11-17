"""
Inheritance :
When one class iaquire the proporty of another calss

"""

#Single inheritacne
class father:
    def __init__(self, f_name,f_business,f_car):
        self.f_name = f_name
        self.f_business = f_business
        self.f_car = f_car
    def show_f_name(self):
        print("FAthername:",self.f_name)
    def show_f_business(self):
        print("Father business:",self.f_business)
    def show_f_car(self):
        print("Father car:",self.f_car)
    def show_all_details_of_father(self):
        self.show_f_name()
        self.show_f_business()
        self.show_f_car()
#Child class

class Son(father):
    """
    When we setup inheritance bet 2 lcasses then parnet
    class constructor has to intilaize in child class constrcutor
    """
    def __init__(self, s_name,f_name,f_business,f_car):
        super().__init__(f_name,f_business,f_car)
        self.son_name = s_name
    def show_son_name(self):
        print("Son name:",self.son_name)
    def family_details(self):
        self.show_all_details_of_father()
        self.show_son_name()

obj = Son('Arun'," Aman",f_business="Builder",f_car="Honda")
obj.family_details()

    