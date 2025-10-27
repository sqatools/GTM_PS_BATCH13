"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""

list1 = [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {5, 7, 9}, True]
print(list1, type(list1))
#[12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {9, 5, 7}, True] <class 'list'>
print(list1[2])  #Hello
print(list1[3][1]) #6
print(list1[-4]) #[6, 7, 8]

print("_"*50)
###################################################
list2 = ['a', 'b', 'c', 10, 20, 30]
# loop to get value without indexing
for val in list2:
    print("list2:", val)

print("_"*50)
# loop to get value with indexing
list_length = len(list2)

for i in range(list_length):
    print(i, list2[i])

"""
0 a
1 b
2 c
3 10
4 20
5 30
"""

print("_"*50)

for i in range(-list_len, 0, 1):
    print(i, list2[i])

"""
-6 a
-5 b
-4 c
-3 10
-2 20
-1 30

"""

print("_"*50)


