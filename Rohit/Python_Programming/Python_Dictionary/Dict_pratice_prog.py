#1.Python program to add elements to the dictionary.

dict1 = {'name':'Rahul'}
dict1["Surname"]= 'Chavan'
dict1["Age"] = '18'
print(dict1) # {'name': 'Rahul', 'Surname': 'Chavan', 'Age': '18'}

print("-"*50)
############################################################################
#2.Python Dictionary program to print the square of all values in a dictionary.
dict2 =  {'a': 5, 'b':3, 'c': 6, 'd' : 8}
result = {}
for k,v in dict2.items():
    result[k] = v**2
print(result) # {'a': 25, 'b': 9, 'c': 36, 'd': 64}

print("-"*50)
############################################################################
#3.Python Dictionary program to concatenate two dictionaries.
dict3 = {'Name':'Harry','Rollno': 345, 'Address':'Jordan'}
dict4 = {'Age' : 25, 'salary': '$25k'}
dict3.update(dict4)
print(dict3) # {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan', 'Age': 25, 'salary': '$25k'}

print("-"*50)
##########################################################################
#4.Python Dictionary Program to create a dictionary from two lists.
list1 = ['a','b','c','d','e']
list2 = [12, 23, 24, 25, 15, 16]
dict = dict(zip(list1,list2))
print(dict) # {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}

print("-"*50)
##########################################################################
#5.Python Dictionary program to store squares of even and cubes of
# odd numbers in a dictionary using dictionary comprehension.
dict5 = [4, 5, 6, 2, 1, 7, 11]
result = {}
for i in dict5:
    if i%2==0:
        result[i] = i**2
    else:
        result[i] = i**3

print(result) # {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}

print("-"*50)
##########################################################################
#6.Python Dictionary program to concatenate two dictionaries.
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}
dict1.update(dict2)
print(dict1)

print("-"*50)
##########################################################################
#7.Python Dictionary program to get a list of odd and even keys from the dictionary.

dict6 = {1:25, 5:'abc', 8:'pqr',21:'xyz',12:'def',2:'utv'}

for val in dict6:
    print(val)
    if val%2==0:
        print("Even number :", val)
    elif val%2!=0:
        print("odd number :", val)

print("-"*50)
##################################################################
# 8.Python Dictionary program to sort a dictionary using keys.
dict7 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
result = sorted(dict7.items())
print("sorted by keys :", result) # [('a', 13), ('b', 53), ('c', 41), ('d', 21)]

print("-"*50)
##################################################################
# 9.Python Dictionary program to sort a dictionary in python using values.
dict8 = {'d':14,'b':52,'a':13,'c':41}
result1 = (sorted(dict8.items(), key=lambda item : item[1]))
print("Sorted by values :", result1) # [('a', 13), ('d', 14), ('c', 41), ('b', 52)]

print("-"*50)
##################################################################
# 10.Python Dictionary program to add a key in a dictionary.
dict10 = {1:'a', 2:'b'}
dict10 [3] = 'C'
print(dict10) # {1: 'a', 2: 'b', 3: 'C'}

print("-"*50)
##################################################################
#11.Python Dictionary program to get the sum of all the items in a dictionary.
#dict11 = {'x' : 23, 'y' : 10 , 'z' : 7}
#result = {}
#for key, val in dict11:
 #   result[key] = sum(val)
#print("sum of all items :", result)

#print("-"*50)
##############################################################
name = input("Enter student name")
m1 = int(input("Enter english subject marks :"))
m2 = int(input("Enter Maths subject marks :"))
m3 = int(input("Enter Hindi subject marks "))

dic1 = {'name': name, 'marks':(m1,m2,m3)}
avg = (m1 + m2 + m3) /3

print("Average marks :", avg)
print(dic1)

