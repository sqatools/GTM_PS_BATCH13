class GrandDad:
    def __init__(self, first_name, last_name, business, age):
        self.first_name = first_name
        self.last_name = last_name
        self.business = business
        self.age = age

    def show_grand_dad_name(self):
        print("Dad's first and last name :", self.first_name+self.last_name)

    def show_grand_dad_age(self):
        print("Dad's age :", self.age)

    def show_grand_dad_details(self):
        print("Grand_Dad First Name :", self.first_name)
        print("Grand_Dad Last Name :", self.last_name)
        print("Grand_Dad's Business :", self.business)
        print("Grand_Dad's Age :", self.age)

class Dad(GrandDad):
    def __init__(self, dad_name, dad_job_title, first_name, last_name, business, age):
        super().__init__(first_name, last_name, business, age)
        self.dad_name = dad_name
        self.dad_job_title = dad_job_title

    def show_dad_details(self):
        print("Dad Name :", self.dad_name)
        print("Dad job title :", self.dad_job_title)


class Kid(Dad):
    def __init__(self, kid_name, dad_name, dad_job_title, first_name, last_name, business, age):
        super().__init__(dad_name, dad_job_title, first_name, last_name, business, age)
        self.kid_name = kid_name

    def show_kid_name(self):
        print("Kid's name is :", self.kid_name)

    def grand_family_details(self):
        print("Kids name :", self.kid_name)
        print("Family Details : ", self.show_dad_details())
        print("Grand Family Details :", self.show_grand_dad_details())


kd = Kid('Archie', 'Henry', 'HR Manager', 'Dave','Abby', 'Recruitment', '70')
kd.grand_family_details()