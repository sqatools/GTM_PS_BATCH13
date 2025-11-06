#15th Oct -Class
"""
Logical Operator - 2 operators - AND and OR
If we have to compare 2 conditions at a time

Logical AND Operator(2 keys to the door, only when both are opened - door will open)
False and True - False
False and False - False
True and True - True
True and False - False

Logical OR Operator(1 main door key and other is the back door key)
False OR True - True
True OR False - True
True and True - True
False and False - False

Conditional Operators
> : - Greater than
>= : - Greater than or equal to
<= : - Less than or equal to
< : Less than
== : - Equal to
!= : - Not equal to
"""

#write a program to compare three values which is greater

a = 50
b = 60
c = 70

if a > b and a > c:
    print("a has greater value : ", a)
elif b > a and b > c:
    print("b has greater value : ", b)
elif c > a and c > b:
    print("c has greater value : ", c)
else:
    print("Sorry! None of the numbers have greater value")

#########################################################################################
#write a program to check if a number is divisible by 3 or 5
#num3 = 3

#take input from the user
num3 = input("Enter the number : ") #here input always take in string format not int format, e.g 12 will be taken as "12"
#input function takes value in string format, we have to convert to required format
print(type(num3))  # <class 'str'>
num4 = int(num3)  #here whatever we enter earlier from input, it will take as a string, to convert to number - add int
print("converted type is : ", type(num4))

#here until its a string, we camt do any mathemetical operation and check teh conditions
if num4 % 3 ==0 and num4 % 5 == 0:
    print("num4 is divisible by 3 and 5:", num4)
elif num4 % 3 == 0 or num4 % 5 == 0:
    print("num4 is divisible by 3 or 5:", num4)
else:
    print("num4 is not divisible by 3 or 5:", num4)

###################################################################################################################
#use of "in/not in" operator
lis1 = [5,7,9,10,3]
n1 = 7
#we need toc heck if n1 value is present in list1
if n1 in lis1:
    print("n1 is available in lis1")
else:
    print("n1 is not available in lis1")

str1 = "Hello Good Morning, we are learning Python"
val1 = "Java"
#to see if Java is not present in str1
if val1 not in str1:
    print("val1 is not in str1")
else:
    print("val1 is in str1")




