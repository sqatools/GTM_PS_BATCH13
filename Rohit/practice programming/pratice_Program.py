# pattern program
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
print("-"*50)

############################################################
"""
* * * * *
* * * *
* * *
* * 
* 
"""
for i in range(6, 0, -1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()
#############################################
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
print("-"*50)
