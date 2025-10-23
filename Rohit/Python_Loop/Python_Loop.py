"""
# range(start, end, step value)
->  Output of the range will include start value and exclude the end value.
->  Output will show value as per the step value from start to end.
->  default start value is zero and default step value is 1
    range(10)  ->  range(0, 10, 1)
    range(3, 10) -> range(3, 10, 1)
->  start value, end value and step value could be +ve or -ve
"""
for i in range (1,10,1):
    print(i)

print("--"*50)
######################
for j in range (1,10,2):
    print(j)

print("--"*50)

##########################################
#Show output with decrement value
for k in range (10,0,-2):
    print(k)
print("-"*50)

# default start value 0 and step value as 1#
for i in range(7):  # -> range(0, 7, 1)
    print(i)
print("-"*40)

################################################
# write a program to get sum of all the value from 1 to 5
sum=0
for i in range(1,6): # i = 1, 2, 3,
    sum = sum + i # 0+1 = 1 | 1 +2 = 3 | 3+ 3 = 6
    print("sum:",sum)

print("--")
print("Total Sum:",sum)

print("-"*50)
###################################################
# write a python program to print all the value divisible 3 and 5 from 1 to 50:
for i in range (1,50):
    if i%3==0 and i%5==0:
        print(i)
print("-"*50)
####################################
# Apply loop on list
list1 = [2, 37, 11, 27]
for val in list1:
    print(val)
print("-"*50)

list1 = [2, 7, 10, 17]
for val in list1:
    print(val,end=" ")

print("-"*50)
############################# Nested For Loop ########################
# In nested for loop, for each value of outer loop, then entire inner loop will be executed.
# outer loop
for i in range(1, 6):  # i =1, 2
    print("Address i:", i)
    # inner loop
    for j in range(1, 4):  # j = 1, 2, 3
        print("Package j:", j)
    print("_" * 10)

############################# While Loop ########################

 # while loop : condition loop
num = 1
while num < 10:
    print(num)
    #num = num + 1
    num += 1
######################### Continue and Break Statement ##############
# Continue :  continue statement help to move next iteration of the loop without executing the remaining portion of the code.
for a in range(10):
    if a == 3 or a ==5 or a == 7:
        continue

 ##break :  break statement will break the loop execution immediately once break condition is satisfied.
print("_"*40)
for i in range(15, 1, -1):
    if i == 7:
        break
    print(i)


