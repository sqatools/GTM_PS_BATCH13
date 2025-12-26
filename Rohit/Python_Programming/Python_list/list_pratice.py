# 1.  write a python program to get max value from list without using inbuilt function.

list1 = [22,67,45,89,77,23]
max_val = 0
for val in list1:
    if val >max_val:
        max_val = val
    else:
        continue
print("Print max_value :",max_val)  # Print max_value : 89

print("-"*50)

#2. write a python program to remove duplicate values from list
list2 = ["Rohit", "Rahul", "Rohan",  "Ravi", "Rahul", "Rohit"]
dup_value = []
for val in list2:
    if val not in dup_value:
        dup_value.append(val)
    else:
        continue
print("Duplicated values removed :",dup_value)

print("_"*50)

# 3. write a python program to move all positive value in left side and negative values in right side.
list3 = [5, 8, -9, 2, -30, 10, -60]
post_value = []
neg_value =[]
for val in list3:
    if val > 0:
        post_value.append(val)
    else:
        neg_value.append(val)

#post_value.extend(neg_value)
result = post_value + neg_value
print("Display Positive & Negative values :", result)
#print("post_value :", post_value)

