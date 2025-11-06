"""
#Q1 : Write a python prgm to check given num is prim ot not
# Prime num is only divisible by one an itself
num =13
prime = True

for i in range(2,num):
    if num % i == 0:
        prime = False
        break
    else:
        continue

if prime == True:
    print("This is a prime number", num )
else:
    print("This is a not prime number", num )


"""
"""
# Write a prgm to get all the prim number form 1 to 100
for num in range(1,100):
    prime = True

    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    else:
        continue

    if prime == True:
        print(num, end= )
    else:
        pass
    """
"""
#Pattern prgrm
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
    
    """

# Prgrm for this pattern
"""
*****
****
***
**
*

"""
"""

for i in range(5,0,-1):
    for j in range(i):
        print("*", end= '')
    print()

"""
"""
#Prgrm for
1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
"""