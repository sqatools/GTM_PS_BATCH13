tup1=(3,5,7,7,9,)
print(tup1)
print('-'*45)
#########################################
### apply loop on tuple
for i in tup1:
    print(i,end=  " ")
print('-'*45)
# Apply loop with indexing
print(tup1.index(7))
print('-'*45)
#########################################
t1 = (3, 3,3,3.5, 'Hello', [4, 7, 8], (6, 7), {'a': 123}, {4, 7, 8}, True)
print(t1)
print('-'*45)
############################# Slicing #######################
print(t1[2:5])
print(t1[: : 2])
print(t1[::-1])
print('-'*45)
#########################################
# count method:  will give the no of occurences
print(t1.count('Hello'))
print('-'*45)
#########################################
# Index method:
print(('Index of (6, 7):',t1.index((6,7))))
print(t1+t1)
# sorted function:
t3=(1,3,6,8,9)
print(sorted(t3))
