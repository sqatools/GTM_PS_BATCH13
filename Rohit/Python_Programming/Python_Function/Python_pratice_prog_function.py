#1.Python function program to add two numbers
def addition_value (x,y):
    result = x+y
    print("Result of addition :",result) # Result of addition : 30
addition_value(10,20)
print("-"*50)

#########################################################################
#2. Python function program to print the input string 10 times.
def string_value(a,b):
    print("String value :",a*10)

string_value("Python",0) # PythonPythonPythonPythonPythonPythonPythonPythonPythonPython

print("-"*50)
#########################################################################
#3.Python function program to multiply all the numbers in a list
#Input : [-8, 6, 1, 9, 2]
def multiply(x,y,z,w,n):
    print("Multiply :",x*y*z*w*n) # Multiply : -864

multiply(-8, 6, 1, 9, 2)

print("-"*50)
#########################################################################
#4.Python function program to reverse a string
#Input: Python1234

def reverse_string(s):
    print(s[::-1])  # 4321nohtyP

reverse_string('Python1234')

print("-"*50)
#########################################################################
#5.Python function program to find the even numbers from a given list.
#Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_number(l):
    for val in l:
        if val%2==0:
            print("Even number :",val) # 2,4,6,8

l= [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_number(l)

print("-"*50)
#########################################################################
#6.Python function program to create and print a list where the values are
# squares of numbers between 1 to 10.
def square():
    for i in range(1,11):
        print("i :",i**2)

square()
print("-"*50)
#########################################################################
#7.Program to calculate the sum of numbers from 0 to 10
def sum():
    sum = 0
    for i in range(0,11):
        sum +=i
        print(sum)
sum()
'''
0
1
3
6
10
15
21
28
36
45
55
'''
print("-"*50)
###########################################################
#8. Python function program to find the sum of all the numbers in a list
# Input : [6,9,4,5,3]
def sum_number(l1):
    sum = 0
    for i in l1:
        sum += i
    print("Sum of numbers :",sum) #  27
l1 = [6,9,4,5,3]

sum_number(l1)

print("-"*50)
###########################################################
#9.Python function program to get the square of all values in the given dictionary.
#Input = {‘a’: 4, ‘b’ :3, ‘c’ : 12, ‘d’: 6}

def square_value(s):
   a = {}
   for k ,v in s.items():
    a[k] = v**2
    print("square of values :", a) # {'a': 16, 'b': 9, 'c': 144, 'd': 36}

s = {'a': 4, 'b' :3, 'c' : 12, 'd': 6}

square_value(s)

print("-"*50)
###########################################################
#10.Python function program to get a list of odd numbers from 1 to 100
def odd_number():
    for i in range(1,100):
        if i%2!=0:
            print("odd number :",i)
odd_number()

