#14th Oct Class
#when there are some comapriosns to be done, some condition ti be defined - if ,else, elif
#cntrl + Alt +i -> for code identation
a = 10
b = 20

print("a is equal to b?", a == b)  #False

if a == b: # "==" called comapriosn operator, "=" - called assignment operator
    print("Both values are equal")
else:
    print("At least one value is not equal")  #At least one value is not equal

#################################################################################
#write a program to check if given number is even or odd
#if a number is divisble by 2 its even else its odd
#2,4,6,8,10...

num1 = 12
if num1 % 2 == 0:
    print("num1 is even", num1)
else:
    print("num1 is odd",num1)  #num1 is even

####################################################################################
#multiple conditions
#if -elif - else condition
"""
if cond1:
    print("cond1 is true")
elif:
    print("cond1 is false")
elif cond2:
    print("cond2 is true")
else:
    print("none of conditions are true")
"""
#e.x delivery guy has a parcel wheer there are 5 houses, he goes to house 1, its not true
#go to house 2, not true, then goes to house 3 - not true
#go to house 4 - True, then skips the house5

#write a pyhon ppgram to check if given number is divisible by 3,5,7
num2 = 13
if num2 % 3 == 0:
    print("num2 is divisible by 3 :", num2)
elif num2 % 5 == 0:
    print("num2 is divisible by 5 :", num2)
elif num2 % 7 == 0:
    print("num2 is divisible by 7 :", num2)
else:
    print("num2 is not divisible by any numbers :", num2)
#if the 1st condition itselkf is true, it wont go to any other conditions further

##########################################################################################
#Nested - If condition
#main Door, Kitchen door and Fridge door
#if main door open - ythen only open kictehn door and then open the fridge door
#if main door not opened then kicthen door cant be opened and fridge door
#so one condition is depenent on other condition
#interview - if 1st riund cleared - then go to next round and then again 3rd round dependent on 2nd round

"""
if cond1:
    code1
    if cond2:
        code2
        if cond3:
            code3
        else:
            code4
    else:
        code5
else:
    code6
"""
#write a python program with nested if condition and provide solution for interview process
round1 = "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("Congragulations! Round1 is passed")
    if round2 == "pass":
       print("Congragulations! Round2 is passed")
       if round3 == "pass":
           print("Congragulations! Round3 is passed")
       else:
           print("sorry! Failed in Round3,try next time")
    else:
        print("Sorry! Failed in round 2, try next time")
else:
    print("Sorry ! Failed in 1st round, try next time")

#When values are -
# round1 = "pass"
#round2 = "fail"
#round3 = "pass"
#Sorry ! Failed in 1st round, try next time
# even though second and third round is pass - since 1st round has failed, it wont go to condition 2 and 3

# round1 = "pass"
#round2 = "fail"
#round3 = "pass"
#Congragulations! Round1 is passed
#Sorry! Failed in round 2, try next time


#round1 = "pass"
#round2 = "pass"
#round3 = "fail"
#Congragulations! Round1 is passed
#Congragulations! Round2 is passed
#sorry! Failed in Round3,try next time

#########################################################################################
#one-line - If statement
#to check if a number is odd or even
result = 20
result = "even" if result % 2 == 0 else "odd"
print("result value is", result) #result value is even

#################################################################################
