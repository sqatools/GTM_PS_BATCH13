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


