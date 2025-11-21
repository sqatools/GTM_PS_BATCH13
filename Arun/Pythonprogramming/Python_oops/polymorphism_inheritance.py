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