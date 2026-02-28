#Reverse a string without using built-in functions.
from multiprocessing.reduction import duplicate

s = "python"
rev = ""
for i in s:
    rev = i+rev
print(rev)

#Check if a string is a palindrome
s = "madam"
if s==s[0:0:-1]:
    print("palindrome")
else:
    print("not palindrome")

#Find duplicate elements in a list
lst = [1, 2, 3, 2, 4, 1]
duplicate = set([x for x in lst if lst.count(x)>1])
print(duplicate)

#Remove duplicates from a list
lst = [1, 2, 2, 3, 4, 4,5]
unique = []
for ch in lst:
    if ch not in unique:
        unique.append(ch)
print(unique)

s = "programming"
rem_dup = ''
for i in s:
    if i not in rem_dup:
        rem_dup +=i
print(rem_dup)

#Swap two numbers without using a third variable
a = 20
b = 30

a, b = b,a
print(a,b)

#Find the largest number in a list
lst = [10, 5, 20, 8]
max = lst[0]
for i in lst:
    if i > max:
        max =i
        print(i)

#Count character occurrences in a string
s = "automation"
count_char = {}
for ch in s:
    count_char[ch] = count_char.get(ch,0) + 1
print(count_char)


#Python code to count characters (elements) in the list
items = ['api', 'ui', 'api', 'ui', 'db', 'api']

char_count = {}
for ch in items:
    char_count[ch] = char_count.get(ch,0) + 1
print(char_count)

#Check if a number is prime
num1 = 7
if num1 > 1:
    for i in range(2,num1):
        if num1 % i == 0:
            print('not Prime number')
            break
    else:
        print('prime')

#Fibonacci series
n = 6
a,b = 0,1
for _ in range(n):
    print(a,end='')
    a,b = b, a+b

print('-'*50)
#Find missing number in a list
lst1 = [1, 2, 3, 5]
n = 5
missing_no = n*(n+1)//2 - sum(lst1)
print(missing_no)

with open('2ndFiles.txt', 'r') as f:
    lines = f.read()
    print(len(lines))

try:
    x = 10/0
except:
    print('zero is not divisible')
finally:
    print('Execution completed')

#Print numbers from 1 to 10 using
for i in range(1,11):
    print(i)
print('-'*50)
# Print even numbers from 1 to 20
for i in range(2,21,2):
    print(i)

print('-'*50)

for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i)
print('-'*50)

# Print odd numbers from 1 to 20
for i in range(1,21,2):
    print(i)
print('-'*50)

# Print numbers in reverse order (10 to 1)
for i in range(10,0,-1):
    print(i)

print('-'*50)
# sum of 1 to 100
sum = 0
for i in range(1,101):
    sum +=i
print(sum)

#Print multiplication table of 5
for i in range(1,11):
    print(f'5X {i}',5*i)

num = list(range(5))
print(num)

# Loop through list using range(len())
lst = ["a", "b", "c"]
for i in range(len(lst)):
    print(i,lst[i])

print('-'*50)
#count even number using range
count=0
for i in range(2,11,2):
    count += 1
    print(count,i)

print('-'*50)
#Count vowels in string
s = "automation"
vowels = "aeiou"
count = 0
print('-'*50)
for ch in s:
    if ch in vowels:
        count += 1
print(count)


#Abstraction:
class Animal:
    def name(self):
        pass
    def bread(self):
        pass
    def voice(self):
        pass

class Dog(Animal):
    def name(self):
        print('Raja')
    def bread(self):
        print('Germanshefard')
    def voice(self):
        print('bho bho')
    def Dog_details(self):
        self.name()
        self.bread()
        self.voice()

class Cat(Animal):
    def name(self):
        print('Kajal')
    def bread(self):
        print('Gavathi')
    def voice(self):
        print('maumau')

    def cat_details(self):
        self.name()
        self.bread()
        self.voice()

obj=Dog()
obj.Dog_details()

print('-'*50)
obj1 = Cat()
obj1.cat_details()

#inheritance
class Father:
    def __init__(self,f_name,f_bus,f_car):
        self.Father_name = f_name
        self.Father_busniess = f_bus
        self.Father_car = f_car

    def show_father_name(self):
        print('Father Name',self.Father_name)
    def show_father_busniess(self):
        print('Father Busniess',self.Father_busniess)
    def show_father_car(self):
        print('Father Car',self.Father_car)

    def father_details(self):
        self.show_father_name()
        self.show_father_busniess()
        self.show_father_car()

class son(Father):
    def __init__(self,s_name,f_name,f_bus,f_car):
        super().__init__(f_name,f_bus,f_car)
        self.son_name = s_name

    def show_son_name(self):
        print('Son Name',self.son_name)

    def Family_details(self):
        self.show_son_name()
        self.father_details()

obj=son('Rohit','Ramchandra','Medical','swift dzire')
obj.Family_details()


with open("rohit_branch_file.txt",'r') as f:
    data = f.read()
    print(data)
    print(len(data))

with open("rohit_branch_file.txt","w") as f:
    f.write("I have done Python Automation class _1")

with open("rohit_branch_file.txt",'a') as f:
    f.write("I have started giving Interviews on Python Automation")



items = ['api', 'ui', 'api', 'ui', 'db', 'api']
char_count = {}
for i in items:
    char_count[i] = char_count.get(i,0)+1
print(char_count)


