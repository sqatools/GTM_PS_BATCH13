class Dad:
    def __init__(self, first_name, last_name, business, age):
        self.first_name = first_name
        self.last_name = last_name
        self.business = business
        self.age = age

    def show_dad_name(self):
        print("Dad's first and last name :", self.first_name+self.last_name)

    def show_dad_age(self):
        print("Dad's age :", self.age)

    def show_dad_details(self):
        print("Dad First Name :", self.first_name)
        print("Dad Last Name :", self.last_name)
        print("Dad's Business :", self.business)
        print("Dad's Age :", self.age)

class Kid(Dad):
    def __init__(self, kid_name,first_name,last_name, business, age):
        super().__init__(first_name, last_name, business, age)
        self.kid_name = kid_name

    def show_kid_name(self):
        print("Kid's name is :", self.kid_name)

    def family_details(self):
        print("Kids name :", self.kid_name)
        print("Family Details : ", self.show_dad_details())


kd = Kid('Ashley', 'Henry', 'Thomas', 'Artist', 40)
kd.family_details()







