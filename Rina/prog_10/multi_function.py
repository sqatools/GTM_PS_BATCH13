"""
def handle_multiple_exception(a, b, c, d):
    try:
        print("addition: ", a+b)
        print("division: ", b//c)
    except TypeError:
        print("All input values should be number")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except AssertionError:
        print("Both values are not equal:", c, d)
    except Exception as e:
        print(e)
        print("Program failed with error")
handle_multiple_exception(10, 5, 'p', 'r')
"""
def handle_nested_level_exception(a, b, c):
    try:
        print("addition: ", a+b)
        try:
            div = b//c
            print("Division: ", div)
        except Exception as e1:
            print(e1)
            print("Addition of int and string is not allowed.")
    except Exception as e2:
        print(e2)
        print("Division of int and string is not allowed.")

handle_nested_level_exception(10, 'a', 3)