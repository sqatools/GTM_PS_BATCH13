# Default start value is always 0, and step value is 1.

for i in range(1, 10, 1):
    print(i)

print('_'*30)
# When start value 0 and step value as 1
for i in range(11):
    print(i)

print('_'*30)
# When output with step value as 2
for i in range(1, 10, 2):
    print(i)

print('_'*30)
# Output with decrement value
for i in range(10, 0, -2):
    print(i)



print('_'*30)
# Write a python program to get the sum off all the values from 1 to 10
sum =0
for j in range(1,11):
    sum = sum+j
print('sum :', sum)



print('_'*30)
# Write a python program to to print all the nummbers divided by 3 & 5

for j in range(1,50):
    if j%3 ==0 and j%5 ==0:
        print(j)
    else :
        pass


print('_'*30)

# Apply loop on list
list1 = (1,2,23,30,77,92)
for val in list1:
    print(val)


print('_'*30)

######## Nested for loop #######

for i in range(1,6):
    print ('Add :',i)
    for j in range(1,3):
        print ('package :', j)

