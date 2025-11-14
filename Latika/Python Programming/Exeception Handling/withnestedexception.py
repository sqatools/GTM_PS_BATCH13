
def with_nested_exception_handle(a,b,c):
    try:
        print("Addition is:",a+b)
        try:
            print("Division is:",b//c)
        except Exception as e:
            print("Exception message is: ",e)
            print("Division with zero not allowed")
    except Exception as e1:
        print(e1)
        print("Addition of int and str is not allowed")

#with_nested_exception_handle(10,20,30)
#with_nested_exception_handle(4,5,0)
with_nested_exception_handle('hi',9,0)