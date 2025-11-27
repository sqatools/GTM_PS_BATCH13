

num1=int(input("Enter the 1st no :"))
num2=int(input("Enter the 2nd no:"))
opr=input("Enter the (+, -, *, /) operator :")

if opr == "+":
    print("num1 and num2 addition is :",num1+num2)
if opr == "-":
    print("num1 and num2 substraction is :",num1-num2)
if opr == "/":
    print("num1 and num2 Division is :",num1//num2)
if opr == "*":
    print("num1 and num2 Multiplication is :", num1 * num2)
elif opr == None:
    print("Invalid operator")



