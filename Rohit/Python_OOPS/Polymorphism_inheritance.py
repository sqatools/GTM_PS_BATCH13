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

#1. method overriding:

class ABC():
    def __init__(self, n1 , n2):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        print("Addition :", self.n1 + self.n2)

    def multiplication(self):
        print("Multiplication :", self.n1 * self.n2)

class XYZ(ABC):
    def __init__(self, a, n1, n2):
        super().__init__(n1, n2)
        self.a = a

    def square(self):
        print("Square :", self.a**2)

    def multiplication(self, x1, x2):  #This will take
        print("Multiplication :", x1*x2)

obj = XYZ(2,3,5)
obj.addition()
obj.multiplication(2,3)
obj.square()

'''
Addition : 8
Multiplication : 6
Square : 4
'''

print("-"*50)
########################################
#2. method overloading:

class Addition():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def Result_Addition(self):
        print("Addition :", self.n1+self.n2)

    def multiplcation(self):
        print("Multiplication :", self.n1*self.n2)

class Sum(Addition):
    def __init__(self, s1, n1, n2):
        super().__init__(n1, n2)
        self.s1 = s1

    def show_sum(self):
        print("Square :", self.s1**2)

    def greeting(self,name,mgs):
        print(f"{name},{mgs}")

    def greeting(self, mgs): #This will take
        print(f"{mgs}")

obj = Sum(2,10,20)
obj.multiplcation()
obj.Result_Addition()
#obj.greeting('Rohit',"Hello")
#TypeError: Sum.greeting() takes 2 positional arguments but 3 were given

obj.greeting("Hello Good Morning")

'''
Multiplication : 200
Addition : 30
Hello Good Morning
'''

print("-"*50)
################################################
#3. operator overloading : when we call any operator, then python has some magic the called behind the seen to perform this operation
# with different operator and data types.

n1 = 20
n2 = 30

print("Addition :", n1+n2)
print("Addition :", n1.__add__(n2))

'''
Addition : 50
Addition : 50
'''

str1 = "Hello"
str2 = "Good Morning"

print("String Join :", str1+str2)
print("String Join :", str1.__add__(str2))

'''
String Join : HelloGood Morning
String Join : HelloGood Morning

'''

print(dir(int))
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__',
# '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__g

print("substraction :", n1-n2)
print("Division :", n1.__sub__(n2))