"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""
set1 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 3.5, True}
print(set1, type(set1))
# {True, 3.5, 3, 'Hello', (3, 5, 6)} <class 'set'>

print("-"*50)

# Apply loop on set
set3 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 7, 3.5}
for val in set3:
    print(val)
'''
True
3.5
3
Hello
7
(3, 5, 6))
'''
print("Total value :",len(set3))  # 6

print("_"*50)
############################### Sets methods #########################
# Add method: add data to the set.
set_a = {3,6,9,11}
set_a.add(100)
print("set_a :" ,set_a) # {3, 100, 6, 9, 11}