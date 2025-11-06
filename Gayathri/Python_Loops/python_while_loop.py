#16th Oct Class
#################################################################################################
#while loop - its a condition loop
#here while loop executes until the conition is true, when loop condition fails - it loop terminates

#print value from 1- 10
num1 = 0
while num1 < 10:
    #num1 = num1 + 1
    num1 += 1
    print("num1 value :", num1)

###############################################################################################
#print infinite loop
# num1 = 0
# while True:
#     num1 += 1
#     print("num1 value :", num1)
# #here it gets to infinite loop as it never becomes false

#############################################################################################
#17th Oct
#continue and break statement

#continue condition means - jump to next iteration without executing remaining portion of the code
#continue statment help to move to next iteration of the loop without executing remaoning portion of the code

for i in range(10):
    if i == 3 or i ==5 or i ==7:
        continue
    print(i, end=" ") #0 1 2 4 6 8 9
    #here it doesnt print 3,5,7 bcz when the condition is met - it skips the remaining portion of the code
    #ie. print statment and any otehr code below it wont be executed and it goes to start of the code

print("_"*40)

#break statement - break statment will break the loop executoin immediately once break condition is satisfied
for i in range(1,10):
    if i == 5:
        break
    print(i)  #it will execute only from 1,2,3,4 ..when it comes to 5, the loop condition is met and hence the loop breaks
    #1 2 3 4

#for negative step value in reverse
for i in range(10,1,-1):
    if i == 5:
        break
    print(i, end=" ") #10 9 8 7 6






