def addition_values(x, y):
    """
    #This function will provide addition of x & y
    :param x : first parameter
    :param y : second parameter
    :return:
    """
    result = x+y
    print("addition :", result)

addition_values(30, 70)
addition_values(500, 800)

###function with default parameter########

def math_operation(n1, n2=20):
    print("n1 :", n1)
    print("n2 :", n2)
    print("addition :", n1+n2)
    print("multiplication :", n1 * n2)

print ("*"*50)

# override default value of n2
math_operation(50, 60) #now here 60 will override the original n2value)
# If we have atleast one variable with no default paramter then that can't be on the right side.has to be on left
print ("*"*50)

## Function with return statement
var = math_operation(50, 200)
print("var ", var)
# this will return var :None as it has nothing to return..

def get_square(n):
    return n**2

result = get_square(5)
print("square result :", result)
print ("*"*50)

def get_cube(n):
    return n**3

def square_and_cube(num):
    sqr = get_square(num)
    cb = get_cube(num)
    return sqr, cb
print ("*"*50)
output = square_and_cube(7)
print("output :", output)

# note : return statement act as a break for function execution. they are not last statement

def get_addition_values(num_range):
    sum = 0
    for i in range(num_range):
        if sum >= 20:
            return sum
        else:
            sum += i

v1 = get_addition_values(30)
print("v1 :", v1)
v2 = get_addition_values(40)
print("v2 :", v2)
#########
# *args param - accepts multiple valies as parameters in the functions
def accept_multiple_values(*args):
    print(args)
    for val in args:
        print(val)

accept_multiple_values(3, 4.5, 'hello', [5,7],{'a': 'hey'})

print("*"*50)

##############
# **kwargs parameter accepts values in key values

def users_details(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,":", v)

users_details(firstname = 'Mohit',lastname='Sharma', )

def emp_details(**kwargs):
    print(kwargs)
    for k, v in emp_details.items():
        print(k, ":", v)

emp_details(id =452,firstname ='Maddie',dept = 'HR',)




