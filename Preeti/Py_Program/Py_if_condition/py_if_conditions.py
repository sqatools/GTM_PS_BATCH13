
################# if- else condition #############
a=10
b=20
if a==b:
    print("both are same")
else:
    print("both are not same")

#################Program for finding Even and Odd numbers#############
num=20
if num%2==0:
    print("this is Even number:",num)
else:
    print("this is Odd number:",num)

################ if - elif --- else ###############(Nested if condition)
### Wrint program for interview process#########
round1="pass"
round2="fail"
round3="pass"
if round1=="pass":
    print("congrats 1st round is cleared")

    if round2=="pass":
        print("congrats 2nd round is cleared")

        if round3=="pass":
            print("congrats you are selected")
        else:
            print("failed in 3rd round")
    else:
        print("failed in 2nd time")

else:
    print("sorry you are not cleared the interview")

# 1) Check if a number is positive or negative

num=int(input("Enter a number:"))
if num>0:
    print("number is positive:",num)
else:
    print("number is negative:",num)

# 2) Check if a number is Odd or Even
num=int(input("Enter a number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# 3) Check if a number is divisible by 5
num=int(input("Enter a number:"))
if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

# 4) Check if a number is divisible by both 3 and 5

num=int(input("Enter number:"))
if num%3==0 and num%5==0:
    print("number is divisible by both 3 and 5")
else:
    print("number is not divisible by 3 and 5")

# 5) Find the largest of two numbers
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a>b==0:
    print("A is largest number")
else:
    print("B is largest number")

# 6) Find the largest of three numbers
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>=b and a>=c:
    print("A is largest")
elif b>=a and b>=c:
    print("B is largest")
else:
    print("C is largest")

# 7) Check if a year is a leap year
year=int(input("Enter year:"))
if year%4==0 and year!=0:
    print("Leap year")
else:
    print("Not leap year")

# 8) Check if a number is within a range (1 to 100)
num=int(input("Enter a number:"))
if num>=1<=100:
    print("number is within a range 1 to 100")
else:
    print("number is not within a range 1 to 100")

# 9) Check eligibility to vote
age=int(input("Enter a age:"))
if age>=18==0:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

# 10) Check if a character is a vowel or consonant
ch=input("enter a character")
if ch.lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# 11) Check if a number is a multiple of 7
num=int(input("Enter a number:"))
if num%7==0:
    print("Number is a multiple of 7")
else:
    print("Number is a not multiple of 7")

# 12) Check if a person is eligible for driving license
age=int(input("Enter a age:"))
if age>=18==0:
    print("Eligible for driving license")
else:
    print("Not Eligible for driving license")

#################################################
print("_"*50)
# 13) Check if a number is positive, negative, or zero
num=int(input("Enter a number:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")

##################################################
print("_"*50)

# 14) Check if a triangle is valid based on sides
a=int(input("Enter side1:"))
b=int(input("Enter side2:"))
c=int(input("Enter side3:"))
if a+b>c and b+c>a and c+a>b:
    print("Trianglen is valid")
else:
    print("Triangle is invalid")
