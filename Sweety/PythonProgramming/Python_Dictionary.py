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
dict1 = {'a': 123, 'b': 456, 'c': 789}
print(dict1, type(dict1)) # <class 'dict'>

# <class 'dict'>
dict1['d'] = 100
dict1['b'] = 500
print("dict1: ", dict1)

# Apply loop on dictionary

for key, val in dict1.items():
    print(key, ":", val)
    #print(key, val)

print("_"*50)
#######################
# write a python program to create a dictionary from given string.
str1 = "We are learning Python"
# output = {"W": We, "a": "are", "l": "learning", "P": "Python"}
result = {}
word_list = str1.split(" ")
for word in word_list:
    print(word)
    first_index = word[0]
    result[first_index] = word
print("Result: ", result)
Result:  {'W': 'We', 'a': 'are', 'l': 'learning', 'P': 'Python'}

print("_"*50)
#######################
# write a python program to get number from 1 to 20 and store even value as key and their square as dict value.
# dict2 = {2 :4, 4: 16, 6: 36, 8: 64, 9: 81}
result2 = {}
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        result2[i] = i**2
    else:
     continue
print(result2)

###############################################
# Q3:  write a python program to get desire result:
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# output = {'a' : 6, 'b': 15, 'c': 24}

output = {}
for k, v in dict1.items():
    output[k] = sum(v)
print("output is: ", output)

###################################
# dictionary methods

print("_"*50)
###################
# update method:  this method combine 2 dicts data
dict1 = {'a': 77, 'b': 88, 'c': 99}
dict2 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7)}

print("before updating dict1:", dict1) #{'a': 77, 'b': 88, 'c': 99}
print("before updating dict2:", dict2) #{12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7)}

dict2.update(dict1)
print("after updating dict1:", dict1) #{'a': 77, 'b': 88, 'c': 99}
print("after updating dict2:", dict2) #{12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}


print("_"*50)
###################
# pop() method :  This method remove any specific data using key and return it.
dict3 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
print("before poping dict3:", dict3) #{12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
val = dict3.pop('a')
print("Removed val:", val)
print("ater poping dict3:", dict3) #{12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'b': 88, 'c': 99}


print("_"*50)
###################
# delete data using del keyword
dict4 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'b': 88, 'c': 99}

del dict4[16]
print("dict4: ", dict4) #{12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

# this will remove entire variable from memory.
del dict4
# print(dict4)
# NameError: name 'dict4'

print("_"*50)
###################
# popitem() method : It will remove last item from the dictionary
dict5 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

val = dict5.popitem()
print("value: ", val)
print("dict5:", dict5)

print("_"*50)
#######################################
list1 = ['p', 'q', 'r']
list2 = [100, 200, 300, 400]
dict1 = dict(zip(list1, list2))
print(dict1)


print("_" * 50)
###############################################
# keys and values.

dict6 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

print("list of keys: ", dict6.keys)
print("list of values: ", dict6.values())

# get method: get value with the help of key
print(dict6.get(13)) # [5, 6, 7]

print("_" * 50)
#############################################
from pprint import pprint

# get data from dictionary
school = {
    'teacher': {
        'English': [
            {'name': 'Rohit', 'email': 'rohit@gmail.com', 'phone': 6546456},
            {'name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 56432343}
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

pprint(school['teacher']['English'][1]['phone'])
pprint(school['student']['10th'][0]['email'])
pprint(school)

print("_"*50)
####################################################

# sorted dictionary.
dict_x = {'a': 56, 'z': 2, 'p': 123, 'g': 10}

print(dict_x) #{'a': 56, 'z': 2, 'p': 123, 'g': 10}

print(dict_x.items()) #([('a', 56), ('z', 2), ('p', 123), ('g', 10)])

# sort the dict with keys.
print(sorted(dict_x.items())) #[('a', 56), ('g', 10), ('p', 123), ('z', 2)]

result1 = dict(sorted(dict_x.items()))
print("sorted with keys :", result1)

# sort with the help of values.
result2 = dict(sorted(dict_x.items(), key=lambda item: item[1]))
print("sorted with values :", result2)  # {'z': 2, 'g': 10, 'a': 56, 'p': 123}

print("_"*50)
#####################################################
# program to practice"
fruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25, "lichi": 30, "Pinapple": 60}
fruit_purchased ={"Banana": 12,"Apple": 10, "Mango": 5,  "Watermelon": 2}
# calculate total bill
total_bill = 0

for fruit, purches in fruit_purchased.items():
    f_price = fruit_price[fruit]
    fruit_bill = f_price * purches
    total_bill = total_bill + fruit_bill
    print(fruit, ":", f_price, ":", purches, ":", fruit_bill)

print("_"*20)
print("Total bill :", total_bill)
# Total bill : 820

