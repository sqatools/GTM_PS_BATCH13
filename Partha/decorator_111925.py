def decorator(func):
    def inner(param):
        print("*"*10)
        func(param)
        print("*"*10)
    return inner

@decorator
def greet(msg):
    print(msg)

@decorator
def square(x):
    print("Square of", x, ": ", x**2)

greet("Good Morning")
print("*")
square(3)

def table_num(func):
    def inner(num):
        if num > 11:
            num = 11
            func(num)
        else:
            func(num)
    return inner

@table_num
def table0f17(num):
    for i in range(num):
        if i != 0:
            print(i, ":", i*17)

table0f17(11)