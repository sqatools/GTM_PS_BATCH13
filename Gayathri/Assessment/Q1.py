"""Q1. Simple Calculator (Using if-else)
Write a Python program that:
•	Takes two numbers and an operator (+, -, *, /) as input from the user.
•	Performs the corresponding operation.
•	Prints the result.
•	If the operator is invalid, print "Invalid operator".
"""
num1 = int(input("Enter a number one: ")) #using int - so we take integer number only
num2 = int(input("Enter a number two: "))
operator = input("Enter a operator (+, -, *, /): ")
result = 0 #taking the variable as 0 - so we can use this to store the value inside loop

if operator == '+':
    result =  num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Invalid operator")

print("result of the operation is :", result)

"""
Output of the program:
Enter a number one: 20
Enter a number two: 10
Enter a operator (+, -, *, /): +
result of the operation is : 30

--------------------------------------------------------------------------
Enter a number one: 20
Enter a number two: 10
Enter a operator (+, -, *, /): -
result of the operation is : 10
--------------------------------------------------------------------------
Enter a number one: 20
Enter a number two: 10
Enter a operator (+, -, *, /): *
result of the operation is : 200
________________________________________________________________________
Enter a number one: 20
Enter a number two: 10
Enter a operator (+, -, *, /): /
result of the operation is : 2.0  - Here we got decimal as its /, if we give // decimal will
not be there
-----------------------------------------------------------------------
Enter a number one: 20
Enter a number two: 10
Enter a operator (+, -, *, /): &
Invalid operator
result of the operation is : 0
"""
