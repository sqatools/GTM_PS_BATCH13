"""
# Properties
-> Tuple is immutable datatype.
-> Tuple can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> Tuple follow positive and negative indexing.
-> Tuple contains values in round bracket.
-> Can not modify tuple values.
-> When we want to keep data constant then we should tuple. e.g. days in week, months in year etc.
"""
from Deepesh.PythonProgramming.PythonString.string_prog_practice import count

tup1 = (3, 3.5, 'Hello', [4, 7, 8], (6, 7), {'a': 123}, {4, 7, 8}, True)
print(tup1, type(tup1))  # <class 'tuple'>


##################
# apply loop on tuple without indexing
for i in tup1:
    print(i)

"""
3
3.5
Hello
[4, 7, 8]
(6, 7)
{'a': 123}
{8, 4, 7}
True
"""
print("_" * 50)
# Apply loop with indexing
for i in range(len(tup1)):
    print(i,tup1[i])

"""
0 3
1 3.5
2 Hello
3 [4, 7, 8]
4 (6, 7)
5 {'a': 123}
6 {8, 4, 7}
7 True
"""
print("_" * 50)
############################# Slicing #######################
tup2 = (3, 3.5, 'Hello', [4, 7, 8], (6, 7), {'a': 123}, {4, 7, 8}, True)
print(tup2[2:5])  # ('Hello', [4, 7, 8], (6, 7))

#reverse the tuple
print(tup2[::-1]) #(True, {8, 4, 7}, {'a': 123}, (6, 7), [4, 7, 8], 'Hello', 3.5, 3)

#Get every alternate value, i.e skip 1 value, so step is 2
print(tup2[::2])# (3,'Hello',(6,7),{8, 4, 7})

print("_" * 50)
############################# method #######################
# count method:
tup3 = (4, 7, 9, 3, 4, 8, 4)

#want to know how many times 4 is there in the tuple
print("num 4 is repeated:", tup3.count(4) , 'times')#num 4 is repeated: 3 times

# Index method:
print("Index of 9 :", tup3.index(9))
# Index of 9 : 2

###################################################
#concatenation of two tuples
t1 = (5, 7, 9)
t2 = ('a', 'b', 'c')

t3 = t1 + t2
print("t3 :", t3)  # (5, 7, 9, 'a', 'b', 'c')

#Existing tuple cannot be modified
print("_"*50)

##################################################
# sorted function:

tup4 = (5, 8, 12, 53, 7, 1, 2)
# sorted data in ascending order
print("sorted tuple is :",sorted(tup4)) #sorted tuple is : [1, 2, 5, 7, 8, 12, 53]
result1 = sorted(tup4)
print("Ascending order :", result1)  # [1, 2, 5, 7, 8, 12, 53]

# sorted data in descending order
result2 = sorted(tup4, reverse=True)
print("descending order :", result2)  # [53, 12, 8, 7, 5, 2, 1]

# reversed function:
result3 = tuple(reversed(tup4))
print("reversed output :", result3)  # (2, 1, 7, 53, 12, 8, 5)
