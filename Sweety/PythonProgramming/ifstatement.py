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

