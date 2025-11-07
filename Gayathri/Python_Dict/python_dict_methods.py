#31st-oct-25
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
print(dict1, type(dict1))  # <class 'dict'>

# Add new key to dictionary
dict1['d'] = 100
dict1['b'] = 500 #update the existing value
print("dict1 :", dict1)  # dict1 : {'a': 123, 'b': 500, 'c': 789, 'd': 100}

#to use the for loop, we need to know the values, so we use dict1.items
print(dict1.items())  # ([('a', 123), ('b', 500), ('c', 789), ('d', 100)])
#in dict - we have key,value pair - so we need to use 2 varaibles
for i,j in dict1.items():
    print(i, j)
"""
a 123
b 500
c 789
d 100
"""
print("_" * 50)
#######################

# dictionary methods

print("_" * 50)
###################
# update method:  this method combine 2 dicts data
dict1 = {'a': 77, 'b': 88, 'c': 99}
dict2 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7)}
dict2.update(dict1)
print("dict2 :", dict2)
# {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}

print("_" * 50)
###################
# pop() method :  This method remove any specific data using key and return it.
dict3 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'a': 77, 'b': 88, 'c': 99}
val = dict3.pop('a')
print("Removed value :", val) #Removed value : 77
print("dict3 :", dict3)
# {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'b': 88, 'c': 99}

print("_" * 50)
###################
# delete data using del keyword - it removes the entire varaibel from the memory  itself
dict4 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7), 'b': 88, 'c': 99}
del dict4[16]
print("dict4 :", dict4)  # {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

# this will remove entire variable from memory.
del dict4
# print(dict4)
# NameError: name 'dict4'

print("_" * 50)

#diffrence bewteen pop and delete is, pop - it retruns the value and that value we can store in some varaible or dict again.
#but delete - it removes the variable from memory itself, we cant store that nor it retruns the value
###################
# popitem() method : remove the data as key value pair, it removes the last data in the dict
dict5 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

val = dict5.popitem()
print("value :", val)  # ('c', 99)
print("dict5 :", dict5)  # {12: 'Hello', 13: [5, 6, 7], 'b': 88}

print("_" * 50)
#######################################
list1 = ['p', 'q', 'r']
list2 = [100, 200, 300, 400]
#combine 2 list and create a dict - zip
dict1 = dict(zip(list1, list2))
print(dict1)  # {'p': 100, 'q': 200, 'r': 300}

print("_" * 50)
######################################################
#4th Nov Class
# keys and values.
dict6 = {12: 'Hello', 13: [5, 6, 7], 'b': 88, 'c': 99}

#get the keys and values seperately from the dict

print("list of keys :", dict6.keys())  # [12, 13, 'b', 'c']
print("list of values :", dict6.values())  # ['Hello', [5, 6, 7], 88, 99]

# get method: get value with the help of key
print(dict6.get(13))  # [5, 6, 7]

print("_" * 50)
#############################################

print(dir(dict  ))
#clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#############################################
#4th Nov
 #sorted dictionary.
dict_x = {'a': 56, 'z': 2, 'p': 123, 'g': 10}

print(dict_x)

#dict.items()- it returns the key and value as tuples
print(dict_x.items())  # ([('a', 56), ('z', 2), ('p', 123), ('g', 10)])

# sort the dict with keys.
result1 = dict(sorted(dict_x.items()))
print("sorted with keys :", result1)  # {'a': 56, 'g': 10, 'p': 123, 'z': 2}

# sort with the help of values.
#here to sort based on the value, key is index[0], value is [1]. so to do that, we use lambda and item:item[1]
result2 = dict(sorted(dict_x.items(), key=lambda item: item[1]))
print("sorted with values :", result2)  # {'z': 2, 'g': 10, 'a': 56, 'p': 123}

result2 = dict(sorted(dict_x.items(), key=lambda item: item[0]))
print("sort with keys :", result2) #sort with keys : {'a': 56, 'g': 10, 'p': 123, 'z': 2}
print("_"*50)