"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""

set1 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 3.5, True}
print("set1 values: ", set1, type(set1))

# set2 = {3, 3.5, 'Hello', (3, 5, 6), True, [3, 5, 7]}
# print(set2)
# TypeError: unhashable type: 'list'
print("_" * 50)
##########################
# apply loop on set.
set3 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 7, 3.5}
for val in set3:
    print(val)

"""
True
3
3.5
(3, 5, 6)
Hello
"""

print("total values in set3: ", len(set3))
# Total values : 5

print("_"*50)
############################### Set methods #########################
# Add method: add data to the set.
set_a = {4, 6, 8, 12}
set_a.add(100)
print("set_a values: ", set_a)

print("set_a :", set_a) # {100, 4, 6, 8, 12}


print("_"*50)
######################
# remove method: remove any specific data from set

set_b = {4, 6, 8, 12, 5, 7}
set_b.remove(7)
# remove existing value
print("set b after removing 7: ", set_b) #{4, 5, 6, 8, 12}

# remove non-existing value
#set_b.remove(10)
# KeyError: 10

print("_"*50)
######################
# discard method: this method remove any specific value from set and does not return anything if value is not available

set_c = {4, 6, 8, 12, 50, 70}

# remove existing value
set_c.discard(8)
print("set_c after discarding existing value: ", set_c)

# remove non-existing value
set_c.discard(1200)
print("set_c after discarding non-existing value: ", set_c)

print("_"*50)
######################
# union method :  this method combine two sets data
set_A = {3, 5, 7}
set_B = {'a', 'b', 'c'}

Set_C = set_A.union(set_B)
print("Set_C afte union of set_A and Set_B: ", Set_C) #{'a', 3, 'c', 5, 7, 'b'}

print("_"*50)
######################
# update method :  this method update one sets data to another set

set_x = {3, 5, 7}
set_y = {'a', 'b', 'c'}

set_y.update(set_x)
print("set_y after updating: ", set_y) #{3, 'a', 5, 7, 'c', 'b'}

# result = set_x  + set_y
# print(result)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'


print("_"*50)
######################
# difference method :  this method return the difference values from one set to another
set_x = {3, 5, 7, 'a', 'b'}
set_y = {'a', 'b', 'c', 'p', 'q'}

result1 = set_x.difference(set_y)
print("result1: ", result1)

result2 = set_y.difference(set_x)
print("result2: ", result2)

print("_"*50)
######################
# symmetric difference method :  this method return the difference values from both sets

set_p = {3, 5, 7, 'a', 'b'}
set_q = {'a', 'b', 'c', 'p', 'q'}

result = set_p.symmetric_difference(set_q)
print("result: ", result)


print("_"*50)
######################
# intersection method :  this method return the common values from both sets

set_p = {3, 5, 7, 'a', 'b'}
set_q = {'a', 'b', 'c', 'p', 'q'}

result = set_p.intersection(set_q)
print(result)

# conversion from set to list
set_5 = {6, 8, 90, 21}
list5 = list(set_5)
print("list_5: ", list5, type(list5))

print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

