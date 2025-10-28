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
