# write prg to get max, min and sum of list values

list1 = [45, 102, 89, 56.5, 19]
print("MAx value :", max(list1))
print("Min value :", min(list1))
print("Sum of list :", sum(list1))

#Write a loop to get the max / min

list2 = [4, 12, 79, 55.5, 10]
max_val = 0
for val in list2:
    if val>max_val: # 4>0 | 12>0 | 79>0 |55.5>0 | 10> 0
        max_Val = val # 4,12,79,
    else:
        continue
print("output :", max_Val) # output = 79

print("_"*50)

# Write a prg. to remove duplicate words from given list

list2 = ['rahul', 'preeti', 'partha', 'arun', 'rahul', 'preeti']
result2 = []
for word in list2:
    if word not in result2:
        result2.append(word)
    else:
        continue
print("unique list names :", result2)

print("_"*50)

# Write a prg to move all positive values in left side and negative in right side

list3 = [8, -14, 15, -16, -9, 24]
# output  = [8 15, 24 ,-14, -16, -9] Split in 2 lists and then merge
pos_list = []
neg_list = []
for val in list3:
    if val > 0:
        pos_list.append(val)
    else:
        neg_list.append(val)
result = pos_list + neg_list
print(result)

print("_"*50)

# Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”

str1 = 'programming'
st2 = " "
for char in str1:
    if char in st2:
        st2 = st2 + '$'
    else:
        st2 = st2 + char
print("Revised string :", st2)
print("_"*50)

# Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”

