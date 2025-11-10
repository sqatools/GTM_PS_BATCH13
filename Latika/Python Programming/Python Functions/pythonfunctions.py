# In Python "def" used to initialized function

def addition(x,y):
    """
    This function will provide addition of x and y
    :param x: first parameter
    :param y: second parameter
    :return:
    """
    result=x+y
    print("Addition is :",result)
# Pass by value
addition(36,26)

print()
# there are 2 ways to pass param data to the functions

# Pass by ref

a=100
b=50
addition(a,b)

# throws error if we don't provide required param

print()

# Function with default parameter

def math_operation(n1,n2=20):
    print("n1:",n1)
    print("n2:",n2)
    print("Addition of n1 and n2 is:",n1+n2)
    print("Subtraction of n1 and n2 is",n1-n2)

math_operation(80)

# Override default value of n2
math_operation(50,60)

# Functions with return statement

def get_sqr(num):
    return num **2
result=get_sqr(5)
print("Square of 5 is",result)

def get_cube(num):
    return num**3
result=get_cube(3)
print("Cube of 3 is:",result)

def get_sqr_get_cube(num):
    sqr=get_sqr(num)
    cb=get_cube(num)
    return sqr,cb
output =get_sqr_get_cube(7)
print("Output is:",output)

print()
print("."*100)

# note =return statement act as a break of function execution

def get_additional_value(num_range):
    sum=0
    for i in range(num_range):
        if sum>=20:
            return sum
        else:
            sum+=i
v1=get_additional_value(9)
print("The result of v1:",v1)




