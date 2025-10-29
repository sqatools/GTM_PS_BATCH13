# 1.  write a python program to get max value from list without using inbuilt function.
list1 = [5, 7, 9,  23, 80,  56]
max_value = 0
for val in list1:
    if val > max_value: # 5 > 0 | 7 > 5 | 9> 7 | 23 > 9 | 80 > 23 | 56 > 80
        max_value = val # 5, 7, 9, 23 ... 80
    else:
        continue

print("output :", max_value)
# output : 80


print("_"*50)
# 2. write a python program to remove duplicate values from list
list2 = ["Preeti", "Rahul", "Preeti",  "Anil", "Mohan", "sangeetha"]
result2 = []

for val in list2: # Rohit
    if val not in result2:
        result2.append(val)
    else:
        continue

print("result2 :", result2)

# remove duplicate values with conversion
var3 = set(list2)
print(var3)
print(list(var3))


print("_"*50)
# 3. write a python program to move all positive value in left side and negative values in right side.
list3 = [1, 7, -9, 2, -50, 20, -90]
pos_list = []
neg_list = []

for val in list3:
    if val > 0:
        pos_list.append(val)
    else:
        neg_list.append(val)


result = pos_list + neg_list
print("result :", result)

pos_list.extend(neg_list)
print("result2 :", pos_list)
