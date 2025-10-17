"""
# range(start, end, step value)
->  Output of the range will include start value and exclude the end value.
->  Output will show value as per the step value from start to end.
->  default start value is zero and default step value is 1
    range(10)  ->  range(0, 10, 1)
    range(3, 10) -> range(3, 10, 1)
->  start value, end value and step value could be +ve or -ve
"""
for i in range(1, 11, 1):
    print(i)

print("_"*100)
##########################################################################
# default start value 0 and step value as 1
for i in range(10):  # -> range(0, 10, 1)
    print(i)


print("_"*100)
###########################################################################
# show output with decrement value
for i in range(20, 0, -2):
    print(i)


print("_"*100)
###########################################################################
# show output with decrement value
for i in range(10, 0, 1):
    print(i)

# blank output as per the step value because of wrong range

print("_"*100)
############################################################################
# write a program to get sum of all the value from 1 to 10
sum = 0
for i in range(1, 10):
    sum = sum + i
    print("sum of each number", sum)

print("sum of all the numbers", sum)


print("_"*100)
############################################################################
# write a python program to print all the value divisible 3 and 5 from 1 to 50:
for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print(i)
    else:
        pass


print("_"*100)
#############################################################################








