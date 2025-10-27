str9 = input("Enter a string: ")
counter = 0
vowels = 'aeiouAEIOU'
for char in str9:
    if char not in vowels:
        counter += 1
    else:
        continue
print(" The total number of consonants in the input string is:", counter)

print('*'*50,"List Datatype in Python",'*'*50)

list1 = [2,3.14,]
list2 = [6,9,8,'y']
print(list1)
print(list2)
list1.append(1)
list2.extend(list2)
print(list2)
list1.extend(list2)
print(list1)
list1.extend(list2)
print(list1)