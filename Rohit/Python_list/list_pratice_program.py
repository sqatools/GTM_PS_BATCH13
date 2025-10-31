#Python program to combine two lists.
l1 = [1,2,3,4]
l2 = [5,6,7,8]
#1st way output
l1.extend(l2)
print("Result of combine 2 list :",l1) # [1, 2, 3, 4, 5, 6, 7, 8]

# 2nd way out
l3 = l1 + l2
print("l3 :",l3) # [1, 2, 3, 4, 5, 6, 7, 8]

print("-"*50)
####################################################################
#Python program to calculate the square of each number from the given list
l4 = [1,2,3,4]
for val in l4:
    print(val,val**2)
'''    
1 1
2 4
3 9
4 16
'''
print("-"*50)
####################################################################
##Python program to calculate the sum of all elements from a list
list1 = [1,2,3,4,5]
sum = 0
for val in list1:
    sum +=val
    print(sum)
'''
1
3
6
10
15
'''
print("-"*50)
##############################################################
# Python program to find the minimum and maximum elements from the list
list1 = [23,56,12,89]
print("minimum value :",min(list1)) # 12
print("Maximum value :",max(list1)) # 89
print("Minimum & Maximum value :",min(list1),max(list1))  # 12 89

print("-"*50)
##############################################################
##Python program to differentiate even and odd elements from the given list
num = [2,3,7,8,10,17]
for val in num:
 if val%2==0:
    print("Even number :",val)
 elif val%2!=0:
     print("Odd number :",val)

print("-"*50)
###############################################################
#Python program to remove all duplicate elements from the list
list1 = [1,2,5,6,2,5]
list2 = []
for val in list1:
 if val not in list2:
    list2.append(val)

print(list2)   # [1, 2, 5, 6]
print("-"*50)
#############################################################
# Python Problem to remove all the duplicate elements from a list.
list9 = [5,7,8,2,5,0,7,2]
output= []
for val in list9:
    if val not in output:
        output.append(val)
print("output of duplicate :",output)

print('-'*50)
################################################################
#Python program to print squares of all even numbers in a list
list11 = [2,4,7,8,5,1,6]
for val in list11:
    if val%2==0:
        print("Even number :",val**2)
        ##print("Even number :", val, val ** 2)
'''        
Even number : 4
Even number : 16
Even number : 64
Even number : 36
'''
print("_"*50)
#######################################################################
#Python program to split the list into two-part, the left side all
# odd values and the right side all even values.
l1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even = []
odd = []
for val in l1:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(even)  # [2, 8, 12, 22]
print(odd)  # [5, 7, 11, 17, 19]
odd.extend(even)
print(odd)   # [5, 7, 11, 17, 19, 2, 8, 12, 22]

print("-"*50)
#######################################################################
#Problem to print the list in reverse order using for loop
list12 = [1,2,3,4,55]

#list12.reverse()
#print(list12)
#print("*"*23)

#while list12:
  #  print(list12[::-1])  # [55, 4, 3, 2, 1]
   # break

list3 = [5, 7, 9, 2, 15, 17]
output = []
for i in range(-1, -len(list3)-1, -1):
    print(list3[i], end=" ")
    output.append(list3[i])

print("output :", output)

print("_"*50)
############################################################
#Python program to get common elements from two lists
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
common_list = []
for val in list1:
    if val in list2:
        common_list.append(val)
print(common_list)  ## [4, 5, 7, 2]

print("-"*50)
############################################################
#Python program to reverse a list with reversed and reverse methods.
list1 = [2,3,7,9,3,1]
# using reverse methods
#list1.reverse()
#print(list1)  ## [1, 3, 9, 7, 3, 2]

# Using reversed method
result1  = list(reversed(list1))
print(result1)

print("-"*50)
########################################################
#Python program to add 2 lists with extend method.
list1 = [2,4,6,8,1]
list2 = [23,56,11,89]
list1.extend(list2)
print(list1) # [2, 4, 6, 8, 1, 23, 56, 11, 89]

print("-"*50)
########################################################
# Python program to sort list data, with the sort and sorted method.
list11 = [23,11,78,45,33]
# using sort() method
list11.sort()
print(list11)  # [11, 23, 33, 45, 78]

# using sorted() method
print("list11 :",sorted(list11))  # [11, 23, 33, 45, 78]

print("-"*50)
###########################################################
#Python program to remove data from the list from a specific index using the pop method.
list1 = [33,56,89,12,45]
list1.pop(2)
print(list1) # [33, 56, 12, 45]

print("-"*50)
###########################################################
#Python program to reverse each element of the list
list1 = ["Sqa","Tools","Online","Learning","Platform"]
list2 = []
for val in list1:
    list2.append(val[::-1])
print(list2)
# ['aqS', 'slooT', 'enilnO', 'gninraeL', 'mroftalP']

print("-"*50)
###########################################################
#Python program to split the list into two-part, the left side all odd values and
# the right side all even values.
list1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
even_value = []
odd_value = []
for val in list1:
    if val%2==0:
        even_value.append(val)
    else:
        odd_value.append(val)
#print(even_value)
#print(odd_value)
odd_value.extend(even_value)
#result = odd_value + even_value
print(odd_value)  # [5, 7, 11, 17, 19, 2, 8, 12, 22]
#print(result)

print("-"*50)
############################################################
# Problem to get common elements from two lists.
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
common_values = []
for val in list1:
    if val in list2:
        common_values.append(val)
print("common_values :",common_values)

print("-"*50)
############################################################
# reverse a list with reversed Using reversed method
list1 = [2,3,7,9,3,1]
result1  = list(reversed(list1))
print(result1)

print("-"*50)
############################################################
#Problem to print true if common elements between lists.
list1 = [2,4,7,8,3]
list2 = [4,5,0]
for val in list1:
    if val in list2:
        print("True")
print("-"*50)
############################################################
# Python program to insert items at a specific position in the list.
list11 = [2,4,6,8,3,33]
#Index: 3
#Item: 55
list11.insert(3,55)
print(list11) # [2, 4, 6, 55, 8, 3, 33]