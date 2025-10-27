"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""
list1 = [12, 3.5, 'Hello',10+20j, [6, 7, 8],(5, 6, 7), True,{5, 7, 9},{'a': 123}]
print(list1,type(list1))
#[12, 3.5, 'Hello', (10+20j), [6, 7, 8], (5, 6, 7), True, {9, 5, 7}, {'a': 123}] <class 'list'>
print(list1[0:5:1])
#[12, 3.5, 'Hello', (10+20j), [6, 7, 8]]
print(list1[6]) # True
print(list1[4][1]) # 7
print(list1[-4])
print(list1[-4][-1]) # 7

print("-"*50)
####################################################
list2 = ['a', 'b', 'c', 10, 20, 30]

# loop to get value without indexing
for val in list2:
    print(val)
'''
a
b
c
10
20
30
'''
print("-"*50)

# loop to get value with indexing
list_len = len(list2)
for i in range(list_len):
    print(i,list2[i])
'''
 0 a
1 b
2 c
3 10
4 20
5 30
 '''
print("-"*50)

######################## Slicing in the list ##############################
list3 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']
print(list3[0:5:1])