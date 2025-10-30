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
