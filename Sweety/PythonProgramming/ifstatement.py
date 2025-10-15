a = 10
b = 20
if a == b:
    print("Both numbers are equal", a, b)
else:
    print("Both numbers are not equal", a, b)


print("_"*100)
###################################################
# write a program to check given number is even or not

num = 13
if num%2 == 0:
    print(num, "is even number")
else:
    print(num, "is odd number")

print("_" * 100)
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
############################################
# write a python program to check given number is divisible 3, 5, 7

a = 19

if a%3 == 0:
    print(a, "is divisible by 3")
elif a%5 ==0:
    print(a, "is divisible by 5")
elif a%7 == 0:
    print(a, "is divisible by 7")
else:
    print(a, "is not divisible by any given number")

print("_"*100)
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
# write a python program with nested if condition and provide solution for interview process.
round1 = "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("congratulations 1st round is clear")
    if round2 == "pass":
        print("congratulations 2nd round is clear")
        if round3 =="pass":
            print("congratulations 3rd round is clear")
        else:
            print("failed in 3rd round, try next time")
    else:
        print("failed in 2nd round, try next time")
else:
    print("failed in 1st round, try next time")

print("_"*100)
################################################
# one line if statement

var = 20
result = "even" if var%2 == 0 else "odd"
print("result is:", result)

print("_"*100)
#####################################################
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
a = 10
b = 20
c = 30
if a > b and a > c:
    print("a is grater than b and c")
elif b > a and b > c:
    print("b is grater than a and c")
elif c > a and c > b:
    print("c is grater than a and b")
else:
    print("no one has greater value")


print("_"*100)
######################################################
# write a program to check given number is divisible by 3 and 5
num = int(input("Enter a number: "))
print(num, type(num))
# input function takes value in string format, we have to convert in required format
if num % 3 == 0 and num % 5 == 0:
    print(num, " :is divisible by 3 and 5")
else:
    print(num, " :is not divisible by 3 and 5")

# write a program to check given number is divisible by 3 or 5
num1 = input("Enter a number: ")
print(num1, type(num1))
var = int(num1)
print(var, type(var))

if var % 3 == 0 or var % 5 == 0:
    print(num, " :is divisible by 3 or 5")
else:
    print(num, " :is not divisible by 3 or 5")

print("_"*100)
########################################################
# use of in operator:
list1 = [1, 4, 6, 8, 9, 2]
n = 2
if n in list1:
    print("n is available in the list1")
else:
    print("n is not available in the list1")

# use of not in operator:
list2 = [1, 4, 6, 8, 9, 2]
n2 = 5
if n2 not in list2:
    print("n2 is available in the list2")
else:
    print("n2 is not available in the list2")






