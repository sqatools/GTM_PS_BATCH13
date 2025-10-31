"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""
set1 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 3.5, True}
print(set1, type(set1))
# {True, 3.5, 3, 'Hello', (3, 5, 6)} <class 'set'>

print("-"*50)

# Apply loop on set
set3 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 7, 3.5}
for val in set3:
    print(val)
'''
True
3.5
3
Hello
7
(3, 5, 6))
'''
print("Total value :",len(set3))  # 6

print("_"*50)
############################### Sets methods #########################
# Add method: add data to the set.
set_a = {3,6,9,11}
set_a.add(100)
print("set_a :" ,set_a) # {3, 100, 6, 9, 11}

print("-"*50)
#######################################################################
# remove method: remove any specific data from set
set_a = {3,5,6,11,14,55}

# remove existing value
set_a.remove(11)
print("set_a :", set_a) # {3, 5, 6, 55, 14}

# remove non-existing value
#set_a.remove(50)
#print("set_a :", set_a)
# KeyError: 50   if we try to remove value which not present in set then it will throw error

print("-"*50)
#####################
# discard method: this method remove any specific value from set and does not
# return anything if value is not available
set_b = {4,6,11,70,50}

# remove existing value
set_b.discard(70)
print("set_b :",set_b) # {50, 4, 6, 11}

# remove non-existing value
set_b.discard(100)
print("set_b :", set_b) # {50, 4, 6, 11}
# if we try to remove value which not present it doesn't throw error

print("-"*50)
#######################################################################
# union method :  this method combine two sets data
set_c = {4,6,8,22}
set_d = {'a','b','c','d'}
set_e= set_c.union(set_d)
print("set_e :",set_e) # {{4, 6, 'd', 8, 'b', 22, 'a', 'c'}

print("_"*50)
##########################################################
# update method :  this method update one sets data to another set

set_f = {1,2,3}
set_E = {'a','b','c'}
set_E.update(set_f)
print("set_E :",set_E) # {1, 2, 3, 'c', 'b', 'a'}
# print(set_f)

print("-"*50)
##########################################################
# difference method :  this method return the difference values from one set to another
set1 = {3,4,'a','b','c','d'}
set2 = {'a','b',34,22}
result1 = set1.difference(set2)
print("Result of difference value from set1 & set2 :",result1) # {3, 4, 'c', 'd'}
# set1 will differencet values with set2

result2 = set2.difference(set1)
print("Result of difference value from set1 & set2 :",result2) # {34, 22}

print("-"*50)
##########################################################
# symmetric difference method :  this method return the difference values from both sets
set1 = {3,4,'a','b','c','d'}
set2 = {'a','b',34,22}
result4 = set1.symmetric_difference(set2)
print("result4 :", result4)  # {34, 3, 4, 'd', 'c', 22}

result5 = set2.symmetric_difference(set1)
print("result5 :",result5) # {34, 3, 4, 'c', 22, 'd'}

print("-"*50)
##########################################################
# intersection method :  this method return the common values from both sets
set1 = {3,4,'a','b','c','d'}
set2 = {'a','b',34,22}
result6 = set1.intersection(set2)
print("result6 :", result6) # {'b', 'a'}

print("-"*50)
##########################################################
# Conversion from set to list
set1= {3,4,'a','b','c','d'}
list =list(set1)
print(list) # [3, 4, 'b', 'a', 'd', 'c']


print(dir(set)) # Method apart for this which raerly  used (Above all main methods mostly used)
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'