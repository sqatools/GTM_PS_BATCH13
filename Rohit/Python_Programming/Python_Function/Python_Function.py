def addition_values(x,y):
    """
     This function will provide addition of x and y
     :param x: first parameter
     :param y: second parameter
     :return:
     """

    result = x + y
    print("Addition of values :",result)  # 8 , 12

# There are 2 ways to pass param data to the function
# 1. pass by value
addition_values(2,6)
addition_values(3,9)

# 2. Pass by reference
a= 50
b= 60
addition_values(a,b)

# throws error if we don't provide required params
#addition_values(55)
# TypeError: addition_values() missing 1 required positional argument: 'y'

################ function with default parameter ###########
# non default param has to come on left of the param list.
# default parma has to come on the right side of param list

print("-"*50)

def multiplication_Value(a,b=20):
    print("a :", a)
    print("b :", b)
    print("Addition :",a+b)
    print("Multiplication :",a*b)
    print("Subtraction :",a-b)

multiplication_Value(10)
"""
a : 10
b : 20
Addition : 30
Multiplication : 200
Subtraction : -10
"""

print("-"*50)
#######################################################
def get_square(n):
    return n**2
result = get_square(4)
print("result of square :", result)

def get_cube(n):
    return n**3
result1 = get_cube(3)
print("result of cube :", result1)

print("-"*50)

# call function inside function and store return value
def get_square_cube(num):
    sqr = get_square(num)
    cub = get_cube(num)
    return sqr , cub
output = get_square_cube(2)
print("Output of square and cube :", output) # (4, 8)

a,b = get_square_cube(3)
print("square of a :", a) # 9
print("cube of b :", b) #  27

# note : return statement act as break for function execution.

def get_addition_value(num_range):
    sum = 0
    for i in range(num_range):
        print(i)
        if sum >= 20:
            return sum
            # print("hello")  # code is unreachaable
        else:
            sum += i

v1 = get_addition_value(10)
print("v1 :", v1)
'''
0
1
2
3
4
5
6
7
v1 : 21
'''
print("-"*50)
###########################################################################
# *args param accepts multiple values as param in the functions.
# args accepts the values in form of tuple

def addition_values(*args):
    print(args)
    for val in args:
        print(val)

addition_values(2,4.6,[3,5,7],{3,6,8},"Hello",(3,5,8))
'''
(2, 4.6, [3, 5, 7], {8, 3, 6}, 'Hello', (3, 5, 8))
2
4.6
[3, 5, 7]
{8, 3, 6}
Hello
(3, 5, 8)
'''

print("-"*50)
############################
# **kwargs param accepts values in key value format as dict.
def emp_details(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, ":", v)

emp_details(first_name= "Rohit", Last_Name = "Chavan",Emp_id = 4102, Phone= 9158520006,DOB={'year':2025, 'month': 5, 'day': 20})
'''
{'first_name': 'Rohit', 'Last_Name': 'Chavan', 'Emp_id': 4102, 'Phone': 9158520006, 'DOB': {'year': 2025, 'month': 5, 'day': 20}}
first_name : Rohit
Last_Name : Chavan
Emp_id : 4102
Phone : 9158520006
DOB : {'year': 2025, 'month': 5, 'day': 20}
'''

