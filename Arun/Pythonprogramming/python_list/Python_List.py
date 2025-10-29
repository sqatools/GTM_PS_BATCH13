list1 = [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {5, 7, 9}, True]
print(list1, type(list1))

# [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {9, 5, 7}, True] <class 'list'>

print(list1[2])  # Hello
print(list1[-3]) # {'a': 123}
print(list1[4])  # [6, 7, 8]
print(list1[4][1]) # 7

print("_"*50)
###################################################
list2 = ['a', 'b', 'c', 10, 20, 30]

# loop to get value without indexing
for val in list2:
    print(val)

print("_"*50)
# loop to get value with indexing
list_len = len(list2)

for i in range(list_len):
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
######################## Slicing in the list ##############################
list3 = [5, 8, 9, 2, 15, 'a', 'p', 'q', 'b']
print(list3[0:5]) # [5, 8, 9, 2, 15]
print(list3[-5:-10:-1])  # [15, 2, 9, 8, 5]
print(list3[5:9:1]) # ['a', 'p', 'q', 'b']
print(list3[::-1]) # ['b', 'q', 'p', 'a', 15, 2, 9, 8, 5]
print(list3[-1:-10:-1]) # ['b', 'q', 'p', 'a', 15, 2, 9, 8, 5]

print("_"*50)
################################### list methods #############################
# Append method :  This method add value to the list at the end.
list4 = [5, 7, 9, 23]
list4.append(10)
print("list4 :", list4)
list4.append(500)
print("list4 :", list4)


print("_"*50)
#####################
# insert method :  this method insert data at specific index position.
list5 = [8, 9, 12, 4, 7]
list5.insert(2, 100)
print("list5 :", list5)  # [8, 9, 100, 12, 4, 7]

list5.insert(0, 200)
print("list5 :", list5)  # [200, 8, 9, 100, 12, 4, 7]

list6 = ['Python', 'Hello', 'Learning', 4, 7]
list6.insert(3, 'Programming')
print("list6 :", list6) # ['Python', 'Hello', 'Learning', 'Programming', 4, 7]


print("_"*50)
#####################
# extend method : this method add one list data to another list.
l1 = [4, 7, 9]
l2 = ['a', 'b', 'c']

l2.extend(l1)

print("l2 :", l2) # ['a', 'b', 'c', 4, 7, 9]
print("l1 :", l1) # [4, 7, 9]

str1 = "Hello"
l3 = [1, 2, 3]
l3.extend(str1)
print("l3 :", l3) # l3 : [1, 2, 3, 'H', 'e', 'l', 'l', 'o']

set1 = {5, 7, 9, 5}
l4 = ['a', 'b', 'c']
l4.extend(set1)
print("l4 :", l4) # ['a', 'b', 'c', 9, 5, 7]

print("_"*50)
##########################################################
# list concatenation:
l6 = [7, 8, 9]
l7 = [10, 20, 30]
l8 = l6+l7
print("l8 :", l8) # [7, 8, 9, 10, 20, 30]

####################################################

# Append method :  This method add value to the list at the end.
list4 = [5, 7, 9, 23]
list4.append(10)
print("list4 :", list4)
list4.append(500)
print("list4 :", list4)


print("_"*50)
#####################
# insert method :  this method insert data at specific index position.
list5 = [1,2,56,6,99,102]
list5.insert(7, 100)
print("list5 :", list5)

list5.insert(0, 109)
print("list5 :", list5)

list6 = ['Arun', 'Tej', 'Learning''python', 4, 7]
list6.insert(3, 'Programming')
print("list6 :", list6)
