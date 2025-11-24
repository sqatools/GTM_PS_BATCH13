# Decorator us used to enhance functionality of an existing code without changing it.

def Morning(func):
    print("Good Morning")
    def greet():
        print("Before func-greet, say Morning")
        func()
        print("After func-greet, say Good Day")
    return greet

@Morning
def greeting():
    print("Hello we are learning Python")

# result_func = Morning(greeting)
# result_func()

greeting()