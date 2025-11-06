#28th Oct-25 - Class
# 1.write a python program to get all the even values from list
list1 = [4, 7, 9, 2, 8, 12, 11]
output = []
for value in list1:
    if value %2 == 0:
        output.append(value)
    else:
        continue
print("Output of the list :",output)
#Output of the list : [4, 2, 8, 12]

print("_" * 50)
####################################################################################################
#solve above program to with list comprehension
result = [abc for abc in list1 if abc % 2 == 0]
#its like for abc in list1, if abc %2 ==0, store the value in abc. its liek above output we have abc
print("Result :", result)

print("_" * 50)
##############################################################################################
# write a python program to get all the required output values from list.

list2 = [4, 7, 9, 12]
#we want output like this
## output = [(4, 'even'), (7, 'odd'), (9, 'odd'), (12, 'even')]
output = []
for value in list2:
    if value % 2 == 0:
        output.append((value,'even'))
    else:
        output.append((value,'odd'))
print("Output of the list :",output)
#Output of the list : [(4, 'even'), (7, 'odd'), (9, 'odd'), (12, 'even')]
################################################################################################
#solve the above program in list comprehension
result =  [(value,'even')if value%2==0 else (value,'odd') for value in list2 ]

#here first - we start withf or value in list2,we want if else loopp for evena nd odd
#that we add seond but before the for loop
print("result :", result)

#if we want just the number is even or odd, but dont want the number to be printed
result3 = ["even" if y % 2 == 0 else "odd" for y in list2]
print("result3 :", result3)
#result3 : ['even', 'odd', 'odd', 'even']

#now if its even, print square of the number and if odd - print cube of that number
result4= [(i**2) if i%2==0 else (i**3) for i in list2]
print("result4 :", result4)
#result4 : [16, 343, 729, 144]

print("_" * 50)
#####################################################################

