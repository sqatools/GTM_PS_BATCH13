"""
1. Numbers:
     i) Integer
     ii) Float
     iii) Complex

2. Sequential
     i)  String
     ii)  List
     iii) Tuple

3. Dictionary

4. Set
5. Boolean
"""

######################### Integer #########################
"""
# Integer :  Properties
1.  Integer is immutable data type
2.  Integer only contains whole number.
3.  There is no range limit for integer
"""

num1 = 0
num2 = 400
num3 = 543543534543543543543545543

print("num1 :", num1, type(num1))  # num1 : 0 <class 'int'>
print("num2 :", num2, type(num2))  # num2 : 400 <class 'int'>
print("num3 :", num3, type(num3))  # num3 : 543543534543543543543545543 <class 'int'>

print("_" * 50)
######################### Float #########################
"""
# Integer :  Properties
1.  Float is immutable data type
2.  Float contains pointer/decimal value.
3.  There is no range limit for Float.
"""

f1 = 0.0
f2 = 56.78
f3 = 7189354435.3454353445678445
print("f1 :", f1, type(f1))  # 0.0 <class 'float'>
print("f2 :", f2, type(f2))  # 56.78 <class 'float'>
print("f3 :", f3, type(f3))  # 7189354435.345435 <class 'float'>

print("_" * 50)
######################### Complex #########################
"""
# Integer :  Properties
1.  Complex is immutable data type
2.  Complex number is combination of real and imaginary number e.g. x+yj
"""

comp1 = 10 + 20j
# real = 10
# img = 20
comp2 = 0 + 1j
comp3 = 50j

print("comp1", comp1, type(comp1))  # (10+20j) <class 'complex'>
print("real value :", comp1.real)  # 10.0
print("imag value :", comp1.imag)  # 20.0

print("comp2", comp2, type(comp2))  # 1j <class 'complex'>
print("comp3 :", comp3, type(comp3))  # comp3 : 50j <class 'complex'>

print("_" * 50)
######################### string #########################

"""
# Properties:
1. string in immutable data type.
2. we can defined string with sinlge/double/triple quote.
3. string follows positive and negative indexing.
4. There is no specific range for string.
"""

s1 = ""

s2 = 'Hello'

# to assign a paragraph value, we can use triple quotes.
s3 = """
I'm AI Companion, your personal Zoom assistant. I can help you with:
Searching meetings, chats, emails, or files using keywords, attendees, or dates
Summarizing or answering questions about meetings, chats, emails, or files
Preparing for upcoming meetings 12345 with relevant materials
Finding people based on relationships like team members or managers
Getting someone's profile details such as email, ^&^*&^&^ location, or job title
"""

s4 = '''
I'm AI Companion, your personal Zoom assistant. I can help you with:
Searching meetings, chats, emails, or files using keywords, attendees, or dates
Summarizing or answering questions about meetings, chats, emails, or files
Preparing for upcoming meetings with relevant materials
Finding people based on relationships like team members or managers
Getting someone's profile details such as email, location, or job title
'''

print("s1 :", s1, type(s1))  # <class 'str'>
print("-" * 20)
print("s2 :", s2, type(s2))  # Hello <class 'str'>
print("-" * 20)
print("s3 :", s3, type(s3))  # <class 'str'>
print("-" * 20)
print("s4 :", s4, type(s4))  # <class 'str'>
print("-" * 20)

s5 = "Python"

"""
 0   1   2   3   4  5     +ve indexing
 P   y   t   h   o  n
-6   -5 -4  -3  -2  -1    -ve indexing
"""

print(s5[0])  # P
print(s5[-5])  # y

var1 = "P1y 2 Thon"
print(var1[1])  # 1
print(var1[4])  # 2

print("_" * 40)
#################################### List ###########################
"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""

list1 = [1, 4.5, 'Hello', [4, 7], (3, 7), {'a': 123}, {45, 67}, True]
print(list1, type(list1))
# [1, 4.5, 'Hello', [4, 7], (3, 7), {'a': 123}, {67, 45}, True] <class 'list'>
print(list1[2])  # Hello

#        0    1       2
list2 = [20, [4, 8], True]
#       -3    -2     -1

print(list2[-2])  # [4, 8]
print(list2[-2][1])  # 8

# Add value to the list
list2.append(100)
print("list2 :", list2)
# list2 : [20, [4, 8], True, 100]


print("_" * 40)
#################################### Tuple ###########################
"""
# Properties
-> Tuple is immutable datatype.
-> Tuple can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> Tuple follow positive and negative indexing.
-> Tuple contains values in round bracket.
-> Can not modify tuple values.
-> When we want to keep data constant then we should tuple. e.g. days in week, months in year etc.
"""

tup1 = (4, 7.9, 'Python', [3, 6], (2, 7), {'a': 345}, {76, 8}, True)
print(tup1, type(tup1))
# (4, 7.9, 'Python', [3, 6], (2, 7), {'a': 345}, {8, 76}, True) <class 'tuple'>


print(tup1[4])  # (2, 7)
print(tup1[4][1])  # 7
print(tup1[-4])  # (2, 7)
print(tup1[-4][-1])  # 7

print("_" * 40)
#################################### dictionary ###########################
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

dict1 = {'a': 123, 'b': 567, 'c': 789}
print(dict1, type(dict1))

# {'a': 123, 'b': 567, 'c': 789} <class 'dict'>

# Get data from dict
print(dict1['a'])
# 123


user_details = {
    "name": "Rahul",
    "age": 25,
    "DOB": "1/02/2000",
    "phone": 78979798789,

}

print(user_details)  # {'name': 'Rahul', 'age': 25, 'DOB': '1/02/2000', 'phone': 78979798789}
print(user_details['phone'])  # 78979798789

# Add new detail to dict
user_details["email"] = "rahul123@gmail.com"
print(user_details)
# {'name': 'Rahul', 'age': 25, 'DOB': '1/02/2000', 'phone': 78979798789}

result = user_details.popitem()
print(result)  # ('email', 'rahul123@gmail.com')

dict3 = {1: 'Python',
         4.5: [5, 7, 8],
         5 + 60j: {'a': 345},
         'Python': (5, 7, 9),
         True: {4, 7, 9, 1, 2},
         (4, 7, 8): {'a': 678},
         100: 5000,
         }

print(dict3[4.5])  # [5, 7, 8]
print(dict3[100])  # 5000

print("_" * 40)
#################################### set ###########################

"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""

set1 = {2, 3.4, 60 + 20j, 'Hello', (4, 7, 9), True, 2, 3.4}
print(set1, type(set1))
# {True, 2, 3.4, (4, 7, 9), (60+20j), 'Hello'} <class 'set'>


# List is not allowed as set member
# set2 = {2, 3.4, 60+20j, 'Hello', (4, 7, 9), True, 2, 3.4, [4, 6, 7]}
# print(set2)
# TypeError: unhashable type: 'list'


print("_" * 40)
#################################### Boolean ###########################
"""
Properties:

->  Boolean is immutable data type.
->  Boolean contains value as True or False.
->  Boolean is result of any conditional output.

"""

var1 = True
var2 = False
print(var1, type(var1))  # True <class 'bool'>
print(var2, type(var2))  # False <class 'bool'>

print(200 == 100)  # False
print(300 == 300)  # True
