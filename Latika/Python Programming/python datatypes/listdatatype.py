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