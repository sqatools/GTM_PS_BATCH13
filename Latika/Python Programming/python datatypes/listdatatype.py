"""
properties
List is mutable datatypes
List can contain any types of data
e.g. int,float,string,complex,tuple,list,boolean,dict,set
List follows positive and negetive indexing
List contain value in square bracket
"""

#loop to get value without indexing

list2=['a','b','c',10,20,30]
for val in list2:
    print(val)
print("."*100)
# loop to get value with indexing
list_len = len(list2)
for i in range(list_len):
    print(i,list2[i])

for i in range(-list_len,0,1):
    print(i,list2[i])

################################################Slicing Method####################################
print("."*100)
list3=[5,8,9,10,'a','t','i']
print(list3[0:5])
print(list3[-5:-10:-1])
print(list3[5:9])

#................................................................................................#

"""
List Methods - 
1. Append() - This method add value to the list at the end.
2. insert() - This method insert data at specific index position
3. Extend() - This method add on list data to another list
"""
#append
list4=[5,7,8,2,3]
list4.append(50)
print(list4)
print("."*100)
print()

#insert
list5=[8,9,10,4,7,12]
list5.insert(2,100)
print(list5)

print()

list6=['Python','Hello','Learning',4,7]
list6.insert(3,'programming')
print(list6)
print("."*100)
print()

#extend

l1=[4,7,9]
l2=['a','b','c']
l2.extend(l1)
print("L2 list is" , l2)
print("L1 list is " ,l1)

str='hello'
l3=[1,2,3]
l3.extend((str))
print(l3)
print()
#remove method : remove any specific value from list

list_a=[6,7,9,45]
list_a.remove(9)
print(list_a)

# pop method : This method remove values from list using index position.
# default index position is -1
# This method return the removed value that we can stored in a variable

list_b=[6,3,9,6,5]
v1=list_b.pop()
print("pop value v1 is :",v1)
print(list_b)

# remove from specific index
v2=list_b.pop(2)
print("pop value v2 is :",v2)
print(list_b)

print("_"*50)
##########################################################
# remove method :  remove any specific value from list

list_b = [6, 7, 9, 2, 45]
list_b.remove(9)
print("list_b :", list_b)  # list_b : [6, 7, 2, 45]

print("_"*50)
##########################################################
# pop method :  this method remove value from list using index position.
#              ->  default index position is -1
#              -> This method return the removed value, that we can store in a variable

list_c=  [5, 7, 2, 15, 18]

# remove default index -1
v1 = list_c.pop()
print("removed value :", v1)  # 18
print("list_c :", list_c)  # [5, 7, 2, 15]

# remove from specific index
v2 = list_c.pop(1)
print("removed value :", v2) # 7
print("list_c :", list_c) # [5, 2, 15]


print("_"*50)
##########################################################
# clear method : clear all data from list

list1 = [5, 7, 9, 2]
list1.clear()
print("list1 :", list1) # list1 : []

print("_"*50)
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


print("_"*50)
# Deep Copy: In this concept we have to copy method to create a of list, and if we will do modification in any of the list
# then changes will not reflect in another list.

list_x = ['a', 'b', 'c']
list_y = list_x.copy()
list_x.append('d')
list_y.append(100)
print("list_x :", list_x) # ['a', 'b', 'c', 'd']
print("list_y :", list_y) # ['a', 'b', 'c', 100]

#############################################################################################################

# sort method
# Ascending
list1 =[3,9,6,10,20]
list1.sort()
print("Sorted list is : ",list1)

print()
# Descending
list2=[9,1,3,89,20]
list1.sort(reverse=True)
print("Descending list is: ",list1)

#######################################################################################################################
print()
# reversed method
# This method reverse the entire list

list_x=[3,8,9,12,'python','java','c#']
list_x.reverse()
print("reverse list is:", list_x)
