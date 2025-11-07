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

print("list_e :", list_e) #list_e : [4, 7, 9, 23, 100, 200]
print("list_d :", list_d) #list_d : [4, 7, 9, 23, 100, 200]

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
list2.sort(reverse=True)  #default value for reverse = False
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