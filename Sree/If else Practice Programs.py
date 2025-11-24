# 1.check given number is divided by 3 or not
""" print("1.", "_" * 50)
a = 30
if a % 3 == 0:
    print("It is divisible  by 3 :", a)
else:
    print("It is not divisible by 3")

print("2.", "_" * 50)
    ########################################
num = 21
if num % 3 == 0:
    print("Number is divisible by 3:", num)
else:
    print("Number is not divisible by 3 :", num)

print("3.", "_" * 50)
##################
# 3. write a program to check given number is even or not

num1 = 57
if num1 % 2 == 0:
    print("This is even number:", num1)
else:
    print("This is odd number:", num1)
    print("4.", "_" * 50)
    ###########################################
    a = 20
    b = 10
    if a == b:
        print("both are equal")
    else:
        print("Both are not equal")
        print("5.", "_" * 50)  #####################################
        x = 28

        if x % 3 == 0:
            print("It is divisible by 3:", x)
        else:
            print("Not divisible by 3:", x)

print("6.", "_" * 50)  #####################################
a = 100

if a % 2 == 0:
    print("Even nuber:", a)

else:
    print("Not Even nuber:", a)
print("7.", "_" * 50)  #####################################

a = 20
if a > 100:
    print("Number is greater than 5: ", a)
else:
    print("Not greater than 5:", a)
print("8.", "_" * 50)  #####################################
# 8. if-elif-else statement
Marks = 20
if Marks >= 90:
    print("Grade A")
elif Marks >= 80:
    print("Grade B")
elif Marks >= 30:
    print("Grade C")
else:
    print("fail")

print("9.", "_" * 50)  #####################################

marks = 20

if marks > 90 and marks <= 100:
    print("grade Excellent")
elif marks > 80 and marks <= 90:
    print("grade A++")
elif marks > 70 and marks <= 80:
    print("grade A+")
elif marks > 60 and marks <= 70:
    print("grade A")
elif marks > 50 and marks <= 60:
    print("Grade B")
elif marks > 40 and marks <= 50:
    print("grade c")
elif marks < 40:
    print("Fail")
else:
    print("Invalid marks")

    print("10.", "_" * 50)  #####################################

    # check the given number divided by 3 and 5
a = 30

if a % 3 == 0 and a % 5 == 0:
    print("Divisible by 3 & 5:", a)
else:
    print("Not")

print("11." + "_" * 70)
#############################################################

a = 10

if a > 0:
    print("It is greater than 0")

    if a % 2 == 0:
        print("Divisible by 3")

        if a == 10:
            print("the numbers are equal")
        else:
            print("the numbers are not equal")
    else:
        print("Not divisible by 3")


else:
    print("It is not less than 0")

print("12."+"_" * 70)
    ###########################################
       #And Operators
age = 25

if age > 18 and age <=30:
    print("eligible to work")
else:
    print("not eligible to work")

print("_"*50)
#############################################
    #or Operators
Day = "Sunday"

if Day == "Saturday" or Day == "Sunday":
        print("Weekend")
else:
        print("Weekday")
print("_"*50)
    #############################################
    # Not Operators
is_raining= True

if not is_raining:
        print("You can go outside with out umbrella")
else:
        print("You should take umbrella")

print("_"*50)
########################################################
# Check if a number is positive or negative

a = 10

if a > 0:
    print("positive number")
elif a < 0:
    print("negative number")
else:
    print("The number is equal to Zero")

print("_"*50)
##############################################
# Check if a number is even or odd

a = 24

if a%2 ==0:
    print("Even number")
else:
    print("odd number")

b = 17
if b%2 == 0:
    print("Even number")
else:
    print("odd number")

print("_"*50)
#######################################
# Check if a number is divisible by 5

a = 100

if a%5 ==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

print("_"*50)
######################################
# Find the largest of two numbers

a = 50
b =100

if a > b:
     print(" a is larger")
else:
    print("b is larger")

print("_"*50)
############################################
# Find the largest of three numbers

a = 200
b = 400
c = 600

if a >= b and a <= c:
    print("a is largest")
elif b >= c and b <= c:
    print("b is largest")
else:
    print("c is largest")

print("_"*50)
#############################################
# Check eligibility to vote

age = 25

if age >=18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

print("_" * 50)
#############################################
# Check if a year is a leap year( divisible by 4, and Either not divisible by 100, or divisible by 400.

Year = 2025

#if Year%4 ==0 or Year%400 ==0:

if Year%4 ==0 and Year%100 != 0:
    print("Leap year")
else:
    print("Not a leap year")

print("_"*50)
#####################################
# Logical operators

a = 80
b = 30
c = 50

if a > b and a > c:
    print(" a has greater value")
elif b > a and b >c:
    print("b has greater value")
elif c > a and c >b:
    print("c has greater value")
else:
    print("No one has greater value")

print("_" * 50)
#####################################

num1 = int(input("please enter the number: "))

if num1%3 ==0 and num1%5 ==0:
    print("This number is divisible by 3 and 5")
else:
    print("This number is not divisible by 3 and 5:", num1)

print("_" * 50)
##########################################

num1 = int(input("please enter the number"))

if num1%3 ==0 or num1%5 ==0:
    print("This number is divisible by 3 or 5 :" , num1)
else:
    print("This number is not divisible by 3 or 5 :", num1)"""""

print("_"*50)
#########################      In operator  ##################
fruits = ["orange""apple""peach""berry"]

if "grape" in fruits:
    print("its in the list")
else:
    print("its not in list")
print("_"*50)
#######################################
Fruits = ["mango""blueberry"]

if "peach" not in Fruits:
    print("No peach in the list")
##########################################
print("_"*50)

Str = "I am taking python classes"

if "python" in Str:
    print("its in the given sentence")
else:
    print("Its not in the given sentence")
############################################
print("_"*50)

str = "I am taking java classes"

if "python" not in str:
    print("correct")
else:
    print("not correct")
#######################################
print("_"*50)
#Check if a number is within a range (1 to 100)

num1 = int(input("Enter number:"))

if num1 >=1 and num1 <= 100:
    print("with in range")
else:
    print("out of range")
##############################################
print("_"*50)
#Check eligibility to vote

age = num1

if age >=18:
    print("eligible to vote")
else:
    print("Not eligible")
########################################
print("_"*50)
#Check if a number is a multiple of 7

Mul = num1

if Mul%7 ==0:
    print("Multiple be 7")
else:
    print("not multiple by 7")
####################################
print("_"*50)
#Check if a person is eligible for driving license
age = num1

if age >=16:
    print("Eligible to get driving license")
else:
    print("Not eligible to get driving license ")
#########################################################
print("_"*50)
#Check if a number is positive, negative, or zero
Number = num1

if num1 > 0:
    print("Positive number")
elif num1 < 0:
    print("negative number")
else:
    print("Zero")
###################################
print("_"*50)
#
for i in range (1, 10, 1):
    print(i)
####################################
print("_"*50)

for i in range(2,10):
    print(i)
##############################
print("_"*50)

for J in range(10):
    print(J)
###############################
print("_"*50)

for k in range (1,10,2):
    print(k)
#############################
print("_"*50)

for p in range(10, 1,-2):
    print(p)
##################################################
print("_"*50)
#write a program to get sum of all the value from 1 to 10
sum = 0
for i in range(1,12): ## i = 1, 2, 3,
    sum = sum+i   #0+1 = 1 | 1 +2 = 3 | 3+ 3 = 6
print("total:", sum)



for i in range(1,6):
        for j in range(i):
            print(i, end=" ")
        print()





