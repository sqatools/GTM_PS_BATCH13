def addition_values(x, y):
    """
    This function will provide addition of x and y
    :param x: first parameter
    :param y: second parameter
    :return:
    """
    result = x + y
    print("addition :", result)

# There are 2 ways to pass param data to the function
# 1. pass by value
addition_values(30, 70)
addition_values(500, 800)

# 2. Pass by reference
a = 100
b = 200
addition_values(a, b)

# throws error if we don't provide required params

#addition_values(50)
# TypeError: addition_values() missing 1 required positional argument: 'y'

# addition_values(50, 40, 60)
# TypeError: addition_values() takes 2 positional arguments but 3 were given

def bill_calculator():
    fruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25, "lichi": 30, "Pinapple": 60}
    fruit_purchased = {"Banana": 12, "Apple": 10, "Mango": 5, "Watermelon": 2}
    # calculate total bill
    total_bill = 0

    for fruit, purches in fruit_purchased.items():
        f_price = fruit_price[fruit]
        fruit_bill = f_price * purches
        total_bill = total_bill + fruit_bill
        print(fruit, ":", f_price, ":", purches, ":", fruit_bill)

    print("_" * 20)
    print("Total bill :", total_bill)
#bill_calculator()

################ function with default parameter ###########
# non default param has to come on left of the param list.
# default parma has to come on the right side of param list
def math_operation(n1, n2=20):
    print("n1 :", n1)
    print("n2 :", n2)
    print("addition :", n1+n2)
    print("multiplication :", n1*n2)

print("_"*50)
# consider default value of n2
math_operation(30)
"""
n1 : 30
n2 : 20
addition : 50
multiplication : 600
"""

print("_"*50)
# override default value of n2 from 20 to 60
math_operation(50, 60)
"""
n1 : 50
n2 : 60
addition : 110
multiplication : 3000
"""

print("_"*50)
####################### Function with return statement #############
def get_square(n):
    return n**2


result = get_square(5)
print("square result :", result)

def get_cube(n):
    return n**3

# call function inside function and store return value
def square_and_cube(num):
    sqr = get_square(num)
    cb = get_cube(num)
    return sqr, cb

print("_"*50)
output = square_and_cube(7)
print("output :", output)  # (49, 343)

a, b = square_and_cube(8)
print("square of 8 :", a)  # square of 8 : 64
print("cube of 8 :", b) # cube of 8 : 512


# note : return statement act as break for function execution.

def get_addition_value(num_range):
    sum = 0
    for i in range(num_range):
        print(i)
        if sum >= 20:
            return sum
            #print("hello")  # code is unreachaable
        else:
            sum += i

v1 = get_addition_value(30)
print("v1 :", v1)
# v2 = get_addition_value(40)
# print("v2 :", v2)

# *args param accepts multiple values as param in the functions.
# args accepts the values in form of tuple

def accept_multiple_values(*args):
    print(args)
    for val in args:
        print(val)
accept_multiple_values(3, 4.5, 'Hello', [5, 7, 8], (3, 5, 7), {'a': 345})

# **kwargs param accepts values in key value format as dict.

def users_details(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k ,":", v)

users_details(firstname='Mohit', lastname='Sharma', email='mohit@gmail.com', phone=654565464, DOB={'year':2025, 'month': 5, 'day': 20})
#users_details(firstname='Mohit', lastname='Sharma', email='mohit@gmail.com', DOB={'year':2025, 'month': 5, 'day': 20})