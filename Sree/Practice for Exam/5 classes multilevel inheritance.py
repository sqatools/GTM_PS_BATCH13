
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
print('-'*30)

class parent1:

    def __init__(self,parname,parbuss,parcar):
        self.parent1name=parname
        self.parent1bussiness=parbuss
        self.parent1car=parcar

    def parent1details(self):
        print('parentname:',self.parent1name)
        print('parentbusiness:', self.parent1bussiness)
        print('parentcar:', self.parent1car)

class son1(parent1):
    def __init__(self, parname, parbuss, parcar,son1name,son1car):
        super().__init__(parname, parbuss, parcar)
        self.son1name=son1name
        self.son1car=son1car

    def son1details(self):

        print('son1name:',self.son1name)
        print('son1car:', self.son1car)


class son2(son1):
    def __init__(self, parname, parbuss, parcar, son1name, son1car,son2name,son2car):
        super().__init__(parname, parbuss, parcar, son1name, son1car)
        self.son2name = son2name
        self.son2car = son2car
    def son2details(self):
        print('son2name:', self.son2name)
        print('son2car:', self.son2car)
class son3(son2):
    def __init__(self, parname, parbuss, parcar, son1name, son1car, son2name, son2car,son3name,son3car):
        super().__init__(parname, parbuss, parcar, son1name, son1car, son2name, son2car)
        self.son3name = son3name
        self.son3car = son3car
    def son3details(self):
        print('son3name:', self.son3name)
        print('son3car:', self.son3car)
class son4(son3):
    def __init__(self, parname, parbuss, parcar, son1name, son1car, son2name, son2car, son3name, son3car,son4name):
        super().__init__(parname, parbuss, parcar, son1name, son1car, son2name, son2car, son3name, son3car)
        self.son4name=son4name
    def son4details(self):
        print('son4name:',self.son4name)
obj=son4('Ram','IT','HONDA','Rahul','Subaru','sheam','van','raj','jeep','guna')
obj.parent1details()
obj.son1details()
obj.son2details()
obj.son3details()
obj.son4details()
"""
*****
****
***
**
*
"""

for i in range(5,0,-1): #
   print(i* "*")
#########################
print()
for i in range (1,6):
    for j in range(i):
        print('*',end=" ")
    print()
for k in range(5,0,-1):
    for a in range(k):
        print('*',end=" ")
    print()
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
#########################################


print()
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
#############overridding############
class math:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def addition(self):
        print('additionvalue',self.n1+self.n2)
    def mul(self,v1,v2,v3):
        print("mulval",v1*v2,*v3)
class math2(math):
    def __init__(self, n1, n2,x,y):
        super().__init__(n1, n2)
        self.x=x
        self.y=y
    def div(self):
        print('div:',self.x /self.y)
    def mul(self,v1,v2):
        print('mul',v1*v2)
    def mess(self,wish):
        print("message", f"{wish}")
obj=math2(3,5,7,2)

obj.addition()
obj.mul(5,5)
obj.mess('hello')
####################################
"""
Polymorphism : when one method/variable with same name and perform multiple task, then it is called polymorphism.
1. method overriding: When 2 classes are connected to each with inheritance and have method with same name in both the class
                      then child class method will override the parent class method.

2. method overloading: Method overloading is not supported in python
                       -> When one class have 2 method with same but different parameter, then it is called method overloading.
                       -> but in python if we defined 2 method with same, name then latest defined method will get priority.

3. operator overloading: when one operator perform multiple task, then it is called operator overloading
                        e.g. plus(+) operator can add 2 int, it can add 2 string, it can add 2 list as well.

"""


class ABC:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        print("Addition :", self.n1 + self.n2)

    def multiplication(self, v1, v2, v3):
        print("multiply class ABC:", v1 * v2 * v3)


class XYZ(ABC):
    def __init__(self, var1, n1, n2):
        self.var1 = var1
        super().__init__(n1, n2)

    def square(self):
        print("square of var1 :", self.var1)

    # This method will override the multiplication method of parent class.
    def multiplication(self, x1, x2):
        print("multiply class XYZ:", x1 * x2)

    def greeting(self, name, msg):
        print(f"{msg}, {name}")

    # this is latest defined method will get priority
    def greeting(self, msg):
        print(f"{msg}")




obj = XYZ(var1 = 10, n1=20, n2=30)

obj.square() # square of var1 : 10
obj.addition() # Addition : 50
obj.multiplication(40, 50) # multiply class XYZ: 2000
#obj.greeting("Mohit", "Good Morning")
# TypeError: XYZ.greecting() takes 2 positional arguments but 3 were given

obj.greeting("Good Morning")  # Good Morning

print(dir(XYZ))

print("_"*50)
#############################################################
# operator overloading : when we call any operator, then python has some magic the called behind the seen to perform this operation
# with different operator and data types.

n1 = 100
n2 = 300
print("addition :", n1+n2)
print("addition :", n1.__add__(n2))
print(dir(int))



str1 = "Hello"
str2 = "Python"
print("string join:", str1 + str2)  # HelloPython
print("string join :", str1.__add__(str2)) # HelloPython

















