# 1.  write a python program to get max value from list without using inbuilt function.
list1=[5,7,9,23,80,56]
max_value = 0
for val in list1:
    if val > max_value: # 5 > 0 | 7 > 5 | 9> 7 | 23 > 9 | 80 > 23 | 56 > 80
        max_value = val # 5, 7, 9, 23 ... 80
    else:
        continue

print("output :", max_value)
# output : 80


print("_"*50)
###2nd list [2,5,90,80,100]
list2=[2,8,90,80,100]
mx_value = 0
for Val1 in list2:
    if Val1 > mx_value:
        mx_value = Val1
    else:
        continue

print("output:", mx_value)

# 2. write a python program to remove duplicate values from list
list2 = ["Rohit", "Rahul", "Rohan",  "Ravi", "Rahul", "Rohit"]
result2 = [] # ["Rohit", "Rahul"]

for val in list2: # Rohit
    if val not in result2:
        result2.append(val)
    else:
        continue



print("result2 :", result2) # ['Rohit', 'Rahul', 'Rohan', 'Ravi']

######2nd list3['Arun','Anil','Amit', 'Amol','Anil','Amol']

list3 = ['Arun','Anil','Amit', 'Amol','Anil','Amol']
result3 = []
for val in list3:
    if val not in result3:
        result3.append(val)
    else:
        continue

print("result3 :", result3)


# remove duplicate values with conversion
var3 = set(list2)
print(var3)  # {'Rohan', 'Rahul', 'Ravi', 'Rohit'}
print(list(var3))  # ['Rohan', 'Rahul', 'Ravi', 'Rohit']

print("_"*50)

### 2nd list3 = ['Arun','Anil','Amit', 'Amol','Anil','Amol']
var4= set(list3)
print(var4)
print(list(var4))
print("_"*50)



