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






