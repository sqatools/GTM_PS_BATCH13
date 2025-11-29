from Deepesh.PythonProgramming.PythonString.string_prog_practice import vowels
from Shalaka.Basic_Python.String.String_Programs import count

print("Hello World this is my first python program")
print("I have started my python class from 9th of Oct")

result = []
for i in range(1, 21):
    if i % 2 == 0:
        result.append(i)
        print(result)
print("-"*50)

A = [2,3,5,7,9,10]
for i in A:
    if i%2==0:
        print(i)
print("-"*50)
a= 100
b= 200
c= a+b
print(c)

print("sub :",a/b)

print("-"*50)
x,y,z=15,33,42

list1 = ['x','y','z']
list2 =15,33,42
result = dict(zip(list1,list2))
print(result)

list1= [2,4,7,5,8,9,12]
for val in list1:
    if val%2==0:
        print("even number :", val)
    else:
        print("odd number :",val)

list1= [2,4,5,7]
list2 = [3,4,8,9]
list2.extend(list1)
print(list2)

print("-"*50)
#########################################
a = 10
b = 20

a,b = b,a

print(a,b)

print("-"*50)
#############################################
nums = [1,2,3,4]

print(len(nums))

print("-"*50)
###############################################

for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")

print("-"*50)

############################################
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opt = input("Enter the operation (+, -, *, /) : ")

if opt == "+":
    print(num1 + num2)
elif opt == "-":
    print(num1 - num2)
elif opt == "*":
    print(num1 * num2)
elif opt == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

print("-"*50)
######################################
num3 = int(input("Enter the number :"))

for i in range(1,num3):
    if i <=1 and num3 % i == 0:
        print("Prime number")
    else:
        print("Not prime number")

print("-"*50)
#####################################
#•	Takes n integers as input from the user and stores them in a list.
#	From this list, creates another list containing only the even numbers.
#	Prints both the original list and the even-number list.

n = int(input("Enter the number :"))
even = []
for i in range(n):
    if i % 2 == 0:
     even.append(i)

print("Even number :", even)
print("original list :", i)

print("-"*50)
#############################
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
a = input("Enter the vowels :")

for i in a:
    if i in vowels:
        count +=1
    print("Total vowels :", count)