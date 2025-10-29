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

# write a python program to remove duplicate values from list
list2 = ["Rohit", "Rahul", "Rohan",  "Ravi", "Rahul", "Rohit"]
result=[]
for val in list2:
    if val not in result:
        result.append(val)
    else:
        continue
    print(val)


