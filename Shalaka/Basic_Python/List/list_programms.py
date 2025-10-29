#.1 Get the max value from list without using inbuild function
list1 =[4,5,90,34,23,30]
max_val =0
for val in list1:
    if val > max_val:
        max_val=val
    else:
        continue
print(max_val)

#2. Rempved duplicate
list2 =['shalaka','john','shalaka','Hello']
result2 =[]
for val in list2:
    if val not in result2:
        result2.append(val)
    else:
        continue
print(result2)


#.3 Move all positive no to left and negative no to right side
list3 =[-2,4,-5,-6,3,6]
positive_list =[]
negative_list =[]
for val in list3:
    if val>=0:
        positive_list.append(val)
    else:
        negative_list.append(val)
result3 = positive_list + negative_list
print(result3)


print('1). Python program to calculate the square of each number from the given list.')

list1 = [2,3,77,92]
for val in list1:
    print(val,':', val**2)

print('2). Python program to combine two lists.')
list2 = [6,3,7]
list3 = [5,2,1,'Shalaka']
result = list2 + list3
print(result)

print('3). Python program to calculate the sum of all elements from a list.')
list4 =[2,3,7,9]
sum = 0

for val in list4:
    sum +=val
print(sum)


print('5). Python program to find the minimum and maximum elements from the list.')
list5 =[4,5,90,34,23,30,78]
maximum = 0
minimum = list5[0]
for val in list5:
    if val > maximum:
        maximum=val
    if val < minimum:
        minimum= val

print(maximum)
print(minimum)

print('6). Python program to differentiate even and odd elements from the given list.')
list6 =[4,5,90,34,23,30,78]
even = []
odd = []
for val in list6:
    if val%2==0:
       even.append(val)
    else:
        odd.append(val)
print(even)
print(odd)



print('7). Python program to remove all duplicate elements from the list.')

list7 =['Hello','john','shalaka','Hello']
result7 =[]
for val in list7:
    if val not in result7:
        result7.append(val)
    else:
        continue
print(result7)

print('8). Python program to print a combination of 2 elements from the list whose sum is 10.')

print('9). Python program to print squares of all even numbers in a list.')

list9 =[4,5,90,34,23,30,78]
even = []
odd = []
for val in list9:
    if val%2==0:
       even.append(val**2)
    else:
        continue
print(even)

print('10). Python program to split the list into two-part, the left side all odd values and the right side all even values.')
list10 =[4,5,7,34,23,30]
even = []
odd = []
for val in list10:
    if val%2==0:
       even.append(val)
    else:
        odd.append(val)
result10 = odd + even
print(result10)

print('11).  Python program to get common elements from two lists.')
list_11 = [4, 5, 7, 9, 2, 1]
list_12 = [2, 5, 8, 3, 4, 7]
elements =[]
for val in list_11:
     if val in list_12:
         elements.append(val)
print(elements)

print('12). Python program to reverse a list with for loop.')
print('13). Python program to reverse a list with a while loop.')
print('14). Python program to reverse a list using index slicing.')

list14 =[3,4,5,6,7]
result14 = list14[::-1]
print(result14)

print('15). Python program to reverse a list with reversed and reverse methods.')
list15 = [11,23,45,67,89]
print(list(reversed(list15)))

print('16). Python program to copy or clone one list to another list.')

list16 = [3,4,5,6,7]
l16 = []

for val in list16:
    l16.append(val)
print('another list :', l16)

print(' 17). Python program to return True if two lists have any common member.')

list17 = [1,2,3,4,5,6]
l17 = [3,2,6,7,1,8]

for val in list17:
    if val in l17:
        print('True')
        break
