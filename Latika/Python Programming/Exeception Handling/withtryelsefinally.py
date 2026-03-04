
# finally will always execute, if there is exception or not

def with_try_except_else_finally(a,b,c):
    try:
        print("addition is",a+b)
    except Exception as e:
        print("Exception error message: ",e)

    else:
        print("Code run is pass")
    finally:
        for i in range(1,11):
            print(i,"*",c,"=",i*c)

#with_try_except_else_finally(10,6,9)
with_try_except_else_finally(5,'Functions','hello')
