#5th Oct - 25
#In Python, a function is a named, reusable block of code designed to perform a specific task
#1. Defining a Function:
#Functions are defined using the def keyword, followed by the function name, parentheses (), and a colon :.
#The code block belonging to the function is indented.
#2. Calling a Function:
#To execute the code within a function, you "call" it by using its name followed by parentheses.
#3. Parameters and Arguments:
#Parameters: are placeholders defined in the function's signature that represent the values the function expects to receive.
#Arguments: are the actual values passed to the function when it is called.
#4. Return Values:
#Functions can optionally return a value using the return keyword. This value can then be used in other parts of the program.
#5.Types of Functions:
#User-Defined Functions: Functions created by the programmer to perform specific tasks.
#Built-in Functions: Pre-defined functions provided by Python (e.g., print(), len(), sum()).
#Anonymous (Lambda) Functions: Small, single-expression functions defined without a name, typically used for concise operations.
def addition(x,y):
    """This function will provide addition of x and y
    :param x : first parameter
    :param y : second parameter
    :retrun
    """
    result = x + y
    print("addition :", result)

# There are 2 ways to pass param data to the function
# 1. pass by value
# 2. pass by reference

#Pass by value - here we are directly passing the values to teh fuynction
addition(1, 2) #addition : 3

#pass by reference, instead of directlky passing values we are passing value through another variable
a = 200
b = 100
addition(a, b) #addition : 300

# throws error if we don't provide required params

#when no argument value is provided
#addition() # TypeError: addition() missing 2 required positional arguments: 'x' and 'y'

#when only 1 paramter is passed
#addition_values(50)
# TypeError: addition_values() missing 1 required positional argument: 'y'

#when extra paramter is passed, i.e instead of 2 - 3 is passed
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
# non default param has to come on left of the param list. i.e n1 where no value is defined
# default parma has to come on the right side of param list i.e n2- where value is defined
#we can define n no of default paramter, where value is defined
def math_operation(n1, n2=20):
    print("n1 :", n1)
    print("n2 :", n2)
    print("addition :", n1+n2)
    print("multiplication :", n1*n2)

print("_"*50)
# consider default value of n2
math_operation(30)# ehere 30 value is given for n1, while n2 will have default value
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
#if above math-operation want to retrun something
var = math_operation(20,30)
print("value of var :", var) #value of var : None
#above function doesnt have property to retrun , hence its retruning None
print("_"*50)

####################### Function with return statement #############
#whatver o/p the function is providing we want to store that in a variable
#so that it can be used in future, it can be used in another function

def get_square(n): #Function -1
    return n**2

def get_cube(n): #Function - 2
    return n**3

# call function inside function and store return value
def square_and_cube(num):#Function 3 - calling function 1 and function 2
    sqr = get_square(num)
    cb = get_cube(num)
    return sqr, cb #in a single return statement we can return any no of values

print("_"*50)
output = square_and_cube(7)
print("output :", output)  # (49, 343). Here sqr and cb retrun valus we are storing in o/p variable

#instead of passing the retrun value in a single statment, we have split o/p in storing in two variables a,b
a, b = square_and_cube(8)
print("square of 8 :", a)  # square of 8 : 64
print("cube of 8 :", b) # cube of 8 : 512

# note : return statement act as break for function execution.
#so basically once the function retruns a value - its stops the execution further
def get_addition_value(num_range):
    sum = 0
    for i in range(num_range):
        print(i)
        if sum >= 20:
            return sum #here i goes from 0-30, but sum when it hits 21 it terminates
            print("hello")  # code is unreachaable
            #once retrun is present, code post  that will become unreachable - wont get executed
        else:
            sum += i

v1 = get_addition_value(30)
print("v1 :", v1)
# v2 = get_addition_value(40)
# print("v2 :", v2)

#############################################################################
#6th Nov Class
# *args param accepts multiple values as param in the functions.
# args accepts the values in form of tuple

def accept_multiple_values(*args):
    print(args)
    for val in args:
        print(val)

print("_"*50)
accept_multiple_values(3, 4.5, 'Hello', [5, 7, 8], (3, 5, 7), {'a': 345})
"""
(3, 4.5, 'Hello', [5, 7, 8], (3, 5, 7), {'a': 345})

3
4.5
Hello
[5, 7, 8]
(3, 5, 7)
{'a': 345}

"""
print("_"*50)
############################
# **kwargs param accepts values in key value format as dict.

def users_details(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k ,":", v)


users_details(firstname='Mohit', lastname='Sharma', email='mohit@gmail.com', phone=654565464, DOB={'year':2025, 'month': 5, 'day': 20})
#users_details(firstname='Mohit', lastname='Sharma', email='mohit@gmail.com', DOB={'year':2025, 'month': 5, 'day': 20})

"""
{'firstname': 'Mohit', 'lastname': 'Sharma', 'email': 'mohit@gmail.com', 'phone': 654565464, 'DOB': {'year': 2025, 'month': 5, 'day': 20}}
firstname : Mohit
lastname : Sharma
email : mohit@gmail.com
phone : 654565464
DOB : {'year': 2025, 'month': 5, 'day': 20}
"""

