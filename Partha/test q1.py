a=int(input("Enter the First Number: "))
op=(input("Enter the Operation: "))
b=int(input("Enter the Second Number: "))
if op=="+":
    print("The Sum is:", a+b)
elif op=="-":
    print("The Subtraction is:", a-b)
elif op=="*":
    print("The Multiplication is:", a*b)
elif op=="/":
    if b==0:
        print("Division by Zero error")
    else:
        print("The division is:", a/b)
else:
    print("Error: Invalid Operator")
