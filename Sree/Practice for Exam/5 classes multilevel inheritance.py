
class class1:
    def student1(self):
        print('stud1')
class class2(class1):
    def student2(self):
        print('stud2')
class class3(class2):
    def student3(self):
        print('stud3')
class class4(class3):
    def student4(self):
        print('stud4')
class class5(class4):
    def student5(self):
        print('stud5')
obj=class5()
obj.student1()
obj.student2()
obj.student3()
obj.student4()
obj.student5()




