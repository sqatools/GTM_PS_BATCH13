######### Remove method##########
list1=[4,8,9,3.0]
list1.remove(8)
print(list1)

########## pop method #############
list2=[2,8,4,9,5,4]
v1=list2.pop()
v2=list2.pop(1)
print(v1)
print(v2)
print(list2)

############ clear method #########
list3=[9,4,3,8]
list3.clear()
print(list3)

############ shallow copy ##########
list_a=[4,7,9,23]
list_b=list_a
list_a.append(8)
list_b.append(10)
print(list_a)
print(list_b)

############## deep copy ##########
list_x=['a','b','c','d']
list_y=list_x.copy()
list_x.append('e')
list_y.append(100)
print(list_x)
print(list_y)

###### sort #########
list1=[3,8,9,2,1,0,4,5]
