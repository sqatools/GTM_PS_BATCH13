"""
# Properties
-> Tuple is immutable datatype.
-> Tuple can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> Tuple follow positive and negative indexing.
-> Tuple contains values in round bracket.
-> Can not modify tuple values.
-> When we want to keep data constant then we should tuple. e.g. days in week, months in year etc.
"""

tup1 = (3,4.6,"World",[4,6,2],(2,4),{'a':12},{3,4,5},True)
print(tup1,type(tup1))
# (3, 4.6, 'World', [4, 6, 2], (2, 4), {'a': 12}, {3, 4, 5}, True) <class 'tuple'>

print("-"*50)
##################
# apply loop on tuple
for val in tup1:
    print(val)
'''
3
4.6
World
[4, 6, 2]
(2, 4)
{'a': 12}
{3, 4, 5}
True
'''
print("-"*50)
# Apply loop with indexing
for i in range(len(tup1)):
    print(i, tup1[i])
'''
0 3
1 4.6
2 World
3 [4, 6, 2]
4 (2, 4)
5 {'a': 12}
6 {3, 4, 5}
7 True


'''
print("-"*50)
############################# Slicing #######################
tup2 = (3, 3.5, 'Hello', [4, 7, 8], (6, 7), {'a': 123}, {4, 7, 8}, True)
print(tup2[2:6])
# ('Hello', [4, 7, 8], (6, 7), {'a': 123})
print(tup2[-1:-4:-1])
# (True, {8, 4, 7}, {'a': 123})

print(tup2[::-1])
# (True, {8, 4, 7}, {'a': 123}, (6, 7), [4, 7, 8], 'Hello', 3.5, 3)

print(tup2[-2:2:-1])
# ({8, 4, 7}, {'a': 123}, (6, 7), [4, 7, 8])

print("-"*50)
############################# method #######################
# count method:
tup3 = (3,4,7,8,4,2,7,4)
print("Count of 4 :",tup3.count(4)) # Count of 4 : 3

print("-"*50)

# Index method:
print("Index of 8 :",tup3.index(8)) # Index of 8 : 3

print("-"*50)
###################################################
#combining 2 sets:
tup_1 = (1,3,5,7)
tup_2 = (2,4,8,9)
tup_3 = tup_1 + tup_2
print("tup_3 :", tup_3) # (1, 3, 5, 7, 2, 4, 8, 9)

print("-"*50)
##################################################
# sorted function:
tup4 = (5, 8, 12, 53, 7, 1, 2)

# sorted data in ascending order
result = sorted(tup4)
print("Ascending order :",result) # [1, 2, 5, 7, 8, 12, 53]

# sorted data in descending order
result1 = sorted(tup4,reverse=True)
print("Descending order :",result1) # [53, 12, 8, 7, 5, 2, 1]

# reversed function:
result2 = tuple(reversed(tup4))
print("Reversed order :", result2) # (2, 1, 7, 53, 12, 8, 5)

print("-"*50)

