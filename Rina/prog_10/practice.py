"""
numa = 50
numb = 60
print("addition : ", numa + numb)
print("subtraction : ", numa - numb)
print("multiplication :", numa*numb)

str1 = "SQATools"
n1 = 6
print("result :", str1*n1)

a = 40
b = 50
c = 30
print("Avg : ", (a + b + c)/3)

values = [10, 20, 30, 40, 50, 60]
values.sort()
n = len(values)

if n % 2 == 1:
    median_value = values[n // 2]
else:
    median_value = (values[n // 2 - 1] + values[n // 2]) / 2

print(f"The median is: {median_value}")

import math
num1 = 169
print(math.sqrt(num1))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

while(True):
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1

print(f"L.C.M of {num1} and {num2}: {lcm}")


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
if num1 > num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller+1):
    if((num1 % i == 0) and (num2 % i ==0)):
        hcf = i
print(f"H.C.F of {num1} and {num2}: {hcf}")

num = int(input("Enter a number up to which you want to find sum: "))
total = 0
for i in range(1,num+1):
    total += 1
print("Total : ", total)

num = int(input("Enter a number up to which you want to find sum: "))
total = 0

for i in range(1,num+1):
    total += i

print("Total: ",total)

num = int(input("Enter a number: "))
print(f"Binary form of {num} is: ","{0:b}".format(int(num)))

import datetime
dt = datetime.datetime.now()
print("Current date: ", dt)

from _datetime import date
date_1 = date(2025, 1, 21)
date_2 = date(2024, 11, 12)
result = (date_1 - date_2).days
print("Calculate the days between days : ", result, "days")

class Myclass:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name: ", self.name)

obj = Myclass("Rina")
obj.display_name()



class MyClass:
    def __init__(self):
        self.instance_var = 80
obj = MyClass()
print(obj.instance_var)


class MyClass:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name: ", self.name)

    def updated_name(self, new_name):
        self.name = new_name

obj = MyClass("Rina")
obj.display_name()

obj.updated_name("RinaR")
obj.display_name()

class MyClass:
    class_var = "Hello"
print(MyClass.class_var)


class MyClass:
    @staticmethod
    def static_method():
        print("New Static Method")

MyClass.static_method()

class MyClass:
    calss_var = "Hello"
    @classmethod
    def class_method(cls):
        print("Class Var: ", cls.calss_var)

MyClass.class_method()

class MyClass:
    pass
obj = MyClass()
print("Class name: ", obj.__class__.__name__)
print("Module name: ", obj.__module__ )
"""

class ParentCalss1:
    def parent_method1(self):
        print("Parent Mathod1: ")
class ParentClass2:
    def parent_method2(self):
        print("Parent Method2: ")
class ChildClass(ParentCalss1, ParentClass2):
    def child_method(self):
        print("Child mehod: ")
obj = ChildClass()
obj.parent_method1()
obj.parent_method2()
obj.child_method()
