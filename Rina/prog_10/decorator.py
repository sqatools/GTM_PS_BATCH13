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





