print("Python program to check given number is divided by 3 or not.")

num1=int(input("Please enter a no : "))

if num1%3==0:
    print("The",num1 ,"is divisible by 3")
else:
    print("The",num1 ,"is not divisible by 3")


print("."*100)

print("If-else program to assign grades as per total marks")

"""
Marks less than 40: Fail
Marks between 40-50: Grade C
Marks between 51-60: Grade B
Marks between 61-70: Grade A
Marks between 71-80: Grade A+
Marks between 81-90: Grade A++
Marks between 91-100: Excellent
"""

marks=int(input("Enter the marks :"))

if marks<40:
    print("The result is fail")
elif marks >=40 and marks <=50:
    print("Grade C")
elif marks >=51 and marks <=60:
    print("Grade B")
elif marks >=71 and marks <=70:
    print("Grade A")
elif marks >=81 and marks <= 90:
    print("Grade A+")
elif marks>=91 and marks <=100:
    print("Grade A++")
else:
    print("Invalid Marks/Entry")


