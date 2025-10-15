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

# write a python program with nested if condition and provide  solution for interview process.
round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats first round is cleared")
    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("Congratulations you are selected")
        else:
            print("Sorry you are not selected in round 3")
    else:
        print("Sorry you are not eligible for round 3")
else:
    print("Sorry you are not eligible for next round")

##################################################

