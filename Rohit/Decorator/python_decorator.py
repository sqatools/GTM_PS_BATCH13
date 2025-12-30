# decorator the enhance the functionality of existing code without changing it, then it is called decorator.

def decorator(func):
    def inner(param):
        print(" * "*10)
        func(param)
        print(" * "*10)
    return inner

@decorator

def greeting(mgs):
    print(mgs)

@decorator
def square(n):
    print("Square of n :", n**2)

greeting("Hello Good Morning")
print()
square(5)

'''
 *  *  *  *  *  *  *  *  *  * 
Hello Good Morning
 *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  *  * 
Square of n : 25
 *  *  *  *  *  *  *  *  *  * 
'''

print("-"*50)
###############################################################
## This value decorator can apply on any function, then it will print the value
# fixed number of value can not more than 10.

def value_checker(func):
    def inner(num):
        if num > 10:
            num = 10
            func(num)
        else:
            func(num)
    return inner

@value_checker

def get_sqaure_of_given_range(num):
    for i in range(1, num):
        print(i ,":",i**2 )

get_sqaure_of_given_range(20)

'''
1 : 1
2 : 4
3 : 9
4 : 16
5 : 25
6 : 36
7 : 49
8 : 64
9 : 81
'''