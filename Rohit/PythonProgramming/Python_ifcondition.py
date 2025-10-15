a= 10
b=2
print(a==b)
if a==b:
    print("Both values are equal")
else:
    print("Both valuea are not equal")

print("-"*50)

###############################################
# Write a program to check given number is even or odd

num1 = 10
if num1%2== 0:
    print("This is an even number:", num1)
else:
    print("This is an odd number:",num1)

print("-"*50)

num2 = 11
if num2 % 2 == 0:
    print("This is an even number:", num2)
else:
    print("This is an odd number:", num2)

print("-"*50)

############################################################
# Write program to check given number is divisible with 3,5,7

x= 14
if x%3==0:
    print("This is divisible by 3:",x)
elif x%5==0:
    print("This is divisible by 5:",x)
elif x%7==0:
    print("This is divisible by 7:",x)
else:
    print("This is not divisible by any number")

print("-"*50)

x= 11
if x%3==0:
    print("This is divisible by 3:",x)
elif x%5==0:
    print("This is divisible by 5:",x)
elif x%7==0:
    print("This is divisible by 7:",x)
else:
    print("This is not divisible by any number")

    print("-"*50)
 #######################################################################
 # write a program one line if statement
val1= 21

result= "even" if val1%2==0 else "odd"
print("result:",result)
print("-"*50)

val1= 14

result= "even" if val1%2==0 else "odd"
print("result:",result)

print("-"*50)
##############################################################################
#Write a python program with nested if condition and provide solution for interview process
round1="Pass"
round2="Pass"
round3="Pass"

if round1=="Pass":
    print("You have clear 1st round of interview")
    if round2=="Pass":
        print("You have clear 2nd round of interview")
        if round3=="Pass":
            print("You have clear 3rd round of interview")
        else:
            print("sorry you have failed to fail for 3rd round")
    else:
        print("Sorry you have not clear 2nd round try next time")
else:
    print("sorry try next time")

print("-"*50)

round1="Pass"
round2="fail"
round3="Pass"

if round1=="Pass":
    print("You have clear 1st round of interview")
    if round2=="Pass":
        print("You have clear 2nd round of interview")
        if round3=="Pass":
            print("You have clear 3rd round of interview")
        else:
            print("sorry you have failed to fail for 3rd round")
    else:
        print("Sorry you have not clear 2nd round try next time")
else:
    print("sorry try next time")

print("-"*50)

round1="Pass"
round2="Pass"
round3="Fail"

if round1=="Pass":
    print("You have clear 1st round of interview")
    if round2=="Pass":
        print("You have clear 2nd round of interview")
        if round3=="Pass":
            print("You have clear 3rd round of interview")
        else:
            print("sorry you have failed for 3rd round")
    else:
        print("Sorry you have not clear 2nd round try next time")
else:
    print("sorry try next time")

print("-"*50)

#############################################################################