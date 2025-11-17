class grandfather:
    def __init__(self, gf_name, gf_property):
        self.grandfather_name = gf_name
        self.property = gf_property


    def  grandfather_details (self):
        print (self.grandfather_name)
        print (self.property)



class father(grandfather):
    def __init__(self, f_name, f_car, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.father_name = f_name
        self.father_car = f_car

    def father_details(self):
        print(self.father_name, "and", self.father_car)


class son(father):
    def __init__(self, s_name, f_name, f_car, gf_name, gf_property):
        super().__init__(f_name, f_car, gf_name, gf_property)

        self.son_name = s_name

    def son_details(self):
        print(self.son_name)

    def family_details(self):
        self.grandfather_details()
        self.father_details()
        self.son_details()


obj = son("Rahul", "Mr. Ram", "Audi", "Shyam","10 Acr")
obj.family_details()