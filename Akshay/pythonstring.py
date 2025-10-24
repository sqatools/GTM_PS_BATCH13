str1= "Akshay bardapure"

print(str1[::-1])## string[start : stop : step]

##Python program to repeat a given string 5 times.
str1="SQAtools"
n1=5
print(n1*str1)
##
num1=15
if num1%3==0:
 print("divisble by 3")
else:
 print("not")

 #string formating#

name ="rohan"
age=22
city="mumbai"

result=("my name is rohan and my age is 22 city mumbai")
print(result)

# 1.  string concatenation:
result="my name is "+name+"and age is"+str(age)+",live in "+city
print(result)

# 2.  format method:
result2 = "My name is {} and age is {}, I live in {}".format(name, age, city)
print(result2)


# 3.  fstring formatting method:
result3 = f"My name is {name} and age is {age}, I live in {city}"
print(result3)