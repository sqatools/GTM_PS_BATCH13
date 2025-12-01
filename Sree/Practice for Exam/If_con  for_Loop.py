"""
 1.If else program to assign grades as per total marks.marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks

print('1.','_'*30)
marks=int(input("Enter marks"))
if marks >=90 and marks <=100:
    print("Excellent grade")
elif marks >=80 and marks <=90:
    print("grade A++")
elif marks >=70 and marks <=80:
    print("grade A+")
elif marks >=60 and marks <=70:
    print("grade A")
elif marks >=50 and marks <=60:
    print("grade B")
else:
    print("invalid marks")
print('2.','_'*30)
d mathematical operations from users and perform mathematical operations
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operation = input("Enter operation of your choice")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "/":
    print(num1/num2)
elif operation == "*":
    print(num1*num2)
else:
    print("Invalid operation")
"""
"""
Python program to check the given number divided by 3 and 5.

Number=int(input("enter the number"))
if Number %3==0 or Number%5==0:
#if Number%3 ==0 and Number%5==0:
    print('divided by 3 or 5',)
else:
    print("not divided by 3 or 5")
"""
print('3.','_'*30)
"""
Python program to print the square of the number if it is divided by 11

a=11
if a%11==0:
    print(44**2)
num=int(input("enter the number to give square of it"))
if num%11==0:
    print(num**2)
else:
    print("invalid")
print('4.','_'*30)
"""
"""
Python program to check given number is a prime number or not

num=20
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False  # if num is divisible "not prime"
        break
    else:
        continue
if prime==True:
    print('prime number')
else:
    print('not')

print('5.','_'*30)
num=int(input("enter a number"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
    else:
        continue
if prime==True:
    print("Prime")
else:
    print('not')

print('6.','_'*30)
"""
#given number is odd or even.
"""
num=int(input("Enter a numbe"))
if num%2==0:
    print("Even number")
else:
    print("odd")
for i in range(1,101):
    if i%2!=0:
        print(i)

print('7.','_'*30)
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num=int(input('enter a number'))
if num in fib:
    print('fib')
else:
    print('not fib')
"""
#authentication of username and password
"""
print('8.','_'*30)
Name=input("Enter name")
password=input("Enter pass")
if Name=="admin"and password=="1234":
    print('valid login')
else:
    print("not valid")

Num=int(input('enter a nuber for 2 and 3'))
for i in range(1,Num):
    if i%2==0:
        print(i**2)
    elif i%3==0:
        print(i**3)
    else:
        print(i,'not divisibe by 2 or 3')

#interview process
print('-'*30)
round1=input('Enter round 1 results')
round2=input('enter round2 results')
if round1 == "passed":
    print('congratues pass 1')
    if round2=="passed":
        print('congrates you passed round 2')
    else:
        print('failed in roud 2')
else:
    print('failed in round 1')

while True:
    round1 = input('Enter round 1 results: ')
    round2 = input('Enter round 2 results: ')

    if round1 != "passed":
        print("failed in round 1")
        break   # stop everything if round1 failed

    print("congrats, you passed round 1")

    if round2 == "passed":
        print("congrats, you passed round 2")
    else:
        print("failed in round 2")
        break

# given number is available in the list of numbers or not.
list=[1,6,8,9,33,55,22]
i=int(input('enter a number'))
if i in list:
    print(i,'it is in the list')
else:
    print(i,'not in the list')

#person eligible to vote or not
num=int(input("enter age"))
if num>=18:
    print(num,'eligible for vote')
else:
    print(num,"not")

#largest number among three numbers.
a=100
b=200
c=300
if a>b and a>c:
    print(a,'a has larger value')
if b>a and b>c:
    print(b,'b has larger value')
if c>a and c>b:
    print(c,'c has larger value')
num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if num1>num2 and num1>num3:
    print(num1,"num1 has larger")
if num2>num1 and num2>num3:
    print(num2,"num1 has larger")
if num3>num1 and num3>num2:
    print(num3,"num1 has larger")
#####################################
num1 = 121
num2 = str(num1)

if num1 == int(num2[::-1]):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
###########################################
num = int(input("Enter a number: "))

if num<0:
    print("True")
else:
    print("False")

########################### is upper###########
char=input("give a character")
if char.isupper():
    print('it is a uppercase')
else:
    print('Not')
"""
#################    If LOOP  #############################
"""
*
**
***
****
*****
starts from 6
"""
for i in range(6):
    print(i*"*")
