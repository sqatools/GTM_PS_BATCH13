# pattern program
"""
*
* *
* * *
* * * *
* * * * *
"""
from http.cookiejar import uppercase_escaped_char

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
print("-"*50)

############################################################
"""
* * * * *
* * * *
* * *
* * 
* 
"""
for i in range(6, 0, -1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()
#############################################
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
print("-"*50)

#####################################################################
## thon program to check given number is divided by 3 or not.

b=9
if b%3==0:
    print("The given number is divided by 3:",b)
else:
    print("The given number is not divided by 3:",b)

print("-"*50)

b=17
if b%3==0:
    print("The given number is divided by 3:",b)
else:
    print("The given number is not divided by 3:",b)

print("-"*50)

#####################################################################
## If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1,30):
    if i%3==0:
        print(i)
    else:
        continue

print("-"*50)

for i in range(1, 31):
    if i % 3 == 0:
        print(i,end=' ')
    else:
        continue

print("-"*50)

#####################################################################
##If else program to assign grades as per total marks.
""""
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks

"""

marks= int(input("Enter the marks"))
if marks<40:
    print("Fail")
elif marks> 40 and marks<50:
    print("Grade C")
elif marks>50 and marks<60:
    print("Grade B")
elif marks>60 and marks<70:
    print("Grade A")
elif marks>70 and marks<80:
    print("Grade A+")
elif marks>80 and marks<90:
    print("Grade A++")
elif marks>90 and marks<100:
    print("Grade Excellent")
else:
    print("Invalid")

print("-"*50)

#####################################################################
##Python program to check the given number divided by 3 and 5.

num= int(input("Enter the number"))
if num%3==0 and num%5==0:
    print("The given number is divided by 3:",num)
else:
    print("The given number is not divided by 3:",num)

print("-"*50)
######################################################################
# write a program to print the square of the number
num= int(input("Enter the number"))
if num%11==0:
    print(num**2)
else:
    print("The given number is not divided by 11:",num)

print("-"*50)

#########################################################################
## Write a program to check given number is odd or even.
num= int(input("Enter the number"))
if num%2==0:
    print("The number is Even")
else:
    print("The number is odd")

print("-"*50)

#########################################################################
##Write a rogram to check a given number is part of the Fibonacci series from 1 to 10

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Take input through the user
num = int(input("Enter a Fibonacci series number: "))
# Check for number in fibonacci series
if num in fib:
    # Print output
    print("It is a part of the Fibonacci series :", num)
else:
   # Print output
    print("It is not a part of the Fibonacci series :", num)

print("-"*50)

####################################################################
##Write a program to check authentication with the given username and password.(Check with Deepesh)
num = str(input("Enter the Username: "))
num1= int(input("Enter the password: "))
username= 'Rohit'
password= 1234
if num==username and num1==password:
    print("Given username and password is authenticated successfully")
else:
    print("Invalid username and password")

print("-"*50)

##################################################################################
##write a program to validate user_id in the list of user_ids.
id_list = [11,22,23,45,67]
id = int(input("Enter the id"))
if id in id_list:
    print("Id is valid")
else:
    print("Id is not valid")

print("-"*50)
###################################################################################
##write a program to print a square or cube if the given number is divided by 2 or 3
num = int(input("Enter a number: "))
if num%2 == 0:
    print("Sqaure: ", num ** 2)
elif num % 3 == 0:
     print("Cude:",num**3)

print("-"*50)
###################################################################################
##write a program to determine whether a given number is available in the list of numbers or not.
list = [22,34,66,109,222]
num = int(input("Enter a number: "))
if num in list:
    print("Given number is available in list")
else:
    print("Given number is not avaliable in list")

print("-"*50)
#############################################################################
##Write program to check any person eligible to vote or not
""""
age > 18+ : eligible
age < 18: not eligible
"""
num = int(input("Enter a person age:  "))
if num > 18:
    print("Person is eligible to Vote")
else:
    print("PErson is not eligible to Vote")

print("-"*50)
#################################################################################
##program to check whether a student has passed the exam.
# If marks are greater than 35 students have passed the exam.

marks = int(input("Enter student marks: "))
if marks >=35:
    print("Student is passed the exam")
else:
    print("Student is failed in exam")

print("-"*50)
#################################################################################
##Write a program to check whether the given number is positive or not.
num = int(input("Enter the number: "))
if  num>0 or num>-1:
    print("Given number is positive")
else:
    print("Given number is negative")

print("-" * 50)
#################################################################################
##Write a program to print the largest number from two numbers.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a>b:
    print("A is largest number")
elif b>a:
    print("B is largest number")

print("-"*50)
################################################################################
## Write a program to check whether a given character is uppercase or not.
num = str(input("Enter the character: "))
if num.isupper():
    print("Given character is Uppercase")
else:
    print("Given character is lowercase")

print("-"*50)
################################################################################
## Write a program to check whether the given character is lowercase or not.
num = str(input ("Enter the Character: "))
if num.islower():
    print("Give character is lowercase")
else:
    print("Given character is not lowercase")

print("-"*50)
################################################################################
## Write a program to check whether the given number is an integer or not.
num = int(input("Enter the number: "))
if num%2==0:
    print("Given number is Integer")
elif num%2!=0:
    print("Given number is not Integer")

print("_"*50)
################################################################################
##Write a program to check whether the given number is float or not
num = float(input("Enter the float number: "))
print(num)
if num.__float__():
    print("Given number is float")
elif num == 0.0:
    print("Given number is not float")


