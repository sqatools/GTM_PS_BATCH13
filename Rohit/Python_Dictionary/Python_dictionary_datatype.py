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
from Deepesh.PythonProgramming.Python_Dict.python_dict_datatype import result, first_char

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

