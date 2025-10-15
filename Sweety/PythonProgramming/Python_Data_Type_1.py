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
num = 0
num1 = 145
num2 = 3535662536988980925324545143

print("num", num, type(num))
print("num1", num1, type(num1))
print("num2", num2, type(num2))



print("_"*100)

######################### Float #########################
"""
# Integer :  Properties
1.  Float is immutable data type
2.  Float contains pointer/decimal value.
3.  There is no range limit for Float.
"""
f1 = 23.8
f2 = 0.0
f3 = 4244126556435461413461.543324212311221321
print("f1", f1, type(f1))
print("f2", f2, type(f2))
print("f3", f3, type(f3))

print("_"*100)

######################### Complex #########################
"""
# Integer :  Properties
1.  Complex is immutable data type
2.  Complex number is combination of real and imaginary number e.g. x+yj
"""
comp1 = 10 + 20j
comp2 = 0 + 1j
comp3 = 50j
#real = 10
#img = 20j

print("comp1", comp1, type(comp1))
print("comp2", comp2, type(comp2))
print("comp3", comp3, type(comp3))


print("_"*100)
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
Preparing for upcoming meetings with relevant materials
Finding people based on relationships like team members or managers
Getting someone's profile details such as email, location, or job title
"""
s4 = '''
I'm AI Companion, your personal Zoom assistant. I can help you with:
Searching meetings, chats, emails, or files using keywords, attendees, or dates
Summarizing or answering questions about meetings, chats, emails, or files
Preparing for upcoming meetings with relevant materials
Finding people based on relationships like team members or managers
Getting someone's profile details such as email, location, or job title
'''
print("s1", s1, type(s1))
print("s2", s2, type(s2))
print("s3", s3, type(s3))

s5 = "Python"

"""
0   1   2   3   4  5     +ve indexing
 P   y   t   h   o  n
-6   -5 -4  -3  -2  -1    -ve indexing
"""
print("s5", s5, s5[0])
print("s5", s5, s5[-3])


print("_"*100)
#################################### List ###########################
"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""
list1 = [10, 3.6, "name", 50j, [2, 5], (1, 7), False, {'a': 123}, {8, 9}]
list1.append(200)         #It wll add this value at end
print(list1, type(list1)) #display type as <class 'list'
print(list1[1])           #diaplay value of index 1
print(list1[4][0])        #diaplay value of child index of list 0



print("_"*100)
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

tup1 = (22, 1.2, "Hi", 10+40j, [3, 4], (1, 2), True, {'b': 567}, {6, 7})
print(tup1, type(tup1))
print(tup1[3])
print(tup1[5][1])


print("_"*100)
#################################### dictionary ###########################
"""
Properties:
->  Dict is mutable datatype, we can modify any point of time.
->  Dict contains data in curly braces in keys value pair e.g.   {key : value}, {'a': 123}
->  Dict contains unique keys, duplicate keys are not allowed.
     {'a': 123, 'b': 456, 'a': 789}
     if we mention the duplicate then it will only consider the latest defined value
     it means it will consider a = 789

->  Only immutable data can be key in the dictionary e.g. int, float, string, tuple, boolean
   not allowed as key e.g. list, dict, set

-> Dict value can contain any types of data. e.g.  int, float, string, list, complex, tuple, set, boolean.
-> Dict does not follow indexing.

-> Dict follow LIFO (LAST IN FIRST OUT) concept 
"""

dict1 = {'a': 123, 'b': 456, 'c': 789}
print(dict1, type(dict1))
print(dict1['a'])         # Get data from dict

dict1["email"] = "name@gmail.com"
print(dict1)

dict1.popitem()
print(dict1.popitem())

print("_"*100)


print("_"*100)
#################################### set ###########################

"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""

set1 = {22, 3.4, 'Hi', (3, 5), True}
print(set1, type(set1))

# List is not allowed as set member
#set2 = {2, 3.4, 60+20j, 'Hello', (4, 7, 9), True, 2, 3.4, [4, 6, 7]}
#print(set2)
# TypeError: unhashable type: 'list'


print("_"*100)
#################################### Boolean ###########################
"""
Properties:

->  Boolean is immutable data type.
->  Boolean contains value as True or False.
->  Boolean is result of any conditional output.

"""

var1 = True
var2 = False
print(var1, type(var1))
print(var1, type(var2))

print(200 == 100)
print(100 == 100)


