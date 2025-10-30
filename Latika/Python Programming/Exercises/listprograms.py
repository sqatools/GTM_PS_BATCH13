# Max, Min, Sum

list1=[4,8,7,10,2,11]

print("Max value is:",max(list1))
print("Min value is:",min(list1))
print("Sum of :",sum(list1))

#...............................................................................................................................

print()
print("."*100)

print("Write a program to get max values from list without using inbuilt functions")
list2=[5,7,9,23,56,99,12]
max_val=0

for val in list2:
    if val > max_val:
        max_val = val
    else:
        continue
print("Max value is :",max_val)

#....................................................................................
print()
print("."*100)
print("Write a program to remove duplicates from list")

list3=["Latika","Shalaka","Sweety","Latika","Sweety","Sadhna","Shalaka"]
result=[]

for val in list3:
    if val not in result:
        result.append(val)
    else:
        continue
print("After remove the duplicates :",result)

#..................................................................................
print()
print("."*100)
print("Write a python program to move all positive value in left side and negetive values in right side")

list4=[4,-2,8,-10,33,5,-1]
pos_list=[]
neg_list=[]

for val in  list4:
    if val >0:
        pos_list.append(val)
    else:
        neg_list.append(val)
result=pos_list+neg_list
print("result is :",result)

#..................................................................................
print()
print("."*100)

#sorted function - dosenot modify the list

list5=[6,8,10,3,2]
result=list(sorted(list5))
print("increasing sorted order",result)

result=list(sorted(list5,reverse=True))
print("decreasing sorted order",result)













