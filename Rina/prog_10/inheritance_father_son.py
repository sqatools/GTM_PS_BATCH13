class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.grandfather_name = gf_name
        self.grandfather_property = gf_property

    def show_grand_father_details(self):
        print("Grandfather Name: ", self.grandfather_name)
        print("Grandfather Property: ", self.grandfather_property)

# parent class
class father(GrandFather):
    def __init__(self, f_name, f_business, f_car, f_house, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.father_name = f_name
        self.father_business = f_business
        self.father_car = f_car
        self.father_house = f_house

    def show_father_name(self):
        print("Father Name: ", self.father_name)

    def show_father_business(self):
        print("Father Business: ", self.father_business)

    def show_father_car(self):
        print("Father Car: ", self.father_car)

    def show_father_house(self):
        print("Father House: ", self.father_house)

    def show_all_details_of_father(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_car()
        self.show_father_house()

# Child class

class Son(father):
    def __init__(self, s_name, f_name, f_business, f_car, f_house, gf_name, gf_property):
        super().__init__(f_name, f_business, f_car, f_house, gf_name, gf_property)
        self.son_name = s_name

    def show_son_name(self):
        print("Son Name: ", self.son_name)

    def family_details(self):
        self.show_grand_father_details()
        self.show_all_details_of_father()
        self.show_son_name()

obj = Son('Raj', 'Rajendra', 'Racing', 'RR', 'Royal', 'Ravinath', '10cr.')
obj.family_details()




