'''2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64
'''


dict= {'a': 5, 'b':3, 'c': 6, 'd': 8}

for val in dict:
    print(val,":", dict[val]**2)
    print(val, ":", dict[val] **3)



