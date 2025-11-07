######### 13th Oct Class##########
#################################### Tuple ###########################
"""
# Properties
-> Tuple is immutable datatype.
-> Tuple can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> Tuple follow positive and negative indexing.
-> Tuple contains values in round bracket.
-> Can not modify tuple values.
-> When we want to keep data constant then we should tuple. e.g. days in week, months in year etc.
"""

tup1 = (4, 7.9, 'Python', [3, 6], (2, 7), {'a': 345}, {76, 8}, True)
print(tup1, type(tup1))
# (4, 7.9, 'Python', [3, 6], (2, 7), {'a': 345}, {8, 76}, True) <class 'tuple'>

print(tup1[4])  # (2, 7)
print(tup1[4][1])  # 7
print(tup1[-4]) # (2, 7)
print(tup1[-4][-2]) # 2