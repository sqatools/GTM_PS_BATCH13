"""
range(start,end,step value)
output of the range include start value and exclude the end value
output will show the value as per step value from start to end
Default start value is zero and default step value is 1
range(10)--> range(0,10,1)
"""
print("Write a program to get sum of all the values from 1 to 10")
print("."*100)
sum=0
for i in range(1,11):
    sum=sum+i
    print(sum)
print("Total sum",sum)
#******************************************************************************************************************#
print("Write a program to print all the value is divisible by 3 and 5 from 1 to 50")
print("."*100)

for j in range(1,50):
    if j%3==0 and j%5==0:
        print(j)
    else:
        pass
#******************************************************************************************************************#
print("Apply loop on list")
print("."*100)
list=[3,8,10,6]
for val in list:
    print(val)

#******************************************************************************************************************#
print("Nested For Loop")

for i in range(1,6):
    print(i)
    for j in range(1,4):
        print("Package J:",j)
    print("*"*40)
#*******************************************************************************************************************#
print("While Loop, which is conditional loop")

print("Print 1 to 10 nos")
num=1
while num<=10:
    print(num)
    num+=1

#*******************************************************************************************************************#
print("."*100)
print("Continue Statement")
"""
Continue statement help tp move next iteration of the loop without executing the remaining portion of the code.
"""
for i in range(10):
    if i==3 or i==5 or i==7:
        continue
    print(i)

#*******************************************************************************************************************#
print("."*100)
print("Break Statement")
"""
Break statement will break the loop execution imidiately once break condition is satisfied.
"""
for i in range(1,10):
    if i==5:
        break
    print(i)
print("."*50)
for j in range(10,1,-1):
    if j==5:
        break
    print(j)
