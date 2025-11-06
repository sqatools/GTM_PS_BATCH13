#30th Oct-25 - Class
"""
Properties:
->  Set is mutable data type, we can modify any point of time.
->  Set only store unique values, duplicate data is not allowed.
->  Set store values in random order.
->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

"""
set1 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 3.5, True}
print(set1, type(set1))  # {True, 3, 3.5, (3, 5, 6), 'Hello'} <class 'set'>

#incase we add in list the mutable data type i.e list
#set2 = {3, 3.5, 'Hello', (3, 5, 6), True, [3, 5, 7]}
#print(set2)
#TypeError: unhashable type: 'list'
print("_" * 50)
##########################
# apply loop on set.
for i in set1:
    print(i)

"""
True
3
3.5
(3, 5, 6)
Hello
"""
#get the length of the set
print("Total values :", len(set1))
# Total values : 5
print("_"*50)
############################### Sets methods #########################
# Add method: add data to the set.
set_a = {4, 6, 8, 12}
set_a.add(100)
print("set_a :", set_a) # {100, 4, 6, 8, 12}
print("_"*50)
#set_a : {100, 4, 6, 8, 12}
######################
# remove method: remove any specific data from set
set_b = {4, 6, 8, 12, 5, 7}
# remove existing value
set_b.remove(12)
print("set_b :", set_b)  # {4, 5, 6, 7, 8}

# remove non-existing value
#set_b.remove(10)
# KeyError: 10

print("_"*50)
######################
# discard method: this method remove any specific value from set and does not return anything if value is not available

set_c = {4, 6, 8, 12, 50, 70}
set_c.discard(50)
print("set_c :", set_c) # {4, 70, 6, 8, 12}

# remove non-existing value
set_c.discard(100)
print("set_c :", set_c)  # {4, 70, 6, 8, 12}

print("_"*50)
######################
# union method :  this method combine two sets data
#union it generates a new set

set_A = {3, 5, 7}
set_B = {'a', 'b', 'c'}

set_C =  set_A.union(set_B)
print("set_c :", set_C)
# {3, 'b', 5, 7, 'c', 'a'}


print("_"*50)
######################
# update method :  this method update one sets data to another set
#here if we want to update existing set - then update

set_x = {3, 5, 7}
set_y = {'a', 'b', 'c'}
set_y.update(set_x)
print("set_y :", set_y)  # {'a', 3, 5, 7, 'c', 'b'}

# result = set_x  + set_y #concatenation is not possible
# print(result)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

print("_"*50)
######################
# difference method :  this method return the difference values from one set to another

set_x = {3, 5, 7, 'a', 'b'}
set_y = {'a', 'b', 'c', 'p', 'q'}
result1 = set_x.difference(set_y)
print("result x to y :", result1)  # {3, 5, 7}


result2 = set_y.difference(set_x)
print("result y to x :", result2)  # {'q', 'p', 'c'}

print("_"*50)
######################
# symmetric difference method :  this method return the difference values from both sets

set_p = {3, 5, 7, 'a', 'b'}
set_q = {'a', 'b', 'c', 'p', 'q'}

result = set_p.symmetric_difference(set_q)
print("result :", result)  # {3, 'c', 5, 'q', 7, 'p'}

print("_"*50)
######################
# intersection method :  this method return the common values from both sets

set_p = {3, 5, 7, 'a', 'b'}
set_q = {'a', 'b', 'c', 'p', 'q'}

result_intersect = set_p.intersection(set_q)
print("result_intersect :", result_intersect)  # {'a', 'b'}

# conversion from set to list
set_5 = {6, 8, 90, 21}
list5 = list(set_5)
print("list5 :", list5) # [8, 90, 21, 6]

print(dir(set)) # to know the methods used for a data type
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'