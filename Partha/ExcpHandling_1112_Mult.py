def mult_excp(a,b,c,d,e=5):
    try:
        print("Square of first parameter is: ", a**2)
        print("Square of second parameter is: ", b**2)
        assert c == d/2, "third parameter is exactly half of fourth parameter"
        product = d*e
    except TypeError:
        print("Wrong data type. Only integers allowed")
    except ZeroDivisionError:
        print("Division by zero")
    except AssertionError:
        print("d is not half of c")
    except Exception as excp:
        print(excp)
        print("Runtime error")

mult_excp(1,0,2,4,5)
