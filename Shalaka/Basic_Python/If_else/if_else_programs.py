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

print('20). Python program to check whether the given number is negative or not.')
num8 = int(input('Enter your number'))

if num8<0:
    print ('Number is negative ')
else:
    print('Number is positive')
"""
"""
print('21). Python program to check whether the given number is positive or negative and even or odd.')

num9 = int(input('Enter your number'))

if num9 % 2 == 0 and num9 > 0:
    print('The given number is positive and even')
else:
    print('The given number is negative and odd')

"""
"""
print('22). Python program to print the largest number from two numbers.')

num10 = int(input('Enter your number: '))
num11 = int(input('Enter your number: '))

if num10 >num11:
    print('largest number : ', num10 )
else:
    print('largest number', num11)


"""
"""

print('23). Python program to check whether a given character is uppercase or not.')

char = input('Enter character : ')

if char.isupper():
    print ('The given character is an Uppercase')
else:
    print('The given character is not an Uppercase')

"""
"""
print('24). Python program to check whether the given character is lowercase or not.')

char = input('Enter character : ')

if char.islower():
    print('True')
else:
    print('False')

"""
"""
print('25). Python program to check whether the given number is an integer or not.')
num13 = input('Enter your number :')

if type(num13) == int:
    print('True')
else:
    print('False')

"""
"""

print('26). Python program to check whether the given number is float or not.')
num14 = 12.8

if type(num14) == float:
    print('True')
else:
    print('False')

"""
"""
print('27). Python program to check whether the given input is a string or not.')
str1 = 'sqatools'

if type(str1) == str:
    print('True')
else:
    print('False')

"""
"""

print('28). Python program to print all the numbers from 10-15 except 13')

for i in range (10,16):
     if i!= 13:
         print(i)
"""
"""
'''29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill'''
unit = int (input('Enter your unit'))
bill =0
if unit > 0 and unit <= 50:
    bill = bill*0.50
    print(bill)
elif unit > 50 and unit <=100:
    bill = bill*0.75
    print(bill)
elif unit >100 and unit <= 250:
    bill = bill*1.25
    print(bill)
elif unit <= 250:
    bill = bill* 1.50
    print(bill)

total_bill = bill *(17/100)
print(total_bill)  # output is not right.
"""
"""
print("30). Python program to check whether a given year is a leap or not.")
year =int(input("Enter your year"))

if (year%4==0) or (year%4==0 and year%100!=0):
    print("Year is leap year")
else:
    print("Year is not leap year")

"""
"""
print("31).Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.")

num31 = int(input("Enter your number"))

if num31%2==0 and (num31%3!=0):
    print("Fizz")
elif num31%3==0 and (num31%2!=0):
    print("Buzz")
elif (num31%2==0)and(num31%2==0):
    print("FizzBuzz")
else:
    print("Number is not multiply of 2 & 3 or both")
"""
"""
print("32). Python program to check whether an alphabet is a vowel.")

char = input("Enter character")
vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

if char in vowel:
    print("Alphabet is vowel")
else:
    print("Alphabet is not vowel")
"""
"""
print("33). Python program to check whether an alphabet is a consonant.")
char = input("Enter character")
vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

if char not in vowel:
    print("Alphabet is consonant")
else:
    print("Alphabet is not consonant")
"""
"""
print("34). Python program to convert the month name to the number of days.")
month = input("Enter month name: ")

if month in ("january", "march", "may", "july", "august", "october", "december"):
    print("31 days")
elif month in ("april", "june", "september", "november"):
    print("30 days")
elif month == "february":
    print("28 or 29 days")
else:
    print("Invalid month name")
"""
"""
print("35). Python program to check whether a triangle is equilateral or not. An equilateral triangle is a triangle in which all three sides are equal.")
a = int(input("first side"))
b = int(input("second side"))
c = int(input("third side"))

if a == b == c:
    print("triangle is equilateral")
else:
    print("triangle is not equilateral")
"""
"""
print("36). Python program to check whether a triangle is scalene or not. A scalene triangle is a triangle that has three unequal sides.")
a = int(input("first side"))
b = int(input("second side"))
c = int(input("third side"))

if a != b != c:
    print("triangle is scalene")
else:
    print("triangle is not scalene")
"""
"""
print("37). Python program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides.")
a = int(input("first side"))
b = int(input("second side"))
c = int(input("third side"))

if (a == b != c) or (a != b == c):
    print("triangle is isosceles")
else:
    print("triangle is not isosceles")
"""
"""
print ("38). Python program that reads month and returns season for that month.")
month = input("Enter your month")
if month in ("February", "March", "April", "May"):
    print("Summer")
elif month in ("June", "July", "August", "September"):
    print("Rainy")
elif month in ("October", "November", "December", "January"):
    print("Winter")
else:
     pass
"""
list1 = [4, 5, 90, 34, 23, 30, 78]
even = []
for val in list1:
    if val % 2 == 0:
        even.append(val)
    else:
        pass
print(list1)
print(even)
