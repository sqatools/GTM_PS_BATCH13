def handle_exception():
    try:
        r = 4
        k = 'rahul'
        print("Addition:", r+k)
    except Exception as e:
        print(e)
        print("its not possible to add")



def handle_nested_level_exception(a, b, c):
    # outer exception block
    try:
        print("Addition:", a+b)
        try:
            # inner exception block
            div = b//c
            print("division :", div)
        except Exception as e2 :
            print(e2)
            print("Division with zero is not allowed")
    except Exception as e1:
        print(e1)
        print("Addition of int and string is not allowed")