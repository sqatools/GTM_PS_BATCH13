""""for i in range (1, 10, 1):
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

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

   # for i in range(7, 0, -1):
    #for j in range(i):
    #    print("*", end=" ")
   # print()
print("_" * 8)
print()
####################################

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end= " ")
    print()

print("_" * 8)
print()
##################################Continue##################]
for i in range(10):
    if i==3 or i == 5 or i ==7:
     continue
    print(i)
print("_" * 8)
print()
for j in range(50):
    if j % 2 == 0 or j % 3 == 0 or j % 5 == 0:
        continue
    print(j)
print("_" * 8)
print()
for k in range(10):
    if k ==4:
        break
    print(k)
print("_" * 8)
print()
for k in range(10,1,-1):
    if k ==8:
        break
    print(k)
###############################################
print("_" * 8)
print()
#Check given numeber is prime or not- A prime number is a number greater than 1 that has no divisors other than 1 and itself
# only divisible by 1 or itself:
N= 13      # need to take flag = prime =True- a flag is a variable used to signal a condition — basically, a True/False marker that helps you control the flow of your program.
prime =True
for i in range(2,N):
    if N %i==0:
        prime = False
        break
    else:
        continue
if prime ==True:  # you can use alternate : prime
    print("It is a prime number")
else:
    print("It is not a prime numbe")
#############################################################
print("_" * 8)
print()
Num = 41
Prime = True
for j in range(2,Num):
    if Num % j == 0:
        Prime = False
        break
    else:
        continue
if Prime:
    print("Prime number")
else:
    print("Not a prime number")
############################################
print("_" * 8)
print()
# How many Prime numbers are in the given list



for Num in range(1,100):
    Prime = True
    for j in range(2,Num):
        if Num % j == 0:
            Prime = False
            break
        else:
            continue
    if Prime:
        print("Prime number",Num)
    else:
        pass
#########################Pattern program##################
print("_" * 8)
print()
for i in range(1,6):
    for j in range(1,6):

        print("*",end="")
    print()
#######################################
print("_" * 8)
print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
        #print("*", end=" "
    print()
##########################################
print("_" * 8)
print()
for i in range(6,0,-1):
    for j in range(i):
       # print(j, end="")
       print("*",end="")
    print()
#########################################
print("_" * 8)
print()
for i in range(1,6):
    for j in range(i):    # Growing numbers each line, J = range(i), If i =1 j= range(1) print j value =0
        print(j,end="")                     # If i =2  j= range(2)  print J value: 0 1
                                            #  If i =3 J =range(3)  print j value : 0 1 2
    print()
print("_" * 8)
print()
for i in range(1,6):
    for j in range(1,6):   # Same numbers each line
        print(j,end="")
    print()
##############################
print("_" * 8)
print()
for i in range(5,0,-1):
    for J in range(i):
        print(J, end="")
    print()
###############################
print("_" * 8)
print()
for i in range(1, 6):
    for j in range(1, i+1 ):  ##when i = 1, j runs 1 time → prints 1
        print(i, end="")         #When i = 2, j runs 2 times → prints 2  2
    print()
"""
#########################################
##rite a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
#nput1:1500 nput2:2700
print("_" * 8)
print()
for i in range(1500,2700):
    if i%7==0 and i%5==0:
       print(i,end="  ")


##Python Loops program to construct the following pattern, using a nested for loops.

for i in range(6):
   print(i*"*")

for i in range(6,-1,-1):
    print(i*"*" )

####################################
print("_" * 8)
print()
for i in range(1,6):
    for j in range(i):
        #print("*",end="")
      print(j,end="")
    print()
for i in range(4,-1,-1):
    for j in range(i):
       # print("*", end="")
       print(j,end="")
    print()

list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6]
print(list1==list2)  #True

print(sorted(list1) == sorted(list2)) #True

def multab(a):
    for i in range(1,11):
        print(i,"*", a, "=", i*a)
multab()



