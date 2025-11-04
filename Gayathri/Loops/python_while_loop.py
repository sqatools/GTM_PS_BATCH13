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
num1 = 0
while True:
    num1 += 1
    print("num1 value :", num1)
#here it gets to infinite loop as it never becomes false