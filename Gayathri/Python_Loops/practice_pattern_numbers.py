##print the below pattern
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6): #1, 2, 3
    for j in range(1,i+1): #Row 1 - 1, Row 2( 1 2), row (1,3)
        print(i,end=" ")
    print()