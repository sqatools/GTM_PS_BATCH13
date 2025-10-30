print('*'*50+"Program 1 - Square List"+'*'*50)

list1 = [5, 7, 9, 23, 80, 56]
list2 = []
for val in list1:
    list2.append((val*val))
print(list2)

print('*'*50+"Program 2 - Combine List"+'*'*50)
list1 = [5, 7, 9, 23, 80, 56]
list2 = [10, 7, 4, 33, 66, -19]
list2.extend(list1)
print(list2)

print('*'*50+"Program 3 - Sum of List"+'*'*50)
list1 = [5, 7, 9, 23, 80, 56]
print("Sum of list is: ",sum(list1))

print('*'*50+"Program 4 - Product of List"+'*'*50)
list1 = [5, 7, 9, 23, 0, 80, 56, 10, -1]
mult = 1
for val in list1:
    if val != 0:
        mult*=val
    else:
        continue
print("Product of list is: ",mult)

print('*'*50+"Program 5 - Min & Max of a List"+'*'*50)
list1 = [5, 7, 9, 23, 0, 80, 56, 10, -1]
print("The Max value in the list is: ", max(list1))
print("The Min value in the list is: ", min(list1))

print('*'*50+"Program 6 - Separate Odd & even from a List"+'*'*50)
list1 = [5, 7, 9, 34.98, 23, 0, "roger", 80, 56, 10, -1, 'abc']
odd_list =[]
even_list = []
for val in list1:
    if type(val) == int and val % 2 == 0:
        even_list.append(val)
    elif type(val) == int and val % 2 != 0:
        odd_list.append(val)
    else:
        continue
print("The even list is: ", sorted(even_list))
print("The odd list is: ", sorted(odd_list))

print('*'*50+"Program 7 - Remove duplicates from a List"+'*'*50)
list1 = [5, 7, 23, 9, 23, 80, 56]
list2 = []
for val in list1:
    if val not in list2:
        list2.append(val)
print(list2)

print('*'*50+"Program 8 - Remove duplicates from a List"+'*'*50)
list1 = [5, 7, 23, 9, 23, 80, 56]
list2 = []
for val in list1:
    if val not in list2:
        list2.append(val)
print(list2)
