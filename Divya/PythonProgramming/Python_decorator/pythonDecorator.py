def decorator(func):
    def inner(param):
        print(" * "*10)
        func(param)
        print(" * " *10)
    return inner
@decorator
def greeting(msg):
    print(msg)

#This value decorator can apply on any function

def value_checker(func):
    def inner(num):
        if num > 10:
            num = 10
            func(num)
        else:
            func(num)
    return inner
@value_checker
def get_square_of_given_range(num):
    for i in range(1,num):
        print(i,":",i**2)

get_square_of_given_range(20)