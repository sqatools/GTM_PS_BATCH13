def excp_handle():
    try:
        a = (1,2,3)
        b = 'Sam'
        print("The Sum of  variable 'a' & 'b' is:", a+b)
    except Exception as excp:
        print(excp)
        print("Wrong data type")
excp_handle()
print("Goodbye")

print("*"*50)

