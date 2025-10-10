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

