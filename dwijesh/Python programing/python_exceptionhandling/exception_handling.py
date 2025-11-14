



def exceptionhandling ():
    try:
        a1=100
        b1="abc"
        print("addition",a1+b1)
    except Exception as a:
        print(a)
        print("addition of string and int is not possible")
#############################################

def exceptionhandling1 (a,b):
    try:
        print("division", a // b)
        print("addition",a+b)
    except Exception as e:
        print(e)
        print("addition of string and int is not possible")
        raise
exceptionhandling1(10,"abc")

