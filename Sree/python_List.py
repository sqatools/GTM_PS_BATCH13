# remove method :  remove any specific value from list
list1=[4,4,6,8,9,10]
list1.remove(8)
print('value1:',list1)
print("-"*40)
#######################################
list2= [47,37,98,23]
list2.pop(0)
print('value2',list2)
print("-"*40)
#  default index position is -1, if we don't mention
list2.pop()
print('value3:',list2)
print("-"*40)
######################################
list2.clear()
print('value4:',list2)
print("-"*40)
######################################Shallow copy#####
list3=[1,3,5,6,8]
list4=list3
list3.append(20)
list4.append(44)
print(list3)
print(list4)
print("-"*40)
# Deep Copy#################
list4=list3.copy()
list4.append(800)
list3.append(500)
print(list3)
print(list4)
