"""
Write a python program to check give no is primt or not.
Note - prime no is only divisible by one and itself.
"""
num=13
prime=True
for i in range(2,num):
    #print(i)
    if num%i==0:
        prime=False
        break
    else:
        continue
if prime==True:
    print(num,"This is the prime number")
else:
    print(num,"This is not the prime number")
#######################################################################################################
print("Write a program to print all prime nos between 1 to 100")
print("."*100)

for num in range(num,100):
    prime=True

    for i in range(2,num):
        if num%i==0:
            prime=False
            break
        else:
           continue

    if prime:
        print(num)
    else:
        pass