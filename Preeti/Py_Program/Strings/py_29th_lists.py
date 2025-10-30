list1=[8,3,9,4,5,10]
max_value=0
for val in list1:
    if val > max_value:
        max_value=val
    else:
        continue
print(max_value)

## max , min, sum of values
print(max(list1))
print(min(list1))
print(sum (list1))
print(len(list1))
print(sorted(list1))


# write a python program to remove duplicate values from list
list2 = ["Rohit", "Rahul", "Rohan",  "Ravi", "Rahul", "Rohit"]
result=[]
for val in list2:
    if val not in result:
        result.append(val)
    else:
        continue
    print(val)


 # write a python program to move all positive value in left side and negative values in right side.
list3 = [5, 8, -9, 2, -30, 10, -60]
# output = [5, 8, 2, 10, -9, -30, -60]
pos_list=[]
neg_list=[]
for val in list3:
    if val>0:
        pos_list.append(val)
    else:
        neg_list.append(val)
result=pos_list+neg_list
print(result)


## Increasing order
list2 = [6, 8, 9, 2, 1]
result2 = list(sorted(list2))  # [1, 2, 6, 8, 9]
print("sorted result :", result2)

# Decreasing order
result4 = list(sorted(list2, reverse=True))  # [9, 8, 6, 2, 1]
print("decreasing sorted result :", result4)

# reversed function
result3 = list(reversed(list2))
print("result3 :", result3)  # [1, 2, 9, 8, 6]

