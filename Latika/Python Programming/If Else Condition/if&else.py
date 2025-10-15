# If Conditional Programs

a=10
b=10
print(a==b)
if a==b:
    print("Both Values are equal")
else:
    print("Both values are not equal")
###########################################################################################################
print("."*100)
print()
print("Even-Odd Program")
num1=4
if num1 % 2 == 0:
    print("It is even no",num1)
else:
    print("It is odd no",num1)

###########################################################################################################
print("."*100)
print()
print("ELIF Programs")
print("Write a program to check given no is divisible by 3,5 and 7")
x=12
if x%3==0:
    print(x,"No is divisible by 3")
elif x%5==0:
    print(x,"No is divisible by 5")
elif x%7==0:
    print(x,"No is divisible by 7")
else:
    print("No is not divisible by 3,5 and 7")

###########################################################################################################
print("."*100)
print()
print("Nested IF and Else Condition")
print("Write a program with nested if condition and provide a solution for interview process")

r1 = "Pass"
r2 = "Fail"
r3 = "Pass"

if r1 == "Pass":
    print("1st round is cleared")
    if r2 == "Pass":
        print("2nd round is cleared")
        if r3 == "Pass":
            print("Congrats !! You are selected")
        else:
            print("Sorry !! You are failed in 3rd round, try next time")
    else:
        print("Failed 2nd round")
else:
    print("Failed 1st round")
########################################################################################################################
print("."*100)

marks1=60
marks2=75
marks3=35
marks4=30

if marks1==60:
    print("Congrats, you received 60%")

    if marks2==75:
        print("Congrats, you received 75% distinction")

        if marks3==35:
            print("You are just pass, need to improve")

            if marks4==30:
                print("Sorry dude, you are fail")
            else:
                print("You Pass the subject")

        else:
            print("Failed in 3rd subject")
    else:
        print("Failed in 2nd subject")
else:
    print("Failed in 1st subject")
