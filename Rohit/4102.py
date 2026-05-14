from Sweety.PythonProgramming.Python_Modules.os_module import file_name

with open("2ndFiles.txt", "r") as f:
    lines = f.read()
    print(len(lines))
print("-"*50)

with open("2ndFiles.txt","w") as f:
    f.write("I am Leaving in Karad City")
print("-"*50)

text = "I Love JAVA Programming"
unique_char = set(text)
print(unique_char)
print("-"*50)

str1 = "Gurgaon city is Good"
result = " ".join(words[::-1] for words in str1.split())
print(result)
print("-"*50)

st = "a2b3c4d1"
output = " "

for i in range(0,len(st),2):
    char = st[i]
    count = int(st[i+1])
    output += char*count
print(output)

print("-"*50)

Input= "abcabcbb"

unique_value = ""
for i in Input:
    if i not in unique_value:
        unique_value += i
print(unique_value)
print("-"*50)

rows = 4

for i in range(1,rows+1):
    print(""*(rows-i),end=" ")

    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("-"*50)

s = "python"
rev = ""

for ch in s:
    rev = ch + rev
print(rev)
print("-"*50)

str1 = "Karad city is Good"
words = str1.split()
result = words[0]+" "+words[2]+" "+words[3]+" "+words[1]
print(result)
print("-"*50)

s = "madam"
if s==s[::-1]:
    print("Polindroma")
else:
    print("Not Polindroma")
print("-"*50)

num =7
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a Prime number")
    else:
         print("Prime number")
print("-"*50)

n=5
a,b = 0,1

for _ in range(n):
    print(a,end="")
    a,b = b, a+b
print("-"*50)

for i in range(1,21):
    print(i)
print("-"*50)

for i in range(1,21,2):
    print(i)
print("-"*50)

for i in range(10,0,-1):
    print(i)
print("-"*50)

s = "automation"
vowels = "aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count +=1
    print(ch)
print("-"*50)
#ploymorshirm

class ABC():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def Addition(self):
        print("Addition :",self.n1+self.n2)

    def Subtraction(self):
        print("Subtraction :",self.n1-self.n2)

    def Multiplication(self):
        print("Multiplication :",self.n1*self.n2)

class DEF(ABC):
    def __init__(self,a,n1,n2):
        super().__init__(n1,n2)
        self.a = a

    def square(self):
        print("square:",a*a)

obj = ABC(21,13)
obj.Addition()
obj.Subtraction()
obj.Multiplication()

obj1 =DEF(2,0,0)
obj1.square()

print("-"*50)

class Animal:
    def name(self):
        pass

    def bread(self):
        pass

    def voice(self):
        pass

class Dog(Animal):
     def name(self):
         print("Tiger")

     def bread(self):
         print("GermanSherad")

     def voice(self):
         print("Bhoom")

     def details_of_Dogs(self):
         self.name()
         self.bread()
         self.voice()

class Cat(Animal):
    def name(self):
        print("Mani")

    def bread(self):
        print("Gavati")

    def voice(self):
        print("mavew")

    def details_of_cats(self):
        self.name()
        self.bread()
        self.voice()

obj =Dog()
obj.details_of_Dogs()

print("-"*50)
obj1 = Cat()
obj1.details_of_cats()
print("-"*50)

class Father:
    def __init__(self,f_name,f_business,f_car):
        self.name = f_name
        self.business = f_business
        self.car = f_car

    def father_name(self):
        print("Father Name :",self.name)

    def father_business(self):
        print("Father Business Name :",self.business)

    def father_car(self):
        print("Father Car Name :",self.car)

    def details_of_Father(self):
        self.father_name()
        self.father_business()
        self.father_car()

class Son(Father):
    def __init__(self,son,f_name,f_business,f_car):
        super().__init__(f_name,f_business,f_car)
        self.son = son

    def son_name(self):
        print("Son Name :",self.son)

    def details_of_famaily(self):
        self.details_of_Father()
        self.son_name()
obj = Son("Rohit","Ramchandra","Medical","Swift")
obj.details_of_Father()
obj.details_of_famaily()

print("-"*50)
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
import json
data = json.loads(sampleJson)
data["company"]["employee"]["payble"]["salary"] = 9000

update_json = json.dumps(data,indent=4)

print(update_json)

