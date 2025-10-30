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
print(list3[0:5])
print(list3[5:9:1])
print(list3[::-1])
print(list3[::1])


# Append Method - add value in list at the end

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

#list with concationation
l8 =[4,6,7,9]
l9=[6,7,3,1]
l10= l8+l9
print(l10)

#Remove Method
l11= [4,6,8,1,3,5]
l11.remove(5)
print(l11)

#POP Method - default start value is -1
list_c =[3,5,7,9]
v1= list_c.pop()
print(v1)
print(list_c)

#with index position
list_d =[5,3,8,9]
v2=list_d.pop(3)
print(v2)
print(list_d)

#clear method : clear all the list
list_1 = [5,6,7,8]
list_1.clear()
print(list_1)

#Copy method : Shallow Method - changes will reflect in all list

list_d =[5,7,9]
list_e =list_d

list_d.append(100)
list_e.append(200)

print(list_d)
print(list_e)

#Copy method : Deep Method - changes will reflect listwise

list_f =[5,7,9]
list_g =list_f.copy()

list_f.append('d')
list_g.append(200)

print(list_f)
print(list_g)


#Sort method
#Ascending order
list_2 =['a','z','c']

list_2.sort()
print(list_2)

#dscending order
list_2 =['a','z','c']

list_2.sort(reverse=True)
print(list_2)

#Reverse Method

list_3 =[200,30,23,77,93]
list_3.reverse()
print(list_3)

# write a program to get all the evn numbers

list_4 =[22,55,66,32,54]
output =[]

for val in list_4:
    if val%2==0:
        output.append(val)
    else:
        continue
print(output)

# write a program to get all the even numbers with list comphersion

list_5 =[22,55,66,32,54]
output = [val for val in list_5 if val%2==0]
print(output)

# write a program to get required output list
list_6 =[22,5,6,9,54]
output =[]
for val in list_6:
    if val%2==0:
        output.append((val, 'Odd'))
    else:
        output.append((val, 'even'))

print(output)

# write a program to get required output with list comphersion

list_7 =[3,6,10,4]
output = [(val, 'odd') if val%2==0 else (val,'even') for val in list_7]
print (output)

