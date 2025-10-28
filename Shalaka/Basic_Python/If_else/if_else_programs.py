"""""
print('1). Python program to check given number is divided by 3 or not.')
var = input('Enter your number')

num1 = int(var)
print ('num', type(num1))

if num1%3==0:
    print('Number is divided by 3 :', num1)
else :
    print('Number is not divied  by 3 :', num1)


print('2). If else program to get all the numbers divided by 3 from 1 to 30.')
for i in range(1,30):
    if i%3 ==0:
        print ('number is divied by 3:',i)
    else:
        pass
"""
"""
print('3). If else program to assign grades as per total marks.')
marks = int (input('Enter your marks: '))

if marks < 40:
    print('Fail')
elif marks >50 and marks<=60:
    print('grade C')
elif marks >50 and marks<=60:
    print('grade B')
elif marks >61 and marks<=70:
    print('grade A')
elif marks >71 and marks<=80:
    print('grade A+')
elif marks >81 and marks<=90:
    print('grade A++')
elif marks >91 and marks<=100:
    print('grade Excellent ')
elif marks > 100:
 print('Invalid marks')


print('4). Python program to check the given number divided by 3 and 5.')

x = int(input('your number :'))

if x %3 ==0 and x %5==0:
    print('No is div by 3 & 5 :', x)
else :
    print('No is not div by 3 & 5 ')


print('5). Python program to print the square of the number if it is divided by 11.')

x = int(input('your number :'))
if x%11==0:
    b=x**2
    print(b)
else:
   print ('fail')


print('6). Python program to check given number is a prime number or not.')
a = int(input('Enter your no : '))

for i in range (2,a):
    if a %i ==0:
        print ('No is not prime', a)
        break
else:
    print('No is prime', a)


print('7). Python program to check given number is odd or even.')
a = int(input('Enter your no : '))

for i in range(2,a):
    if a %i==0:
        print('No is even', a)
        break
    else:
        print ('No is  odd', a)


print('8). Python program to check a given number is part of the Fibonacci series from 1 to 10.')

print('9). Python program to check authentication with the given username and password.')

username ='shalakab2330'
password = 'Shalaka@123'
user = input('Enter Username')
pswd = input('Enter password')


if user == username and password ==pswd:
    print ('Valid user')
else:
    print('Invalid user')


print('10). Python program to validate user_id in the list of user_ids.')
user_id = ['Shalaka', 'John','Hello']

user= input('Enter username')
if user in user_id:
    print('Valid user')
else:
    print('Invalid user')

print('11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.')
y= int(input ('Enter number'))

if y%2==0:
    print('Square: ', y**2)
elif y%3==0:
    print('Cube: ', y**3)

else:
    print('Invalid number')

print('12). Python program to describe the interview process.')




print('13). Python program to determine whether a given number is available in the list of numbers or not.')
list1 = [1,3,6,8,0]
num2 =int(input('Enter your number'))

if num2 in list1:
    print('Number is in list')
else:
    print('Number is not in list')


print('14). Python program to find the largest number among three numbers.')

num3 = int(input('Enter your 3rd number'))
num4 = int(input('Enter your 4th number'))
num5 = int(input('Enter your 5th number'))
if num3 > num4 and num3>num5:
    print("num 3 is largest", num3)
elif num4 > num5 and num4>num5:
    print("num 4 is largest", num4)
elif num5 > num3 and num5>num4:
    print("num 5 is largest", num5)
else:
    print('Invalid number')

print('15). Python program to check any person eligible to vote or not')
age = int(input('Enter your age'))

if age >=18:
    print ('eligible for vote')
else:
    print ('Not eligible for vote')

print('16). Python program to check whether any given number is a palindrome.')
a1 = int(input('Enter your no'))
a2 = str(a1)
if a1 == int(a2[::-1]):
    print('Given number is a palindrome')
else:
    print('Given number is not a palindrome')


print('17). Python program to check if any given string is palindrome or not.')
str1 = input('Enter your string ')
str2 = str(str1)
if str1 == str2[::-1]:
    print('Given string is a palindrome')
else:
    print('Given string is not a palindrome')

print('18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.')
marks = int(input('Enter your marks'))

if marks>=35:
    print('Pass')
else:
    print('Fail')


print('19). Python program to check whether the given number is positive or not.')
num7 = int(input('Enter your number'))

if num7>=0:
    print ('Number is positive')
else:
    print('Number is negative')
"""
print('20). Python program to check whether the given number is negative or not.')
num8 = int(input('Enter your number'))

if num8<0:
    print ('Number is negative ')
else:
    print('Number is positive')









