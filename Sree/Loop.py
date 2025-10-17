for i in range (1, 10, 1):
    print(i)
####################################
print("1.","_"*50)

for i in range(2,10):
    print(i)
##############################
print("2.","_"*50)

for J in range(10):
    print(J)
###############################
print("3.","_"*50)

for k in range (1,10,2):
    print(k)
#############################
print("4.","_"*50)

for p in range(10, 1,-2):
    print(p)           #  print(p,end =" ")

##################################################
print("5.","_"*50)

#write a program to get sum of all the value from 1 to 10
sum = 0
for i in range(1,12): ## i = 1, 2, 3,
    sum = sum+i
                                #0+1 = 1 | 1 +2 = 3 | 3+ 3 = 6
    print("total:", sum)
###################################################
print("6.","_"*50)
#Print numbers from 1 to 10 using range().

for i in range (1,11):
    print(i)
####################################
print("7.","_"*50)
#Print even numbers between 1 and 20 using range().

for i in range(1,20):
    if i%2 ==0:
        print(" even numbers :", i)
##############################################
print("8.","_"*50)
#Print the multiplication table of 7 using range()
for i in range(1, 50):
    if i%7 ==0:
        print("Multiples of 7:", i)
#############################################
print("9.","_"*50)
#Print numbers in reverse order using range().
for i in range(10,0,-1):
    print("Numbers from backward direction:",i)
###################################################
print("10.","_"*50)
#Display all odd numbers from 1 to 50 using range().
for i in range(1,50,2):
    print("Odd nuber:", i)
########################################
print("11.","_"*50)
# Iterate over a list using for loop and range().
##############################################
print("12.","_"*50)
#Total sum of all the values from 1to 10
sum=0
for i in  range(1,11):
    sum = sum + i
    #print("Each value:" ,sum)
print('total value:',sum)
##################################
print("13.","_"*50)
#print all the values divisibl by 3 & 5
for i in range(50):
    if i%3==0 or i%5 ==0:
        #print("The value is divisible by 3 and 5:",i)
      print("the value is divisible by 3 or 5:",i)
    else:
        pass
####################################
print("14.","_"*50)
#Apply loop on a list

list = [1, 2, 3, 4, 5]  # no range required  /n:all
for j in list:
    #print(j)
    print(j, end=' ') # end='' this prints all values in single line

###################################
print("15.","_"*50)
# Nested for loop
for i in range(1,6):
    print("Address:",i)
    for j in range(1,4):
        print("package:", j)
    print("_"*8)
######################################
#While loop: it iterates s
#continue statement
for i in range(15):
    if i==3 or i ==4 or i==6:
        continue
    print(i)
###################################
#Break statement
for i in range(10):
    if i ==6:
        break
    print(i)
#########################
# Pattern program
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end= " ")
    print()
##########################
print()
print("_" * 8)

for i in range(7,1,-1):
    for j in range(1, i-1):
        print("*",end=" ")
    print()
####################################

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end= " ")
    print()










