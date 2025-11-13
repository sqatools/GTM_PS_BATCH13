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