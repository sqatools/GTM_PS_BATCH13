# 1.Program to create a tuple with 2 lists of data
list1 = [4, 6, 8]
list2 = [7, 1, 4]
tup = tuple(zip(list1,list2)) #converted list to tuple
print(tup) # ((4, 7), (6, 1), (8, 4))

print("-"*50)
##########################################################################
#2. Python tuple program to find the maximum & Minimum value from a tuple
tup1 = (41, 15, 69, 55)
print("Maximum value :",max(tup1)) # Maximum value : 69
print("Minimum value :",min(tup1)) # Minimum value : 15

print("-"*50)
##########################################################################
#3. Python tuple program to create a tuple and find an element from it by its index no
# Index = 2
tup2 = (4, 8, 9, 1)
print(tup2[2]) # 9

print("-"*50)
##########################################################################
#4.Python tuple program to assign values of tuples to several variables and print them
tup4 = (6,7,3)
variables = 'a','b','c'
(a,b,c) = tup4
print("a :",a)
print("b :",b)
print("c :",c)

print("-"*50)
##########################################################################
# 5.  Python tuple program to add an item to a tuple.
tup5 =  ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')

str1 = ''
for char in tup5:
    str1 += char
    print("string :",str1) # sqatools

print("-"*50)
##########################################################################
#6.Python tuple program to get the 2nd element from the front and the 3rd element
# from the back of the tuple.
tup7 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
print(tup7[1]) # q
print(tup7[-3]) # o

print("-"*50)
##########################################################################
#7. Python tuple program to check whether an element exists in a tuple or not
tup8 = ('p','y','t','h','o','n')
for p in tup8:
    print("True")
else:
    print("False")
'''
True
True
True
True
True
True
False
'''
print("-"*50)
##########################################################################
#8.Python tuple program to find an index of an element in a tuple.
A=('s','q','a','t','o','o','l','s')
#Index of a?
print(A.index('a')) # 2

print("-"*50)
##########################################################################
#9.Python tuple program to find the length of a tuple.
tup9=('v','i','r','a','t')
result = len(tup9)
print(result) # 5

print("-"*50)
##########################################################################
#10. Python tuple program to reverse a tuple
tup10 = ( 4, 6, 8, 3, 1)
result = tuple(reversed(tup10))
print(result) # (1, 3, 8, 6, 4)