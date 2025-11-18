class Father():
    def __init__(self,f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_Car = f_car

    def father_details(self):
        print("Father Name :", self.father_name)
        print("Father Business :", self.father_business)
        print("Father Car :", self.father_Car)

class Mother():
    def __init__(self, m_name, m_business, m_car):
        self.mother_name = m_name
        self.mother_business = m_business
        self.mother_car = m_car

    def mother_details(self):
        print("Mother Name :", self.mother_name)
        print("Mother Business :", self.mother_business)
        print("Mother Car :", self.mother_car)

class Son(Father, Mother):
    def __init__(self, s_name, f_name, f_business, f_car, m_name, m_business, m_car):
        super().__init__(f_name, f_business, f_car)
        self.mother_name = m_name
        self.mother_business = m_business
        self.mother_car = m_car
        self.Son_name = s_name

    def show_Son_name(self):
        print("Son Name :", self.Son_name)

    def family_details(self):
        self.father_details()
        self.mother_details()
        self.show_Son_name()


obj = Son('Rohit','Ramchandra','Medical Store','Audi','Rajashri','Showroom','BMW')
obj.family_details()

'''
Father Name : Ramchandra
Father Business : Medical Store
Father Car : Audi
Mother Name : Rajashri
Mother Business : Showroom
Mother Car : BMW
Son Name : Rohit
'''
