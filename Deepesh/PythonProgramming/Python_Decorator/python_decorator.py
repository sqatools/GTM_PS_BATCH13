# decorator the enhance the functionality of existing code with out changing it, then it is called decorator.

def decorator(func):
    def inner(param):
        print(" * "*10)
        func(param)
        print(" * " * 10)
    return inner

@decorator
def greeting(msg):
    print(msg)

@decorator
def square(n):
    print("square of n :", n**2)

greeting("Good Morning")
square(5)

# This value decorator can apply on any function, then it will print the value
# fixed number of value can not more than 10.
def value_cheker(func):
    def inner(num):
        if num > 10:
            num = 10
            func(num)
        else:
            func(num)

    return inner

@value_cheker
def get_square_of_given_range(num):
    for i in range(1, num):
        print(i, ":", i**2)


print("_"*40)
get_square_of_given_range(20)