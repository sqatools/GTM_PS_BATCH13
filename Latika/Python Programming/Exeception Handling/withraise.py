
# raise Exception Explicitly

def handle_exception_with_raise(a,b):
    try:
        print("Addition is:",a+b)
        print("Division is:",a//b)
    except Exception as e:
        print(e)
        print("Addition is not allowed with int and str")
    except ZeroDivisionError:
        print("integer division or modulo by zero")

        raise
handle_exception_with_raise(10,6)
handle_exception_with_raise(7,'hello')
