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
print("num2 :", num2,  type(num2)) # num2 : 400 <class 'int'>
print("num3 :", num3,  type(num3)) # num3 : 543543534543543543543545543 <class 'int'>


print("_"*50)
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
print("f1 :", f1, type(f1)) # 0.0 <class 'float'>
print("f2 :", f2, type(f2)) # 56.78 <class 'float'>
print("f3 :", f3, type(f3)) # 7189354435.345435 <class 'float'>


print("_"*50)
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
print("real value :", comp1.real) # 10.0
print("imag value :", comp1.imag) # 20.0

print("comp2", comp2, type(comp2))  # 1j <class 'complex'>
print("comp3 :", comp3,  type(comp3)) # comp3 : 50j <class 'complex'>


print("_"*50)
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
print("-"*20)
print("s2 :", s2, type(s2))  #  Hello <class 'str'>
print("-"*20)
print("s3 :", s3, type(s3))  # <class 'str'>
print("-"*20)
print("s4 :", s4, type(s4))  # <class 'str'>
print("-"*20)


s5 = "Python"

"""
 0   1   2   3   4  5     +ve indexing
 P   y   t   h   o  n
-6   -5 -4  -3  -2  -1    -ve indexing
"""

print(s5[0])  # P
print(s5[-5]) # y

var1 = "P1y 2 Thon"
print(var1[1])  # 1
print(var1[4])  # 2
