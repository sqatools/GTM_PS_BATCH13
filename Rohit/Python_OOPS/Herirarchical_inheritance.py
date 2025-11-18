class Father():
    def __init__(self,f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def father_details(self):
        print("Father Name :", self.father_name)
        print("Father Business :", self.father_business)
        print("Father Car :", self.father_car)

class Son1(Father):
    def __init__(self, s1_name, s1_school, s1_bike, f_name, f_business, f_car):
        super().__init__(f_name, f_business, f_car)
        self.son1_name= s1_name
        self.son1_school = s1_school
        self.son1_bike = s1_bike

    def Son1_details(self):
        print("Son1 Name :", self.son1_name)
        print("Son1 School :", self.son1_school)
        print("Son1 Bike :", self.son1_bike)

    def family_details(self):
        self.father_details()
        self.Son1_details()



class Son2(Father):
    def __init__(self, s2_name, s2_school, s2_bike, f_name, f_business, f_car):
        super().__init__(f_name, f_business, f_car)
        self.son2_name = s2_name
        self.son2_school = s2_school
        self.son2_bike = s2_bike

    def Son2_details(self):
        print("Son2 Name :", self.son2_name)
        print("Son2 School :", self.son2_school)
        print("Son2 Bike :", self.son2_bike)

    def family_details(self):
        self.father_details()
        self.Son2_details()

obj = Son2('Rohit','AITRC','Scooty','Ramchandra','Medical Store','BMW')
obj.family_details()

print("-"*50)

obj= Son1('Rahul','YC College','Hero Honda','Ramchandra','Medical Store','BMW')
obj.family_details()

'''
Father Name : Ramchandra
Father Business : Medical Store
Father Car : BMW
Son2 Name : Rohit
Son2 School : AITRC
Son2 Bike : Scooty
--------------------------------------------------
Father Name : Ramchandra
Father Business : Medical Store
Father Car : BMW
Son1 Name : Rahul
Son1 School : YC College
Son1 Bike : Hero Honda

'''


