

################# Max,min,sum of values ##################
list1 = [1,7,9,22,6,17]

print("max value :",max(list1))
print("min value:",min(list1))
print("sum of the value:",sum(list1))

###############################################
# write a python program to find max value without inbuilt function.
list1 =[5,7,9,19,80,3]
max_val = 0 # start with first element
for val in list1:
    if val> max_val: # 5> 0/ 7>5/9>7
       max_val =val # 5,7,9 ....
else:
    'continue'

print("output:",max_val)

##########################################

# write a python program to remove duplicate values from list
list2 = ["Arun","Rahul","Preethi","Arun"]
result2 = []
for val in list2:
    if val not in result2:
        result2.append(val)
    else:
        continue
print("result2:",result2)

print("_"*50)

#remove duplicate values with conversion
var3 = set(list2)
print(var3)
print(list(var3))

("_"*50)
#3 Write a program to move all postive values at left side and negative values in right side
list3 =[4,8,-10,-4,-6,8,6]
pos_list=[]
neg_list=[]

for val in list3:
    if val > 0:
        pos_list.append(val)
    else:
        neg_list.append(val)
result2= pos_list + neg_list
print("result2:",result2)
pos_list.extend(neg_list)

print("result:",pos_list)

##########################################
# sorted function

#increasing order
list2 = [6,8,9,2,1,7]
result2 =list(sorted(list2))
print("sorted result:",result2)

#Descreasing order
result4 =list(sorted(list2,reverse=True))
print("decreasing result:",result4)


