list1=[1,4,[3,4],{6,7,9},'hello',True,(7,9,8),6.8,{'a':123},5]
print(list1)
print(list1[2])
print(list1[4])
print(list1[7])

################## List method ############
## Append method##
list1=[1,2,3,4]
list1.append(5)
print(list1)

###### Insert method ###########
list2=[34,89,40,34]
list2.insert(1,90)
print(list2)

##### Extend method ##########
l1=[1,2,3,4]
l2=[5,6,7,8]
l1.extend(l2)
print(l1)
print(l2)

## for string ####
str1="hello"
l3=[1,2,3,4]
l3.extend(str1)
print(l3)


### for set ##
set1={2,2,5,8}
l4=[9,5,8,2]
l4.extend(set1)
print(l4)

