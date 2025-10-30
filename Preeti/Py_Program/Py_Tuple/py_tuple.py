"""
# Properties
-> Tuple is immutable datatype.
-> Tuple can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> Tuple follow positive and negative indexing.
-> Tuple contains values in round bracket.
-> Can not modify tuple values.
-> When we want to keep data constant then we should tuple. e.g. days in week, months in year etc.
"""
from Partha.Homework_101825 import count

tuple1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(tuple1)
print(type(tuple1))

# apply loop on tuple
for val in tuple1:
    print(val)

print("_" * 50)
# Apply loop with indexing
for i in range(len(tuple1)):
    print(i,tuple1[i])

print("_" * 50)
############################# Slicing #######################
tup2 = (3, 3.5, 'Hello', [4, 7, 8], (6, 7), {'a': 123}, {4, 7, 8}, True)
print(tup2[::-1])
print(tup2[2:8])
print(tup2[-1])
print(tup2[::2])

print("_" * 50)
############################# method #######################
# count method:
tup3 = (4, 7, 9, 3, 4, 8, 4)
print(sum(tup3))


