
# else block will only execute when there is no exception

def with_try_else_exception(a,b):

    try:
        #b='hello'
        print("addition of ",a+b)
    except Exception as e:
        print(e)
        print("Addition is not allowed")
    else:

        print("Successful")

with_try_else_exception(10,20)



