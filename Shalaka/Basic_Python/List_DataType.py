list1= [3,30,'Hello',(5,6,7),[23,30,77], {'a':30},{3,4,92},True]
print(list1)
print (list1, type[list1])
print(list1[2])
print(list1[-3])
print(list1[4])
print(list1[4] [2])

list2 =['a''b','c',10,30,23]
print(list2)
for val in list2:
    print(val)
#list with indexing
list_len = len(list2)
for i in range(list_len):
    print(i,list2[i])

#list slicing
list3 =[6,7,8,1,'a','b','c','d']



#List Methods
# Append Method - add valun in list at the end

l1 = [5,6,7,8]
print('before append :', l1)
l1.append(23)
print('after append :', l1)

# Inert Method - insert data at any specific index position
l2 =[3,5,6,8,9]
print('before insert :', l2)
l2.insert(2,67)
print('after insert :', l2)

l3 =['hello','world',2,4,6,8]
print('before insert :', l3)
l3.insert(2,'nice')
print('after insert :', l3)


#Extend method - add one list data to another list

l4 = [4,7,9,10]
l5= ['g','t','o']
l5.extend(l4)
print(l5)

#list with string

str1 = ['hello','good','Morning']
l6 =['2',5,9]
l6.extend(str1)
print(l6)

#list with set

set1 = { 45,89,20}
l7=['r','y','i']
l7.extend(set1)
print(l7)
