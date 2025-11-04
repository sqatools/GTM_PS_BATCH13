#13-Oct Class
#################################### set ###########################

"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.
->Main purpose is to maintain uniqueness

"""

set1 = {2, 3.4, 60+20j, 'Hello', (4, 7, 9), True, 2, 3.4}
print(set1, type(set1))
# {True, 2, 3.4, (4, 7, 9), (60+20j), 'Hello'} <class 'set'>
#next time we execute - again the order it gives will be random

# List is not allowed as set member
#set2 = {2, 3.4, 60+20j, 'Hello', (4, 7, 9), True, 2, 3.4, [4, 6, 7]}
#print(set2)
# TypeError: unhashable type: 'list'