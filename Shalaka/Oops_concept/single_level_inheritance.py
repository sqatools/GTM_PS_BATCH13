class father:
    def __init__(self, f_name, f_car):
        self.father_name = f_name
        self.father_car = f_car
        
        
    def father_details(self):
        print(self.father_name, "and", self.father_car)
        
    
class son(father):
    def __init__(self, s_name, f_name, f_car):
        super().__init__(f_name, f_car)
        self.son_name= s_name

    def son_details(self):
        print (self.son_name)

    def family_details(self):
        self.father_details()
        self.son_details()


obj = son("Rahul","Mr. Ram", "Audi")
obj.family_details()