################################
"""
******   starts with 6 & ends with 0 
*****
****
***
**
*
"""
for i in range(6,0,-1):
    print(i*"*")
print()
###########################################
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
Valueofi range(i) j values	How many times printed?
1	range(1)	0	            1 time
2	range(2)	0, 1	        2 times
3	range(3)	0, 1, 2	        3 times
4	range(4)	0, 1, 2, 3	    4 times
5	range(5)	0, 1, 2, 3, 4	5 times

for i in range(1,6):
        for j in range(i):
            print(i, end=" ")
        print()
print('-'*33)
for i in range (1,6):
    for j in range(i):
        print('*',end="")
    print()
###############################
"""
"""The outer loop value i sets the maximum count for inner loop. here 1,6 =1,2,3,4,5
for j in range(i) means:
When i = 1 → range(1) → j = 0
When i = 2 → range(2) → j = 0, 1
When i = 3 → range(3) → j = 0, 1, 2
When i = 4 → range(4) → j = 0, 1, 2, 3
When i = 5 → range(5) → j = 0, 1, 2, 3, 4  
"""
"""
print('-'*30)
for i in range(1,6):
        for j in range(i):
            print(j, end=" ")
        print()
#############################################
print("10",'-'*30)
for i in range(6,0,-1):
    for j in range(i):
        print('*',end="")
    print()
******
*****
****
***
**
*
print('11','_'*30)
###################################
for i in range(6):
    print(i*'*')
for i in range(6,0,-1):
    print(i*"*")
*
**
***
****
*****
******
*****
****
***
**
*
"""
"""
for i in range(1,6):
        for j in range(i):
            print(i, end=" ")
        print()
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 
"""
for i in range(1,101):
    if i%5==0:
        print(i,'',end="")
print()
###########################################
# pyramid

v1=3
v2=5

for i in range(5):
    for j in range(9):

        if j > v1 and j < v2:     # means 4
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

    v1 = v1 - 1
    v2 = v2 + 1
"""
for i in range(5):
This repeats 5 rows.
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
for j in range(9):
Each row prints 9 positions (0 to 8).
"""
v1 = 3
v2 = 5

for i in range(5):
    for j in range(9):

        if j > v1 and j < v2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    v1 = v1 - 1
    v2 = v2 + 1
# total number of even numbers in 1-100
count=0
for i in range(1,101):
    if i%2==0:
        print(i)
        count +=i
print('Total even numbers ',count)
# 5 table ##################
for i in range(1,10):
    print('5 x',i,'=',5*i)
###########  every character on the new line.
str1 = "Sqatools"

for char in str1:
    print(char,end="\n")
#######   sum of all odd numbers between 1-100
count=0
for i in range(1,101):
    if i%2!=0:
        print(i)
        count +=i   # instead of 1 ,here used i , since we want output of 2500
print('Total sum of odd numbers:',count)
####  first 20 natural numbers using a while loop.     ####
count = 1

while count < 21:
    print(count,end=" ")
    count += 1
print('_'*30)
#########   sum of natural numbers
count = 1
total =0

while count<11:
    total +=count
    count += 1

print("Total: ",total)
## Print numbers from 1-10 except 5,6 using a while loop in Python.
for i in range(1,10):
    if i !=5 and i !=6:
        print(i)
####  days in a week except Sunday using a while loop in Python.
days='monday','tuesday',"wed",'thur','fri','sat','sun'
for i in days:
    if i!='sun':
        print(i)

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

#############################################
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


