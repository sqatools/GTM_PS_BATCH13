"""
for i in range(10):
    print(i)


# Output with increment value
for i in range(1,10,2):
    print(i)

#Outout with decrement value
for i in range(10,0,-2):
    print(i)
"""
"""
sum = 0
for i in range(1,11):
    print("Number is",i)
    sum = sum + i
    print("Sum of all numbers", sum)
print("*" * 10)
print("Final sum",sum)
"""
"""
print("_"*30)
#Write a phyton program to print all the values is divisible by 3 and 5 from 1 to 50:

for j in range(1,50):

    if j % 3 == 0 and j % 5 == 0:
        print("Numberr divisible by 3 and 5 :",j)
    else:
        pass
"""
"""
#Apply loop on list
list1=[1,4,8,9]
for val in list1:
    print(val)
"""
"""
######################################## Nested For loop####################################
#Outer loop
for i in range(1,3):
    print("Address i:",i )
#Inner loop
    for j in range(1,5):
        print("Package j:",j )
        for k in range(1,5):
            print("Item k:",k )
    print("_" * 30)
"""
"""
############## While loop#####
num=1
while num<10:
    print(num)
    num=num+1
"""


"""
##################Continue and break statement #####
for i in range(10):
    if i==3 or i ==5:
        continue
    print(i)
"""

###### Break statement#######
print("_"*30)
for i in range(1,10,2):
    if i==5:
        break
    print(i)