# Q1 :  write a python program to check given number is prime or not.
# note:  prime number is only divisible by one or itself.

num = 31
prime = True

for i in range(2, num): # i = 2
    print(i)
    if num%i == 0: # 12%2 == 0
        prime = False
        break
    else:
        continue

if prime:
    print("This is prime number :", num)
else:
    print("This is not a prime number :", num)

print("_"*50)
###############################################################
# write a program to get all the prime number from 1 to 100
for num in range(1, 100):
    prime = True

    for i in range(2, num):  # i = 2
        #print(i)
        if num % i == 0:  # 12%2 == 0
            prime = False
            break
        else:
            continue

    if prime is True:
        print(num, end=" ")
    else:
        pass

#  1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
print()
print("_"*40)
############################################################################
# pattern program
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6): # i = 1, 2, 3
    for j in range(1, i+1): # j = (1, 2), (1, 3), (1, 4)
        print("*", end=" ")
    print()


print()
print("_"*50)

# write a program for this pattern.
"""
* * * * * 
* * * *
* * *
* *
*
"""


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()



"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""