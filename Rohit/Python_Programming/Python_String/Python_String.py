str1 = "Hello Python"
str2 = ''' 
My python programming
'''
str3 = """
Rohit Chavan from karad
"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))

print("-"*50)
##################################################################################
## String formatting
name = "Rohit"
age = 34
city = "Karad"
result = "My name is Rohit and age is 34, I live in Karad"

##1. String concatenation :
result1 = "My name is "+name+ " and age is "+str(age)+" I live in "+city
print(result1)

print("-"*50)

##2. format method:
result2 = "My name is {} and age is {} I live in {}".format(name,age,city)
print(result2)

print("-"*50)

result4 = "My name is {name} and age is {age} I live in {city}".format(name=name,age=age,city=city)
print(result4)

print("-"*50)

##3.fstring formatting method :
result3 = f"My name is {name} and age is {age} I live in {city}"
print(result3)

print("-"*50)
#################################################################################
## String Indexing and slicing
str_b = "Programming"
print(str_b[5]) ## a
print(str_b[-4]) ## m

print("-"*50)

######################### Slicing in string #############################
## Rule 1
'''
Rule1 = str[start index: end index]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right only.
->  start index and end index could be +ve or -ve
->  default start index is zero.
->  default end index is end of string.
->  default step value is 1 
'''

str_a = "Learning"
print(str_a[0:5]) ## Learn
print(str_a[1:6]) ## earni
print(str_a[-1:-5]) ##Only in this we can go left to right so result won't print
print(str_a[:7]) ## Learnin
print(str_a[0:]) ## Learning
print(str_a[0:-1]) ## Learnin
print(str_a[5:1]) ## Blank output as can not move from right o left


print("-"*50)

##Rule 2
"""
Rule2 = str[start index: end index: step value]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right or right left.
->  start index and end index could be +ve or -ve
->  and step value also could be +ve or -ve
->  default start index will be -1 if step value is -ve.
->  default start index will be zero if step value is +ve
"""

str1 = "Python Programming"
print(str1[0:2:1])   ## Py
print(str1[1:4:1])   ## yth
print(str1[-1:-6:-1]) ## gnimm
print(str1[-1:-9:-1]) ## gnimmarg
print(str1[-1:4:-1]) ## gnimmargorP n
print(str1[-1:7:-1]) ## gnimmargor


