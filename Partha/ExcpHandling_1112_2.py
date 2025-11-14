def excp_raise(a,b,c):
    try:
        print("Concatenated Value of tuples a & b is", a+b)
        print("Concatenated Value of tuples a & c is", a+c)
    except Exception as excp:
        print(excp)
        print("Wrong data type")
        raise

excp_raise((1,2,3),4,(5,6,7))

print("*"*50)

