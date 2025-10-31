from itertools import combinations

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

print('*'*50+"Program 8 - List of 2 numbers whose sum is 10"+'*'*50)
list1 = [0, 1, 2, 3, 4, 5, 7, 9, 10, 23, 80, 56]
list2 = []
list3 = []
list4 = []
for val in list1:
    if val<=10:
        list2.append(val)
list3 = tuple(combinations(list2, 2))
for val in list3:
    if sum(val) == 10:
        list4.append(val)
print(list4)

print('*'*50+"Program 9 - List of Squares for all even numbers in a list"+'*'*50)
list1 = [0, 1, 2, 3, 4, 5, 7, 9, 10, 23, 80, 56]
list2 = []
for val in list1:
    if val%2 == 0:
        list2.append(pow(val,2))
print(sorted(list2))

print('*'*50+"Program 10 - Left Odds, Right evens"+'*'*50)
list1 = [0, 1, 2, 3, 4, 5, 7, 9, 10, 23, 80, 56]
list2 = []
list3 = []
for val in list1:
    if val%2 == 0:
        list2.append(val)
    elif val%2 != 0:
        list3.append(val)
list4 = sorted(list2)
list5 = sorted(list3)
list5.extend(list4)
print(list5)

print('*'*50+"Program 11 - Common Items"+'*'*50)
list1 = [0, 1, 2, 3, 4, 5, 7, 9, 10, 23, 80, 56]
list2 = [13, 5, 7, 9, 10, 44, 67]
list3 = []
for val in list1:
    if val in list2:
        list3.append(val)
    else:
        continue
print(list3)

print('*'*50+"Program 12 - Reverse a list with for loop"+'*'*50)
list1 = [0, 1, 2, 3, 4, 5, 7, 9, 10, 23, 80, 56]
for i in range(len(list1)-1, -1, -1):
   print(list1[i], end=' ')