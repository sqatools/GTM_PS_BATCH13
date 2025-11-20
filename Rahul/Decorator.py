def decorator(func):

    def inner(param):
        print(" * "*10)
        func(param)
        print(" * " * 10)
    return inner

def greeting(msg):
    print(msg)

greeting("Go to the GYM")

