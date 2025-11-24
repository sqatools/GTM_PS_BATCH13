#1FATHER & 2 SON'S

class father:

    def __init__(self,fname,fbusiness,faddress):
        self.fathername=fname
        self.fatherbusiness=fbusiness
        self.fatheraddress=faddress
    def display_fatherdetails(self):
        print('fathername:',self.fathername)
        print('fatherbuseniess:',self.fatherbusiness)
        print('fatheraddress:',self.fatheraddress)
class son1(father):
    def __init__(self, sonname, sonbusiness, soncar, fname, fbusiness, faddress):
        super().__init__(fname, fbusiness, faddress)
        self.son_name=sonname
        self.son_business=sonbusiness
        self.son_car=soncar
    def display_son1details(self):
        print('son1name:',self.son_name)
        print('son1business:',self.son_business)
        print('son1car:',self.son_car)

    def family_details(self):
        self.display_fatherdetails()
        self.display_son1details()


class son2(father):
    def __init__(self, sonname, sonjob, sonpet, fname, fbusiness, faddress):
        super().__init__(fname, fbusiness, faddress)
        self.son_name=sonname
        self.son_job=sonjob
        self.son_pet=sonpet
    def display_son2details(self):
        print('son2name:',self.son_name)
        print('son2job:',self.son_job)
        print('son2petname:',self.son_pet)
    def family_details(self):
        self.display_fatherdetails()
        self.display_son2details()
obj1= son1('ram','grocerystore','Honda','Bheem','IT','NY')
obj2=son2('sham','software','dog','Bheem','IT','NY')
obj1.family_details()
obj2.family_details()
    


    