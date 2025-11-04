"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""

list1 = [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {5, 7, 9}, True]
print(list1, type(list1))

# [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {9, 5, 7}, True] <class 'list'>

print(list1[2])  # Hello
print(list1[-3])  # {'a': 123}
print(list1[4])  # [6, 7, 8]
print(list1[4][1])  # 7

print("_" * 50)
###################################################
list2 = ['a', 'b', 'c', 10, 20, 30]

# loop to get value without indexing
for val in list2:
    print(val)

print("_" * 50)
# loop to get value with indexing
list_len = len(list2)  # 6

for i in range(list_len):
    print(i, list2[i])

# for i in range(0, 6, 1):
#     print(i)

"""
0 a
1 b
2 c
3 10
4 20
5 30
"""

print("_" * 50)
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

print("_" * 50)
######################## Slicing in the list ##############################
list3 = [5, 8, 9, 2, 15, 'a', 'p', 'q', 'b']
print(list3[0:5])  # [5, 8, 9, 2, 15]
print(list3[-5:-10:-1])  # [15, 2, 9, 8, 5]
print(list3[5:9:1])  # ['a', 'p', 'q', 'b']
print(list3[::-1])  # ['b', 'q', 'p', 'a', 15, 2, 9, 8, 5]
print(list3[-1:-10:-1])  # ['b', 'q', 'p', 'a', 15, 2, 9, 8, 5]

print("_" * 50)
################################### list methods #############################
# Append method :  This method add value to the list at the end.
list4 = [5, 7, 9, 23]
list4.append(10)
print("list4 :", list4)
list4.append(500)
print("list4 :", list4)

print("_" * 50)
#####################
# insert method :  this method insert data at specific index position.
list5 = [8, 9, 12, 4, 7]
list5.insert(2, 100)
print("list5 :", list5)  # [8, 9, 100, 12, 4, 7]

list5.insert(0, 200)
print("list5 :", list5)  # [200, 8, 9, 100, 12, 4, 7]

list6 = ['Python', 'Hello', 'Learning', 4, 7]
list6.insert(3, 'Programming')
print("list6 :", list6)  # ['Python', 'Hello', 'Learning', 'Programming', 4, 7]

print("_" * 50)
#####################
# extend method : this method add one list data to another list.
l1 = [4, 7, 9]
l2 = ['a', 'b', 'c']

l2.extend(l1)

print("l2 :", l2)  # ['a', 'b', 'c', 4, 7, 9]
print("l1 :", l1)  # [4, 7, 9]

str1 = "Hello"
l3 = [1, 2, 3]
l3.extend(str1)
print("l3 :", l3)  # l3 : [1, 2, 3, 'H', 'e', 'l', 'l', 'o']

set1 = {5, 7, 9, 5}
l4 = ['a', 'b', 'c']
l4.extend(set1)
print("l4 :", l4)  # ['a', 'b', 'c', 9, 5, 7]

print("_" * 50)
##########################################################
# list concatenation:
l6 = [7, 8, 9]
l7 = [10, 20, 30]
l8 = l6 + l7
print("l8 :", l8)  # [7, 8, 9, 10, 20, 30]

# print(dir(list))
# print(dir(dict))
# dict1 = {'a': 123}
# dict1['b'] = 456
# print(dict1)

print("_" * 50)
##########################################################
# remove method :  remove any specific value from list

list_b = [6, 7, 9, 2, 45]
list_b.remove(9)
print("list_b :", list_b)  # list_b : [6, 7, 2, 45]

print("_" * 50)
##########################################################
# pop method :  this method remove value from list using index position.
#              ->  default index position is -1
#              -> This method return the removed value, that we can store in a variable

list_c = [5, 7, 2, 15, 18]

# remove default index -1
v1 = list_c.pop()
print("removed value :", v1)  # 18
print("list_c :", list_c)  # [5, 7, 2, 15]

