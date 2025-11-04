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
#Remove duplicate values from the list
l5=['Ram','Ramesh','Ravi','Ram','Ravi']
result=[]
for i in l5:
    if i not in result:
        result.append(i)
    else:
            continue
print(result)
print("_"*50)

# remove duplicate values with conversion

result2=list(set(l5))
print(result2)
print("_"*50)
####################################################
#  write a python program to get max value from list without using inbuilt function.
l6=[22,55,99,100,4,200]
max_val=0
for i in l6:
    if i> max_val:
        max_val=i
    else:
        continue
print(max_val)
print("_"*50)
####################################################
## write a python program to move all positive value in left side and negative values in right side.

l7=[9,10,33,6,-2,-5,-7,-10]
positive_val=[]
negative_val=[]
for i in l7:
    if i > 0:
        positive_val.append(i)
    else:
        negative_val.append(i)
print(positive_val+negative_val)
##  or #######
positive_val.extend(negative_val)
print(positive_val)
print("_"*50)
##Python program to calculate the square of each number from the given list.#################
l8=[2,4,8,6]
for i in l8:
    print('square value:',i,':',i**2)
print("_"*50)
############################################
## Python program to combine two lists.'
l8=[1,2,3,4,4,]
l2=[0,9,8,7,6,]
l8.extend(l2)
print(l8)  ## or#######
x=l8+l2
print(x)
print("_"*50)
## Python program to calculate the sum of all elements from a list

l3=[5,6,7,8,8,4]
print(sum(l3))
  ##  or
l3=[5,6,7,8,8,4]
x=0
for i in l3:
  x +=i
print('sum of the value:',x)
print("_"*50)
###########################################
##Python program to find the minimum and maximum elements from the list.
l3=[66,55,44,33,90]
x=0
for i in l3:
    if i > x:
        x=i
    else:
        continue
print('Max number',x)
##  or##
print(max(l3))
print("_"*50)
print("minnumber",min(l3))
print("_"*50)
###########################################
## Python program to find a product of all elements from a given list.

l2=[3,3,6,7,5]
X=1
for i in l2:
    if i >x:
        x *=i
print(x)
print('_____'*40)
######################################
l1=[4,6,9,22,90,86,109]
x=0
for i in l1:
    if i > x:
        x=i
    else:
        continue
print('max val:',x)



