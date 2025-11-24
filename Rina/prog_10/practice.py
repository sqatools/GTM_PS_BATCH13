"""
numa = 50
numb = 60
print("addition : ", numa + numb)
print("subtraction : ", numa - numb)
print("multiplication :", numa*numb)

str1 = "SQATools"
n1 = 6
print("result :", str1*n1)

a = 40
b = 50
c = 30
print("Avg : ", (a + b + c)/3)

values = [10, 20, 30, 40, 50, 60]
values.sort()
n = len(values)

if n % 2 == 1:
    median_value = values[n // 2]
else:
    median_value = (values[n // 2 - 1] + values[n // 2]) / 2

print(f"The median is: {median_value}")

import math
num1 = 169
print(math.sqrt(num1))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

while(True):
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1

print(f"L.C.M of {num1} and {num2}: {lcm}")


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
if num1 > num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller+1):
    if((num1 % i == 0) and (num2 % i ==0)):
        hcf = i
print(f"H.C.F of {num1} and {num2}: {hcf}")

num = int(input("Enter a number up to which you want to find sum: "))
total = 0
for i in range(1,num+1):
    total += 1
print("Total : ", total)

num = int(input("Enter a number up to which you want to find sum: "))
total = 0

for i in range(1,num+1):
    total += i

print("Total: ",total)

num = int(input("Enter a number: "))
print(f"Binary form of {num} is: ","{0:b}".format(int(num)))

import datetime
dt = datetime.datetime.now()
print("Current date: ", dt)

"""



