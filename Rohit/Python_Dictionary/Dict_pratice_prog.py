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
#6.
