print(1)
print(2)

"""
# range(start, end, step value)
->  Output of the range will include start value and exclude the end value.
->  Output will show value as per the step value from start to end.
->  default start value is zero and default step value is 1
    range(10)  ->  range(0, 10, 1)
    range(3, 10) -> range(3, 10, 1)
->  start value, end value and step value could be +ve or -ve
"""
print("_"*40)
for i in range(1, 10, 1):
    print(i)

"""
1
2
3
4
5
6
7
8
9
"""

print("_"*40)
# default start value 0 and step value as 1
for i in range(5):  # -> range(0, 5, 1)
    print(i)

"""
0
1
2
3
4
"""


print("_"*40)
# output with step value as 2
for i in range(1, 10, 2):
    print(i)

"""
1
3
5
7
9
"""

print("_"*40)
# show output with decrement value
for i in range(10, 0, -2):
    print(i)

"""
10
8
6
4
2
"""


print("_"*40)
# show output with decrement value
for i in range(10, 0, 1):
    print(i)

# blank output as per the step value

#######################################
print("_"*40)
# write a program to get sum of all the value from 1 to 10
sum = 0
for i in range(1, 11): # i = 1, 2, 3,
    sum = sum + i  # 0+1 = 1 | 1 +2 = 3 | 3+ 3 = 6
    print("sum :", sum)

print("__")
print("total sum :", sum)

###############################################
print("_"*40)
# write a python program to print all the value divisible 3 and 5 from 1 to 50:
for j in range(1, 50):
    if j%3 == 0 and j%5 == 0:
        print(j)
    else:
        pass

"""
15
30
45
"""

print("_"*50)
####################################
# Apply loop on list
list1 = [4, 7, 92, 17]
for val in list1:
    print(val)

"""
4
7
92
17
"""

print('---')
list1 = [4, 7, 92, 17]
for val in list1:
    print(val, end=" ")

# 4 7 92 17

############################# Nested For Loop ########################
# In nested for loop, for each value of outer loop, then entire inner loop will be executed.
# outer loop
for i in range(1, 6):  # i =1, 2
    print("Address i:", i)
    # inner loop
    for j in range(1, 4): # j = 1, 2, 3
        print("Package j:", j)
    print("_"*10)

##########################################
# outer
for i in range(1, 6):  # i =1, 2
    print("Address i:", i)
    # inner loop
    for j in range(1, 4): # j = 1, 2, 3
        print("Package j:", j)
    print("_"*10)

    # inner loop
    for k in range(1, 4): # k = 1, 2, 3
        print("Package k:", k)
    print("_"*10)


#######################################

for i in range(1, 6):  # i =1, 2
    print("Address i:", i)
    # inner loop1
    for j in range(1, 4): # j = 1, 2, 3
        print("Package j:", j)
        # inner loop2
        for k in range(1, 4):  # k = 1, 2, 3
            print("item k:", k)


    print("_"*10)


print("_"*50)
############################# While Loop ########################

 # while loop : condition loop

num = 1
while num < 10:
    print(num)
    #num = num + 1
    num += 1


# infinite loop
"""
num = 1
while True:
    print(num)
    #num = num + 1
    num += 1
"""

print("_"*40)
######################### Continue and Break Statement ##############
# Continue :  continue statement help to move next iteration of the loop without executing the remaining portion of the code.

for i in range(10): # i = 0
    if i == 3 or  i == 5 or i == 7:
        continue # police man
    print(i)

# break :  break statement will break the loop execution immediately once break condition is satisfied.
print("_"*40)
for i in range(10, 1, -1):
    if i == 5:
        break
    print(i)


#########################################