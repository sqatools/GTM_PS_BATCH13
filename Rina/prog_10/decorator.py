def decorator(func):
    def inner(param):
        print("^_^"*10)
        func(param)
        print("^_^"*10)
    return inner

@decorator
def greeting(msg):
    print(msg)

@decorator
def square(n):
    print("square of n: ", n**2)

greeting("Good morning")
print("^_^")
square(55)



def value_cheker(func):
    def inner (num):
        if num > 20:
            num = 20
            func(num)
        else:
            func(num)

    return inner

@value_cheker
def get_square_of_given_range(num):
    for i in range(1, num):
        print(i, ":", i**2)

print("+"*50)
get_square_of_given_range(30)


