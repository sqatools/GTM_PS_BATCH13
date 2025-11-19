class father:
    def __init__(self, f_name, f_business, f_car):
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car

    def show_father_name(self):
        print("Father Name :", self.father_name)

    def show_father_business(self):
        print("Father Business :", self.father_business)

    def show_father_car(self):
        print("Father car :", self.father_car)

    def show_all_details_of_father(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()

class mother:
    def __init__(self, m_name, m_hobby):
        self.mother_name = m_name
        self.mother_hobby = m_hobby

    def show_mother_details(self):
        print("Mother Name :", self.mother_name)
        print("Mother Hobby :", self.mother_hobby)

class son(father, mother):
    def __init__(self, s_name, f_name, f_business, f_car, m_name, m_hobby):
        super().__init__(f_name, f_business, f_car)
        self.mother_name = m_name
        self.mother_hobby = m_hobby
        self.son_name = s_name

    def show_son_name(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.show_all_details_of_father()
        self.show_mother_details()
        self.show_son_name()

obj = son("father", "Busniess", "Car", "Mother", "Hobby", "Son")
obj.family_details()


