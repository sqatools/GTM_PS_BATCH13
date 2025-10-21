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
"""

print('8). Python program to check a given number is part of the Fibonacci series from 1 to 10.')

