"""
Properties:
->  Dict is mutable datatype, we can modify any point of time.
->  Dict contains data in curly braces in keys value pair e.g.   {key : value}, {'a': 123}
->  Dict contains unique keys, duplicate keys are not allowed.
     {'a': 123, 'b': 456, 'a': 789}
     if we mention the duplicate then it will only consider the latest defined value
     it means it will consider a = 789

->  Only immutable data can be key in the dictionary e.g. int, float, complex,  string, tuple, boolean
   not allowed as key e.g. list, dict, set
   e.g.
   {1 : 'Python',
    4.5 : [5, 7, 8],
    5+60j : {'a': 345},
    'Python' : (5, 7, 9),
    True : {4, 7, 9, 1, 2},
    (4, 7, 8) :  {'a': 678}
    }

-> Dict value can contain any types of data. e.g.  int, float, string, list, complex, tuple, set, boolean.
-> Dict does not follow indexing.

-> Dict follow LIFO (LAST IN FIRST OUT) concept
"""

dict1 = {'a': 13,'b':34,'c':22}
print(dict1,type(dict1)) # {'a': 13, 'b': 34, 'c': 22} <class 'dict'>

# Add new key to dictionary
dict1['d'] = 100
dict1['c'] = 200
print("dict1 :",dict1) # {'a': 13, 'b': 34, 'c': 200, 'd': 100}

# Apply loop on dictionary
for k,v in dict1.items():
    print(k ,"|", v)
'''
a | 13
b | 34
c | 200
d | 100
'''
print("-"*50)
######################################################################
# write a python program to create a dictionary from given string.
str1 = "I am Leaving in Karad"
word_list = str1.split()
print(word_list)  # ['I', 'am', 'Leaving', 'in', 'Karad']
result = {}
for word in word_list:
    first_char = word[0]
    result[first_char] = word

print("Result :", result)     # {'I': 'I', 'a': 'am', 'L': 'Leaving', 'i': 'in', 'K': 'Karad'}

print("-"*50)
######################################################################
## write a python program to get number from 1 to 20 and store even value as key and their square as dict value.
result2 = {}
for i in range(1,21):
    if i%2==0:
        result2[i] = i**2
    else:
        continue
print("result :", result2)
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400}

print("-"*50)
######################################################################
# Q3:  write a python program to get desire result: sum of values
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
output = {}
for k,v in dict1.items():
    output[k] = sum(v)

print("output :",output) # {'a': 6, 'b': 15, 'c': 24}

print("-"*50)
######################################################################
# dictionary methods :

# 1.update method:  this method combine 2 dicts data
dict1 = {'a': 77, 'b': 88, 'c': 99}
dict2 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7)}
dict2.update(dict1)
print("dict2 :",dict2) # only dict2 will get modify
#print("dict1 :", dict1)
# dict2 : {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
# dict1 : {'a': 77, 'b': 88, 'c': 99}

print("-"*50)
###################
# 2.pop() method :  This method remove any specific data using key and return it.
dict3 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
val = dict3.pop('b')
print("Removed value :", val) # 88
print(dict3) # {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'c': 99}

print("-"*50)
val1 = dict3.pop(16)
print("Removed value1 :", val1) # (3, 5, 7)
print(dict3) #{12: 'Hello', 13: [5, 6, 7], 'a': 77, 'c': 99}

print("-"*50)
###################
# 3.delete data using del keyword : it will delete entire value from dictionary will not store to restore
dict4 = {12: 'Hello', 13: [5, 6, 7], 'a': 77, 'c': 99}
del dict4[13]
print("dict4 :",dict4) #{12: 'Hello', 'a': 77, 'c': 99}

# this will remove entire variable from memory.
#dict5 = {12: 'Hello', 'a': 77, 'c': 99}
#del dict5
#print(dict5)
## NameError: name 'dict5' is not defined

print("-"*50)
###################
# popitem() method : last value will get deleted/removed
dict6 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}
val = dict6.popitem()
print("value :", val) # ('c', 99)
print("dict6 :",dict6) # {12: 'Hello', 13: [5, 6, 7], 'b': 88}
#########################
# if we want combination of  2 list then zip is used and convert to dict:
list1 = ['p', 'q', 'r']
list2 = [100, 200, 300]
dict1 = dict(zip(list1,list2))
print(dict1) # {'p': 100, 'q': 200, 'r': 300}
print("-"*50)

list3 = ['p', 'q', 'r']
list4 = [100, 200, 300,400]
dict2 = dict(zip(list3,list4))
print(dict2) # {'p': 100, 'q': 200, 'r': 300} if combination is not their then 400 will get ignored

print("-"*50)
##############################################################################
# keys and values:
dict7 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}
print("list of keys :",dict7.keys()) # ([12, 13, 'b', 'c'])
print("list of values :",dict7.values()) # (['Hello', [5, 6, 7], 88, 99])

# get method: get value with the help of key
print(dict7.get('b')) # 88
print(dict7.get(12)) # Hello

print("-"*50)
#############################################
#from pprint import pprint : pprint is use to get structure as it is

from pprint import pprint

# get data from dictionary
school = {
    'teacher': {
        'English': [
            {'name': 'Rohit', 'email': 'rohit@gmail.com', 'phone': 6546456},
            {'name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 916736636}
        ],
        'Maths': [],
    },
    'student': {
        '10th': [
            {'name': 'mohit', 'email': 'mohit@gmail.com', 'phone': 8866868686},
            {'name': 'akshay', 'email': 'akshay@gmail.com', 'phone': 876766766},
        ],
        '11th': [],
    },
    'admin': {
        'account': [],
        'admission': []
    }

}
#pprint(school)
pprint(school['teacher']['English'][1]['email']) #'rahul@gmail.com'

print("-"*50)

#################################################
# program to practice"
fruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25}
fruit_purchased ={"Banana": 12,"Apple": 10, "Mango": 5,  "Watermelon": 2}
# calculate total bill
total_bill = 0

for fruit,purchased in fruit_purchased.items():
    f_fruit_price = fruit_price[fruit]
    fruit_bill = f_fruit_price*purchased
    total_bill = total_bill + fruit_bill
    print(fruit, ":", f_fruit_price, ":", purchased, ":", fruit_bill)

print('-'*20)

print("total bill :", total_bill) # 820

print("-"*50)
#############################################
# sorted dictionary.
dict_x = {'a': 56, 'z': 2, 'p': 123, 'g': 10}
print(dict_x)

print(dict_x.items()) # ([('a', 56), ('z', 2), ('p', 123), ('g', 10)])

print("-"*50)
# sort the dict with keys.
result1 = dict(sorted(dict_x.items()))
print("sorted by keys :",result1) # {'a': 56, 'g': 10, 'p': 123, 'z': 2}

# sort with the help of values.
result2 = dict(sorted(dict_x.items(), key=lambda item : item[1]))
print("sorted by values :",result2) # {'z': 2, 'g': 10, 'a': 56, 'p': 123}

print("-"*50)
#########################################################################
