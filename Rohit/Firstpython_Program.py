'''
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

print("-"*50)
##########################
with open ("2ndFiles.txt","r") as f:
    data = f.read()
    print(data)

print("-"*50)
########################
with open("2ndFiles.txt","w") as f:
    f.write("Python learning")

##########################################
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class seleniumbase:
    def __init__(self,driver):
        self.driver = driver

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
####################################################
s = "Madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

###########################
lst = [1, 2, 3, 2, 4, 1]

duplicate = [x for x in lst if lst.count(x)>1]
print(duplicate)
###############
a= 10
b =20

a,b = b,a
print(a,b)
##################333
lst = [10, 5, 20, 8]
max_no = lst[0]
for i in lst:
    if i > max_no:
        max_no = i
        print(i)

###########################
num1 = int(input("Enter the number"))
if num1%2==0:
    print("Even number")
else:
    print("Odd number")

######################
num2 = 7
if num2%7==0:
    print("Given number is prime")
else:
    print("Givem number is not prime")

########################3
for i in range(1,11):
    print(i)
#################################
for i in range(1,21):
    if i%2==0:
        print("Even numbers",i)
print("-"*50)
#########################33
for i in range(1,21):
    if i%2!=0:
        print("odd numbers",i)

print("-"*50)
#########################33
for i in range(10, 1, -1):
    print(i)
'''
list3 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']

print(list3[::1])
print(list3[::-1])
print(list3[-1:-5:-1])
print(list3[::2])
print(list3[0:4:1])


list1 = [12, 3.5, 'Hello',10+20j, [6, 7, 8],(5, 6, 7), True,{5, 7, 9},{'a': 123}]
print(list1[0:5:1])
print(list1[-1:-5:-1])
print(list1[::2])
print(list1[5][1])
print(list1[-4][-3])


s = "python"
rev = ""
for i in s:
    rev = i+rev
print(rev)

with open("TestFile.txt","r") as f:
    data = f.read()
    print(len(data))

with open("TestFile.txt","w") as f:
    f.write("I am Learning Python with Automation")




