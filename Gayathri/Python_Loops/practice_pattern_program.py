#patter program
#################################
"""
*
* *
* * *
* * * *
* * * * *
"""
#here the number of stars are increaing in every line
#line 1 - 1, Line 2 - 2, Line 3 - 3, Line 4 - 4, Line 5 - 5
for i in range(1,6): #when i = 1, it goes to next for loop
    for j in range(1,6): #when i = 1, j will execuet from 1 - 5
        print("*",end= " ") #will print 5 stars in line 1
    print() #move to next line as print by default as nextline
    #next i = 2, j will execuet from 1 - 5, next line and so forth it goes
    #i decide the line number and J decide the no of stars in the line
    #instead of * - we can print j - it will print 1 2 3 4 5, 1 2 3 4 5 in 5 lines

    # * * * * *
    # * * * * *
    # * * * * *
    # * * * * *
    # * * * * *

#above it prined a square
##################################################################
#now lets print a traingle
for p in range(1,6): # 1 , 2,3,4,5
    for q in range(1,p+1): #(1,2),(1,3),(1,4),(1,5)
        print("*",end= " ")
    print()
# *
# * *
# * * *
# * * * *
# * * * * *

#####################################