print(1)
print(2)

# range(start, end, step value)
# Output of the range will include start value and exclude end value.
# If start value is not defined , then default value is 0.
# Step value is the difference that you want in range.
# Output will show value as per the step value from start to end.
# range(10) --> range(0,10, 1)

print ("*"*50)
for i in range(1, 10,1):
    print(i)
print("*"*50)

print("Write a program to get a sum of all the values from 1 to 10")
sum = 0
for i in range (1,11):
    sum = sum+i
    print("Sum :", sum)

print("*"*50)

print("Write a python prg. to print all values divisible by 3 and 5 from 1 to 50")

for j in range(1,50):
    if j % 3 ==0 and j % 5 == 0:
        print(j, end=" ")
    else:
        pass
print("_"*50)

# outer loop
for i in range(1, 6):
    print(" ")
    print("Address :", i)
    for j in range(1, 4):
        print("Package :", j)
print("*"*50)

