a = 10
b = 20

print(a == b)

if a == b:
    print("Both values are equal")
else:
    print("Both values are not equal")


print("_"*50)
###################################################
# write a program to check given number is even or not

num1 = 13
if num1%2 == 0:
    print("This is even number:", num1)
else:
    print("This is odd number:", num1)


##################################################
# if-elif-else condition
"""
if cond1:
     code
elif cond2:
     code
elif cond3:
     code
else:
     code

"""
print("_"*50)
############################################
# write a python program to check given number is divisible 3, 5, 7

x = 15

if x%3 == 0:
    print("This is divisible by 3:", x)
elif x%5 == 0:
    print("This is divisible by 5:", x)
elif x%7 == 0:
    print("This is divisible by 7:", x)
else:
    print("This is not divisible by any number:", x)


##############################################
# Nested If condition
"""
if  cond1:
    code
    if cond2:
        code
        if code3:
            code
        else:
            code
    else:
        code
else:
    code



"""
print("_"*50)
# write a python program with nested if condition and provide solution for interview process.

round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats first round is cleared")
    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("Congrats you are selected")
        else:
            print("Failed in 3rd round, try next time.")
    else:
        print("Failed iun 2nd, round try next time")
else:
    print("sorry failed in first round, try next time")


################################################
# one line if statement
var1 = 21

result = "even" if var1%2 == 0 else "odd"
print("result :", result)  # result : even


###########################################
#home work programs:
# 1. write a python program to check person is eligible to vote as per age.

###########################################
#home work programs:
# 1. write a python program to check person is eligible to vote as per age.

"""
Logical operator :
cond1  and cond2
True  and False : False
False and True  : False
False and False : False 
True and True :  True 

OR logical operator

True or False  :  True
False or True :  True
True or True :  True
False or False  :  False


> : greater than
< : less than
>= : greater than equal
<= : less than equal
== : equal 
!= :not equal

"""
print("_"*40)
# write a program to compare three values which is greater.

a = 80
b = 60
c = 70

if a > b and  a > c:
    print("A has greater value:", a)
elif b > a and b > c:
    print("B has greater value :", b)
elif c > a and c > b:
    print("C has greater value :", c)
else:
    print("No one has greater value")


###############################################
print("_"*40)
"""
# write a program to check given number is divisible by 3 and 5
var1 = input("Please enter your number :")
# input function takes value in string format, we have to convert in required format
print(var1,  type(var1))
num1 = int(var1)
print(num1,  type(num1))

if num1%3 == 0 and num1%5 == 0:
    print("This number is divisible by 3 and 5:", num1)
else:
    print("This number is not divisible by 3 and 5:", num1)


# '345'




num1 = int(input("Please enter your number :"))
# input function takes value in string format, we have to convert in required format

if num1%3 == 0 or num1%5 == 0:
    print("This number is divisible by 3 or 5:", num1)
else:
    print("This number is not divisible by 3 or 5:", num1)

"""

print("_"*50)
#######################################
# use of in operator:
list1 = [5, 7, 9 , 23, 56]
n1 = 9

if n1 in list1:
    print("n1 is available in the list1")
else:
    print("n1 is not available in the list1")

print("_"*50)
# NOT IN  operator

str1 = "Hello good morning we are learning Python"
val = "Python"

if val not in str1:
    print("val is not available in the string")
else:
    print("val is available in the string.")





#########