# remove from specific index
v2 = list_c.pop(1)
print("removed value :", v2)  # 7
print("list_c :", list_c)  # [5, 2, 15]

print("_" * 50)
##########################################################
# clear method : clear all data from list

list1 = [5, 7, 9, 2]
list1.clear()
print("list1 :", list1)  # list1 : []

print("_" * 50)
############################################################
# copy() method:

# Shallow copy: when we assign one list to another list, and modify any value in both the list
# then changes will reflect in both lists.

list_d = [4, 7, 9, 23]
list_e = list_d
list_e.append(100)
list_d.append(200)

print("list_e :", list_e)
print("list_d :", list_d)

print("_" * 50)
# Deep Copy: In this concept we have to copy method to create a of list, and if we will do modification in any of the list
# then changes will not reflect in another list.

list_x = ['a', 'b', 'c']
list_y = list_x.copy()
list_x.append('d')
list_y.append(100)
print("list_x :", list_x)  # ['a', 'b', 'c', 'd']
print("list_y :", list_y)  # ['a', 'b', 'c', 100]

print("_" * 50)
#####################################################
# sort method :
list1 = [5, 8, 1, 2, 6, 100]
# sort in ascending order
list1.sort()
print("list1 :", list1)  # [1, 2, 5, 6, 8, 100]

# sort in descending order
list2 = [5, 8, 15, 1, 2, 6, 100, 20]
list2.sort(reverse=True)
print("list2 :", list2)  # [100, 20, 15, 8, 6, 5, 2, 1]

print("_" * 50)
#####################################################
# reverse method : this method reverse entire list

list_x = [5, 7, 9, 23, 4, 78, 'Hello', 'Python']
list_x.reverse()
print("list x :", list_x)
# ['Python', 'Hello', 78, 4, 23, 9, 7, 5]

print("_" * 50)
####################################################
# write a python program to get all the even values from list
list1 = [4, 7, 9, 2, 8, 12, 11]
output = []

for val in list1:
    if val % 2 == 0:
        output.append(val)
    else:
        continue

print("output :", output)  # [4, 2, 8, 12]

# solve above program to with list comprehension
result = [abc for abc in list1 if abc % 2 == 0]
print("Result :", result)

print("_" * 50)
####################################################
# write a python program to get all the required output values from list.

list2 = [4, 7, 9, 12]
# output = [(4, 'even'), (7, 'odd'), (9, 'odd'), (12, 'even')]
output = []
for val in list2:
    if val % 2 == 0:
        output.append((val, 'even'))
    else:
        output.append((val, 'odd'))

print("output :", output)  # [(4, 'even'), (7, 'odd'), (9, 'odd'), (12, 'even')]

# solve above program with list comp.
list2 = [4, 7, 9, 12]
result2 = [(y, "even") if y % 2 == 0 else (y, "odd") for y in list2]
print("result2 :", result2)

result3 = ["even" if y % 2 == 0 else "odd" for y in list2]
print("result3 :", result3)

result4 = [y ** 2 if y % 2 == 0 else y ** 3 for y in list2]
print("result4 :", result4)  # [16, 343, 729, 144]

print("_" * 50),,,,,nbnv
######################## Max, Min, sum of list values ##############nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn  vvvv v   v vvvvvv vv
list1 = [4, 7, 10, 50, 23, 45]

print("max value :", max(list1))  # max value : 50
print("min value :", min(list1))  # min value : 4
print("sum of values :", sum(list1))  # sum of values : 139

print("_" * 50)
###########################################################
# sorted function.

# Increasing order
list2 = [6, 8, 9, 2, 1]
result2 = list(sorted(list2))  # [1, 2, 6, 8, 9]
print("sorted result :", result2)

# Decreasing order
result4 = list(sorted(list2, reverse=True))  # [9, 8, 6, 2, 1]
print("decreasing sorted result :", result4)

# reversed function
result3 = list(reversed(list2))
print("result3 :", result3)  # [1, 2, 9, 8, 6]
