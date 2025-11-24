from functools import wraps

def decorator(func):
    @wraps(func)
    def inner(param):
        print(" * " * 10)
        func(param)
        print(" * " * 10)
    return inner

@decorator
def greeting(msg):
    print(msg)

greeting("Good Morning")
print('_'*33)
def decorator(func):
    @wraps(func)
    def inner(param):
        if param > 10:     # its true 20 is greater than 10
            param=10
            func(param)
        else:
            func(param)
    return inner


@decorator
def getsquarofgivenrange(num):
    for i in range(1,num):
        print(i,':',i**2)
getsquarofgivenrange(20)