#15th Oct-25 class
#if we want to print 1 - 10
print(1)
print(2)
print(3)
#--- continue till print(10) - which is not right appraoch

#for this we use the loops
"""
#range function
# range(start, end, step value), it has 3 things to be defined
->  Output of the range will include start value and exclude the end value. ie. n-1
->  Output will show value as per the step value from start to end.
->  default start value is zero and default step value is 1
  range(10)  ->  range(0, 10, 1), so if no start value is mentioned by default it starts from 0 and default step value is 1
  range(3, 10) -> range(3, 10, 1), so here start is 3, stop is 10 and default step value is 1
->  start value, end value and step value could be +ve or -ve
-> range works only on numbers and not on character
"""

#write a program to print from 1-10
for i in range(1,11,1):
    print(i)

"""
1
2
3
1
2
3
4
5
6
7
8
9
10
"""
print("*"*50)
#################################################################################################
#default start value as 0 and step value as 1
for i in range(5): #intenally it is range(0,5,1)
    print(i)
"""
0
1
2
3
4
"""
print("*"*50)
############################################################################################################
#output with srtp value as 2
for i in range(1,5,2):
    print(i)
"""
1
3
"""
############################################################################################################
#show output with decrement value
for i in range(10,0,1): #here the step value cannot be blank bcz we are doing decrememt, also here step cannot be positive also
    print(i)

"""
10
8
6
4
2
"""

#################################################################################################################
#write a program to get the sum of all numbers from 1 - 10
sum_value = 0
for i in range(1,11):
    sum_value = sum_value + i
print("sum value is :",sum_value)

##################################################################################################################
#write a program to printall the value diviisble 3 and 5 from 1 to 50
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("value of the number is : ", i)
    else:
        pass #dont want to do anything we can use pass
# value of the number is :  15
# value of the number is :  30
# value of the number is :  45

###############################################################################################################
#apply loop on list
list1 = [4,7,20]
#print the values in the list
for i in list1:
    print("values in the list :",i)
# values in the list : 4
# values in the list : 7
# values in the list : 20

#why we get the values in next line,bcz in definition of pirnt - after each item it pushes to next line - end='\n'
#instead of getting in the next line, if we want output in one single line, overwrite the end definition of print
list_2 = [5,7,12,34]
for i in list_2:
    #print(i, end=",") #5,7,12,34,
    print(i, end=" ") #5 7 12 34

######################################################################################################
#Nested for Loop
#we have Outer Loop - Inner Loop
#For each value of outerloop -the entire inner loop has to executed

#outer-loop
for i in range(1,4):
    print("i am in outerloop",i)
    for j in range(1,2):
        print("i am in innerloop",j)
    print("***"*10)

# i am in outerloop 1
# i am in innerloop 1
# ******************************
# i am in outerloop 2
# i am in innerloop 1
# ******************************
# i am in outerloop 3
# i am in innerloop 1
# ******************************


