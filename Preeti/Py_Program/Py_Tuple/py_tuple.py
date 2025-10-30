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

# count method:
tup3 = (4, 7, 9, 3, 4, 8, 4)

print("count of 4 :", tup3.count(4))
# count of 4 : 3

# Index method:
print("Index of 9 :", tup3.index(9))
# Index of 9 : 2

###################################################
t1 = (5, 7, 9)
t2 = ('a', 'b', 'c')

t3 = t1 + t2
print("t3 :", t3)  # (5, 7, 9, 'a', 'b', 'c')

print("_"*50)
##################################################
# sorted function:

tup4 = (5, 8, 12, 53, 7, 1, 2)
# sorted data in ascending order
result1 = sorted(tup4)
print("Ascending order :", result1)  # [1, 2, 5, 7, 8, 12, 53]

# sorted data in descending order
result2 = sorted(tup4, reverse=True)
print("descending order :", result2)  # [53, 12, 8, 7, 5, 2, 1]

# reversed function:
result3 = tuple(reversed(tup4))
print("reversed output :", result3)  # (2, 1, 7, 53, 12, 8, 5)
