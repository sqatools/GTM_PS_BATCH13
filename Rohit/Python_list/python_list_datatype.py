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
print(list1[-4]) # (5, 6, 7)
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
print(list3[0:5:1]) #[1, 2, 3, 4, 5]
print(list3[-1:-5:-1]) #['d', 'c', 'b', 'a']
print(list3[-5:-10:-1]) #[5, 4, 3, 2, 1]
print(list3[-3:-7:-1]) # ['b', 'a', 5, 4]
print(list3[::-1]) # ['d', 'c', 'b', 'a', 5, 4, 3, 2, 1]
print(list3[::1]) # [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']

print("-"*50)
################################### list methods #############################
# Append method :  This method add value to the list at the end.
list4 = [22,33,56,77]
list4.append(90)
print(list4)  # [22, 33, 56, 77, 90]

list4.append(99) # [22, 33, 56, 77, 90, 99]
print(list4)

str = ["Hello", "guys" ,"Good"]
str.append("Morning")
print(str) # ['Hello', 'guys', 'Good', 'Morning']

print("-"*50)
########################################################
# insert method :  this method insert data at specific index position.
list5 = [8,9,13,17]
list5.insert(2,77)
print("show inserted list in list5:",list5) # [8, 9, 77, 13, 17]

list7 = ['I', 'am', 'going',' city', 41, 88]
list7.insert(3,'karad')
print("list7 :",list7) # ['I', 'am', 'going', 'karad', ' city', 41, 88]

list8 = ['Hello', 'Guys', 'good', 'morning']
list8.insert(2,'very')
print("list8 :",list8) # ['Hello', 'Guys', 'very', 'good', 'morning']

print("-"*50)
########################################################
# extend method : this method add one list data to another list
l1 = [7,9,11]
l2 = ['x','y','z']
l2.extend(l1)
print("result of l2 :",l2) # ['x', 'y', 'z', 7, 9, 11]
print("l1 :",l1) # [7, 9, 11]

print("-"*50)

l1.extend(l2)
print("result of l1 :", l1) # [7, 9, 11, 'x', 'y', 'z']
print("l2 :",l2) # ['x', 'y', 'z']

print("-"*50)

str1 = "Hello Guys"
l3 = [22,55,77]
l3.extend(str1)
print("result of l3 :",l3) # [22, 55, 77, 'H', 'e', 'l', 'l', 'o', ' ', 'G', 'u', 'y', 's']
# When we will have a string then each character will get display

print("-"*50)

set1 = {2,6,8,2}
l4 = ['a','b','c']
l4.extend(set1)
print("output of l4 :",l4) # ['a', 'b', 'c', 8, 2, 6]

print("-"*50)
###########################################################
# list concatenation:
l9 = [1,2,3]
l10 = [4,5,6]
l11 = l9+l10
print("l11:",l11)

l7 = ['a','b','c','d']
l8 = ['M','N','T','Z']
l13= l7+l8
print("result of l13 :",l13) # ['a', 'b', 'c', 'd', 'M', 'N', 'T', 'Z']

print("-"*50)
###########################################################
# remove method :  remove any specific value from list
list1 = [2,4,9,10,11]
list1.remove(9)
print("list1 :", list1) # [2, 4, 10, 11]

list1.remove(4)
print("list1 :", list1) # [2, 10, 11]

print("-"*50)
###########################################################
# pop method :  this method remove value from list using index position.
#              ->  default index position is -1
#              -> This method return the removed value, that we can store in a variable

list_a = [33,22,23,11,55]

# remove default index -1
v1=list_a.pop()
print("Removed value :",v1) # 55
print("list_a :",list_a) # [33, 22, 23, 11]

# remove from specific index
v2 =list_a.pop(2)
print("Removed value :",v2) # 23
print("list_a :",list_a)  # [33, 22, 11]

print("-"*50)
##################################################################
# clear method : clear all data from list
list3 = [1,2,4,55,67]
list3.clear()
print("list3 :",list3)

list4 = [33,55,'a',77,'t']
list4.clear()
print("list4 :",list4)
print("-"*50)
############################################################
# copy() method:

