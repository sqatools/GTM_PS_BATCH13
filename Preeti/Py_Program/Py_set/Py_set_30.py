"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""

set1 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 3.5, True}
print(set1, type(set1))  # {True, 3, 3.5, (3, 5, 6), 'Hello'} <class 'set'>

# apply loop on set.
set3 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 7, 3.5}
for val in set3:
    print(val)
print(len(set3))

# Add method: add data to the set.
set_1={'a','b','c'}
set_2={2,8,5,9}
result=set_1.union(set_2)
print(result)

# remove non existing value
#result=set3.remove(100) #key error

# remove existing value



