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

for i in range(-list_length, 0, 1):
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
"""
Rule1 = str[start index: end index]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right only.
->  start index and end index could be +ve or -ve
->  default start index is zero.
->  default end index is end of string.
->  default step value is 1

Rule2 = str[start index: end index: step value]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right or right left.
->  start index and end index could be +ve or -ve
->  and step value also could be +ve or -ve
->  default start index will be -1 if step value is -ve.
->  default start index will be zero if step value is +ve
"""
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
list4.append(20)
print("list4: ", list4)
list4.append(3000)
print("list4: ", list4)

print("_"*50)
#####################
# insert method :  this method insert data at specific index position.
list5 = [8, 9, 12, 4, 7]
list5.insert(2, 10)
print(list5) #[8, 9, 10, 12, 4, 7]

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
print("l2:", l2) #l2: ['a', 'b', 'c', 4, 7, 9]

str1 = "Hello"
l3 = [1, 2, 3]
l3.extend(str1)
print("l3:", l3) #l3: [1, 2, 3, 'H', 'e', 'l', 'l', 'o']

set1 = {5, 7, 9, 5}
l4 = ['a', 'b', 'c']
l4.extend(set1)
print("l4 :", l4) # ['a', 'b', 'c', 9, 5, 7]


print("_"*50)
##########################################################
# list concatenation:
l6 = [4, 5, 7]
l7 = [1, 2, 3]
l8 = l6+l7
print(l8) #[4, 5, 7, 1, 2, 3]

# print(dir(list))
# print(dir(dict))
# dict1 = {'a': 123}
# dict1['b'] = 456
# print(dict1)

print("_"*50)
##########################################################
# remove method :  remove any specific value from list
listb = [1, 4, 5, "Hi"]
listb.remove(4)
print(listb) #[1, 5, 'Hi']

print("_"*50)
##########################################################
# pop method :  this method remove value from list using index position.
#              ->  default index position is -1
#              -> This method return the removed value, that we can store in a variable

# remove default index -1
list_c = [5, 7, 2, 15, 18]
p1 = list_c.pop()
print("removed value :", p1)
print(list_c)

# remove from specific index
p2 = list_c.pop(3)
print("removed value :", p2)
print(list_c)

print("_"*50)
##########################################################
# clear method : clear all data from list
list1 = [5, 7, 9, 2]
list1.clear()
print(list1)

print("_"*50)
############################################################
# copy() method:

# Shallow copy: when we assign one list to another list, and modify any value in both the list
# then changes will reflect in both lists.
list_d = [4, 7, 9, 23]
list_e = list_d
list_d.append(11)
list_e.append(22)
print(list_d)
print(list_e)


print("_"*50)
# Deep Copy: In this concept we have to copy method to create a of list, and if we will do modification in any of the list
# then changes will not reflect in another list.
list_x = ['a', 'b', 'c']
list_y = list_x.copy()
list_x.append(100)
list_y.append(200)
print("list x is: ", list_x)
print("list y is: ", list_y)

print("_"*50)
#####################################################
# sort method :
list1 = [5, 8, 1, 2, 6, 100]
# sort in ascending order
list1.sort()
print("list1 after sorting: ", list1)

# sort in descending order
list2 = [5, 8, 15, 1, 2, 6, 100, 20]
list2.sort(reverse=True)
print("list2 after sorting: ", list2)









