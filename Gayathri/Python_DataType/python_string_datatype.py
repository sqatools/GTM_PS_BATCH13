
#Class : 10th Oct 25
######################### string #########################

"""
# String : Properties:
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

##give this character for next line \n
str1 = "Hello Gayathri \n Python"
print(str1, type(str1))

#########################################################################################


