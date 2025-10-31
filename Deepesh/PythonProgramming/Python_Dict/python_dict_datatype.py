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

dict1 = {'a': 123, 'b' : 456, 'c': 789}
print(dict1, type(dict1))  # <class 'dict'>


# Add new key to dictionary
dict1['d'] = 100
dict1['b'] = 500
print("dict1 :", dict1)  # dict1 : {'a': 123, 'b': 500, 'c': 789, 'd': 100}


# Apply loop on dictionary
for k, v in dict1.items():
    print(k, "|", v)

"""
a | 123
b | 500
c | 789
d | 100
"""

print("_"*50)
#######################
# write a python program to create a dictionary from given string.
str1 = "We are learning Python"
# output = {"W": We, "a": "are", "l": "learning", "P": "Python"}

word_list = str1.split(" ")
print(word_list) # ['We', 'are', 'learning', 'Python']
result = {}
for word in word_list: # We, are, learning
    first_char = word[0]  # W, a, l
    result[first_char] = word
    print(result)

print("Result :", result)
# Result : {'W': 'We', 'a': 'are', 'l': 'learning', 'P': 'Python'}


print("_"*50)
#######################
# write a python program to get number from 1 to 20 and store even value as key and their square as dict value.
# dict2 = {2 :4, 4: 16, 6: 36, 8: 64, 9: 81}
result2 = {}

for i in range(1, 21):
    if i%2 == 0:
        result2[i] = i**2
    else:
        continue

print("result :", result2)

# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400}

###############################################
# Q3:  write a python program to get desire result:
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# output = {'a' : 6, 'b': 15, 'c': 24}
output = {}

for k, v in dict1.items():
    output[k] = sum(v)

print("output :", output)
# output : {'a': 6, 'b': 15, 'c': 24}

###################################
# dictionary methods

print("_"*50)
###################
# update method:  this method combine 2 dicts data
dict1 = {'a': 77, 'b': 88, 'c': 99}
dict2 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7)}

dict2.update(dict1)
print("dict2 :", dict2)
# {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}


print("_"*50)
###################
# pop() method :  This method remove any specific data using key and return it.
dict3 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
val = dict3.pop('a')
print("Removed value :", val)
print("dict3 :", dict3)
# {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'b': 88, 'c': 99}

print("_"*50)
###################
# delete data using del keyword
dict4 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'b': 88, 'c': 99}
del dict4[16]
print("dict4 :", dict4) # {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

# this will remove entire variable from memory.
del dict4
# print(dict4)
# NameError: name 'dict4'


print("_"*50)
###################
# popitem() method :
dict5 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

val = dict5.popitem()
print("value :", val)  # ('c', 99)
print("dict5 :", dict5) # {12: 'Hello', 13: [5, 6, 7], 'b': 88}

print("_"*50)
#######################################
list1 = ['p', 'q', 'r']
list2 = [100, 200, 300, 400]
dict1 = dict(zip(list1, list2))
print(dict1) # {'p': 100, 'q': 200, 'r': 300}






