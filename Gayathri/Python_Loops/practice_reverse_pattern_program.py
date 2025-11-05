#write a pattern program in reverse
"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(6,1,-1): #6-1 = 5, 5-1 = 4
    for j in range(1,i): #row 1- 5 Stars, row 2 - 4 stars
        print("*",end=" ")
    print()


############################################
for i in range(5,0,-1): #6-1 = 5, 5-1 = 4
    for j in range(i,0,-1): #row 1- 5 Stars, row 2 - 4 stars
        print("*",end=" ")
    print()
