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
#2. write a python program to get all the required output values from list.

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
# 3.  write a python program to get max value from list without using inbuilt function.
list1 = [5, 7, 9,  23, 80,  56]
max_value = 0
for value in list1:
    if value > max_value:
        max_value = value
    else:
        continue
print("max_value :", max_value)

print("_" * 50)
#####################################################################
# 4. write a python program to remove duplicate values from list
list2 = ["Rohit", "Rahul", "Rohan",  "Ravi", "Rahul", "Rohit"]
output = []
for name in list2:
    if name not in output:
        output.append(name)
        #output = output + name #here output is a list and name is a string
        #we get error when we try to concatenate list and string - an only concatenate list (not "str") to list
    else:
        continue
print("output list is :", output)
#output list is : ['Rohit', 'Rahul', 'Rohan', 'Ravi']

#there is another way of addressing this issue
#convert the list to set, since set will consider only use unique values and eliminate duplicate
#but set will not have any indexing as it takes random value
var3 = set(list2)
print(var3)  # {'Rohan', 'Rahul', 'Ravi', 'Rohit'}
print(list(var3))  # ['Rohan', 'Rahul', 'Ravi', 'Rohit'] #again convert this to list and will get indexing

print("_" * 50)
#####################################################################
# 5. write a python program to move all positive values to left side and negative values to right side
list3 = [5, 8, -9, 2, -30, 10, -60]
pos_list = []
neg_list = []
for value in list3:
    if value > 0:
        pos_list.append(value)
    else:
        neg_list.append(value)
print("Output list:",pos_list + neg_list)
#Output list: [5, 8, 2, 10, -9, -30, -60]

#here we can also use extend method, extend wil modify the current list
pos_list.extend(neg_list)
print("result :", pos_list) #result : [5, 8, 2, 10, -9, -30, -60]

#if we want to sort this list
print("sorted result :", sorted(pos_list)) #sorted result : [-60, -30, -9, 2, 5, 8, 10]
print("_" * 50)
######################################
#write a program to reverse the list without built in keyword
list_q = [10,67,1,78,3]
print("reversed list is :",list_q[::-1]) #reversed list is : [3, 78, 1, 67, 10]

#if using for loop
for i in range(len(list_q)):
    print(list_q[i]) #it prints each number in a seperate row
#since we want to reverse the number, we need to give negative indexing
print("_" * 50)
output=[]
for i in range(-1,-len(list_q),-1):
    print(list_q[i],end=" ") #this prints in reverse but in individual line, but we want in list
    #add the end to make it in same line
#if we want the output in list, declare a empty list and then append it
    output.append(list_q[i])
print("revered list is :",output), #revered list is : [3, 78, 1, 67]
print("_" * 50)