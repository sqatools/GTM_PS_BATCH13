tup1 =(3,3.5,'hello',[4,5],(8,9),{'a':123},{4,7,9},True)
print(tup1,type(tup1))

print()
print("."*100)
# Apply loop on tuple
for val in tup1:
    print(val)

print()
print("."*100)
# Apply loop with index
for i in range (len(tup1)):
    print(i,tup1[(i)])

print()
print("."*100)

# Slicing
tup2 =(4,7,8,9,'a',8.9,{'a':124})
print("slicing",tup2[2:5])
print("slicing with -ve index",tup2[::-1])

print()
print("."*100)

# Methods
# count
tup3=(4,9,10,2,15,1,4,8,4)
print("Count of 4 is ",tup3.count(4))
# index
print("Index of 9 is ",tup3.index(9))

print()
print("."*100)
# Concat
t1=(5,8,9)
t2=('a','b','c')
print("Concat result is :",t1+t2)

# sorted
print()
tup4=(5,8,10,56,3,7)
result1=sorted(tup4)
print("Sorted tuple in ascending order is :",result1)

result2=sorted(tup4,reverse=True)
print("Sorted tuple in descending order is :",result2)

# reversed function
result3=tuple(reversed(tup4))
print("Reverse result of tuple is:", result3)












