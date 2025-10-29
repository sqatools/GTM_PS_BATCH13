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
print("-"*40)
## sort method :#############
l1=[100,40,700,30]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
print("-"*40)
############################### reverse method : this method reverse entire list
l1=[100,40,700,30,'Java','python']
l1.reverse()
print(l1)
print("-"*40)
###############################
# solve above program to with list comprehension
l2=[2,4,8,9,4,6,3]

for i in l2:
    if i % 2==0:
        print('even number:',i)
    else:
        print('odd number:',i)
print("-"*40)
Value=[i for i in l2 if i%2==0]
print('even number:',Value)
print("_"*50)
####################################################
# write a python program to get all the required output values from list.
#output = [(4, 'even'), (7, 'odd'), (9, 'odd'), (12, 'even')]
l4=[4,7,9,12]
output=[]
for i in l4:
    if i%2==0:
        output.append((i,'even'))
    else:
        output.append((i,'Odd'))
print('values:',output)
# solve above program with list comp.
output=[(i,'even')if i%2==0 else(i,'odd')for i in l4]
print('values:',output)
print("_"*50)
####################################################





###############################