# Shallow copy: when we assign one list to another list, and modify any value in both the list
# then changes will reflect in both lists.

list5 = [1,4,6,9]
list_e = list5
#print(list_e)
#print(list5)
list_e.append(199)
list5.append(100)
print("list_e :", list_e)  # [1, 4, 6, 9, 199, 100]
print("list5 :", list5)   # [1, 4, 6, 9, 199, 100]

print("-"*50)

# Deep Copy: In this concept we have to copy method to create a of list, and if we will do modification in any of the list
# then changes will not reflect in another list.

list_a = [33,76,'a',99,'b']
y = list_a.copy()
#print(y)
#print(list_a)
y.append(100)
list_a.append(200)
print("y :",y)
print("list_a :", list_a)

##y : [33, 76, 'a', 99, 'b', 100]
##list_a : [33, 76, 'a', 99, 'b', 200]

print("-"*50)
###############################################################
# sort method :
list1= [2,1,0,99,77,65]
# sort in ascending order
list1.sort()
print("list1 Ascending order :",list1)
# list1 Ascending order : [0, 1, 2, 65, 77, 99]

# sort in descending order
list1.sort(reverse=True)
print("list1 Descending order :", list1)
#list1 Descending order : [99, 77, 65, 2, 1, 0]

print("-"*50)

list_a = ['c','a','d','b']
list_a.sort()
print("list_a Ascending order :",list_a)
# list_a Ascending order : ['a', 'b', 'c', 'd']

list_a.sort(reverse=True)
print("list_a descending order :", list_a)
# list_a descending order : ['d', 'c', 'b', 'a']

print("-"*50)
###########################################################
# reverse method : this method reverse entire list
list_x = [5, 7, 9, 23, 4, 78, 'Hello', 'Python']
list_x.reverse()
print("list_x :",list_x)
# ['Python', 'Hello', 78, 4, 23, 9, 7, 5]

list_z = ['Rohit','chavan','karad','city','satara']
list_z.reverse()
print("list_z :",list_z)
#['satara', 'city', 'karad', 'chavan', 'Rohit']

print("-"*50)
###########################################################
# write a python program to get all the even values from list
list1 = [2,7,8,10,11]
output= []
for val in list1:
    if val%2==0:
        output.append(val)
    else:
         continue

print("output :",output)  # output : [2, 8, 10]

print("-"*50)

# solve above program to with list comprehension
result=[val for val in list1 if val%2==0 ]
print("result :",result) # [2, 8, 10]

print("-"*50)
###################################################################
# write a python program to get all the required output values from list
list2 = [2,5,12,17]
output = []
for val in list2:
    if val%2==0:
        output.append((val,'even'))
    else :
        output.append((val,'odd'))

print("output :",output)
# [(2, 'even'), (5, 'odd'), (12, 'even'), (17, 'odd')]

# solve above program to with list comprehension:
result1 = [(val,'even') if val%2==0 else (val,'odd') for val in list2]
print("result1 :",result1)
# [(2, 'even'), (5, 'odd'), (12, 'even'), (17, 'odd')]

##display only even and odd for numbers
result2 = [('even') if val%2==0 else ('odd') for val in list2]
print("result2 :", result2)
#['even', 'odd', 'even', 'odd']

##Square and cube
result3 =[val**2 if val%2==0 else val**3 for val in list2]
print("result3 :",result3)
# [4, 125, 144, 4913]

print("_"*50)
######################################################################
# sorted function.

# Increasing order
list2 = [6, 8, 9, 2, 1]
result2 = sorted(list2)
print(result2) # [1, 2, 6, 8, 9]

result3 = list(sorted(list2))
print(result3) # [1, 2, 6, 8, 9]

# Decreasing order
result4 = sorted(list2,reverse=True)
print("decreasing sorted result :",result4) # [9, 8, 6, 2, 1]

result5 = list(sorted(list2,reverse=True))
print("decreasing sorted result :",result5) # [9, 8, 6, 2, 1]

# reversed function :
result6 = list(reversed(list2))
print(result6) # [1, 2, 9, 8, 6]