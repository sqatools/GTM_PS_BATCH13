"""class father:

    def __init__(self,fname,fbusiness,faddress):
        self.f_name=fname
        self.f_business=fbusiness
        self.f_address=faddress
    def show_fathername(self):
        print(self.f_name)
    def show_fatherbusiness(self):
        print(self.f_business)
    def show_fatheraddress(self):
        print(self.f_address)
    def show_all_father_detail(self):
        self.show_fathername()
        self.show_fatherbusiness()
        self.show_fatheraddress()
 #child class or base class
class son(father):

    def __init__(self, sonname, fname, fbusiness, faddress):
        super().__init__(fname, fbusiness, faddress)
        self.son_name=sonname

    def show_sonname(self):
        print(self.son_name)

    def family_details(self):
        self.show_all_father_detail()
        self.show_sonname()

obj=son("Rohan",'Ram','ITbusiness','India')
obj.family_details()
print("-"*45)
class parent:
    def __init__(self,pname,pjob,pcar):
        self.parent_name=pname
        self.parent_job=pjob
        self.parent_car=pcar
    def show_parentname(self):
        print('parentname:',self.parent_name)
    def show_parentjob(self):
        print('parentjob:',self.parent_job)
    def show_parentcar(self):
        print('parentcar:',self.parent_car)
    def Parent_details(self):
        self.show_parentname()
        self.show_parentjob()
        self.show_parentcar()
class kid(parent):

    def __init__(self, kidname, pname, pjob, pcar):
        super().__init__(pname, pjob, pcar)
        self.kid_name=kidname
    def show_kidname(self):
        print('kidname:',self.kid_name)
    def family_details(self):
        self.Parent_details()
        self.show_kidname()
obj=kid('Lucky','Sham','worker','Honda')
obj.family_details()
"""
print('-'*45) ## Multilevel inheritance
"""
class grandfather:
    def __init__(self,g_name,g_age):
        self.grandfathername=g_name
        self.grandfatherage=g_age
    def show_GFname(self):
        print("Grandfathername:",self.grandfathername)
    def show_GFage(self):
        print('GrandfatherAge:',self.grandfatherage)
    def Grandfather_detail(self):
        self.show_GFname()
        self.show_GFage()
class father(grandfather):
    def __init__(self, f_name, f_age, g_name, g_age):
        super().__init__(g_name, g_age)
        self.fathername=f_name
        self.fatherage=f_age
    def show_father_name(self):
        print("fathername:",self.fathername)
    def show_father_age(self):
        print('fatherage:',self.fatherage)
    def father_details(self):
        self.show_father_name()
        self.show_father_age()
class son(father):
    def __init__(self, s_name, f_name, f_age, g_name, g_age):
        super().__init__(f_name, f_age, g_name, g_age)
        self.son_name=s_name
    def show_sonname(self):
        print("sonname:",self.son_name)
    def wholefamilydetails(self):
        self.Grandfather_detail()
        self.father_details()
        self. show_sonname()
obj=son("kranthi",'sham','50','kknayudu',"80")
obj.wholefamilydetails()
"""
print('-'*45) # Multiple level
class father:
    def __init__(self,fname,fjob):
        self.fathername=fname
        self.fatherjob=fjob
    def show_fatherdetails(self):
        print(self.fathername)
        print(self.fatherjob)

class mother:
    def __init__(self,mname,mbusiness):
        self.mothername=mname
        self.motherbusiness=mbusiness
    def show_motherdetails(self):
        print("mothername:",self.mothername)
        print('motherbusiness',self.motherbusiness)

class son(father,mother):
    def __init__(self, sname, fname, fjob,mname,mbusiness):
        super().__init__(fname, fjob)
        self.sonname=sname
        self.mothername = mname
        self.motherbusiness = mbusiness
    def show_sonname(self):
        print(self.sonname)
    def familydetails(self):
        self.show_fatherdetails()
        self.show_sonname()
        self.show_motherdetails()
obj=son("ram",'sham','IT','syamala','teacher')
obj.familydetails()
