print("_"*40)
print("Python -  for loop")
for i in range(1,10,2):
    print(i)
print("Write a program to get sum of all value from 1 to 10")
sum = 0
for i in range(1,11,1):
    sum += i
print(sum)
print("_"*40)
print("Write a pyhon program to print all the value divisible 3 and 5 from 1 to 50")
for j in range(51):
    if j%3 ==0 and j%5 == 0:
        print("Divisible by both 3 and 5",j)
print("Apply loop on list")
l1 = [1,4,8,12]
for val in l1:
    print(val)
print("Nested Loop")
for i in range(1,15,5):
    for j in range(1,i,5):
        for k in range(1, j, 1):
            print(k)

