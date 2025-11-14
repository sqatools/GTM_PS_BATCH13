
def handle_with_try(a,b):
    try:
       print("Addition is:",a+b)
    except Exception as e:
        print(e)
        print("addition of int and str are not allowed")

#handle_with_try(10,'hello')
handle_with_try(3,10)
print("Good Morning")
