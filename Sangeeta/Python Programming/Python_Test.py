# Python Test - 11/25/2025

print("\n Section B – Multiple-Choice Questions (10 Questions) \n")
print (" \n Q6. What is the correct file extension for Python files?\n Ans = B. '.py'")
print ("\n Q7. Which of the following is used to take input from the user in Python? \n Ans = C. 'input()' ")
print("\n Q8. What is the output of the following code? \n Ans = A.'2.5'")
print("\n Q9. Which of the following is not a valid Python data type? \n Ans = C. 'array',")
print("\n Q10. How do you start a comment in Python? \n Ans = B. '# comment' ")
print("\n Q11. What is the output of the following code? \n Ans = B. '20 10' ")
print("\n Q12. Which of the following is the correct way to define a function in Python?\n Ans =C. def myFunc(): ")
print("\n Q13. What will be the output of the following code? \n Ans = 'B. 4' ")
print("\n Q14. Which keyword is used to exit a loop in Python? \n Ans = 'D. break' ")
print("\n Q15. What is the output of the following code? \n Ans  = '# C. 3 4 5' ")
print("\n Q16. Which of the following is used to handle exceptions in Python? \n Ans = 'A. try-except'\n ")

print("-*-" * 50)
print(' ')

print('''Q1 - Write a Python program that:
 Takes two numbers and an operator (+, -, *, /) as input from the user.
 Performs the corresponding operation.
 Prints the result.
 If the operator is invalid, print &quot;Invalid operator&quot;.)
''')

print("Please enter any number of your choice :")
a = int(input())
print("Please enter another number :")
b = int(input())
print("Select any one of the operator of your choice from this list - (+, -, *, /)")
c = str(input())

a1 = '+'
b1 = '-'
c1 = '*'
d1 = '/'

if c in a1:
    print("Addition result is :", a+b)
elif c in b1:
    print("Subtraction of a and b results to :", a-b)
elif c in c1:
    print("Multiplication of a and b results to :", a*b)
elif c in d1:
    print("Division of a and b results to :", a/b)
else:
    print("Invalid Operator")

print("-*-" * 50)

print(" Write a Python program that:\n  Takes an integer as input from the user.\n  Checks whether the number is prime or not prime.\n  Prints an appropriate message.")

B = int(input("Enter a number of your choice :"))
if B == 0:
   print('ZeroDivisionError')
elif B>0 and B%B ==0 and B%1 == B:
   print("It is a prime number")
else:
    print("It is not a prime number")

