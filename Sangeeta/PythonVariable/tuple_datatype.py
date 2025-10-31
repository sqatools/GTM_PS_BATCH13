
tup1 = (3, 5, 8.5, 8,['hello', 19],(5, 4), 'true', {'a': 23})

print(tup1, type(tup1))
for val in tup1:
    print(tup1)
print("_"*50)
# to print with index

for i in range(len(tup1)):
    print(i, tup1[i])
print("_"*50)

# for slicing method
tup2 = (3, 5, 8.5, 8,['hello', 19],(5, 4), 'true', {'a': 23})
print("tup2 tuple values are : -", tup2)
print("tup2 [2:6] is - ", tup2[2:6])
print("tup2[-2] is - ", tup2[-2])

print("_"*50)

## sorted funciton
tup4 = (1,2,3,4,5)
print("values i nthe tuple are : ",tup4)
#sorted in ascending order
result1 = sorted(tup4)
print("Result of sorted tuple tup4 is : ", result1)
## Reverse function
result2 = reversed(tup4)
print("Result of reverse of tup4 is : ", result2)
print("_"*50)
## The above one has given different output. The way to reverse i.e to view in desc order is as below
result3 = sorted(tup4, reverse=True)
print("descending order :", result3)
## To view in reverse order is as below
result4 = tuple(reversed(tup4))
print("reversed list in a tuple would be :", result4)

print("_"*50)

## Count method
tup5 = (5, 0, 8, 19, 5, 7, 0, 5, 5.5)
result1 = tup5.count(5)
print("count of 5 in tup5 :-", result1)

print("_"*50)
### Concatenation
t1 = (5, 9, 16)
t2 = ('a', 'b', 'c')
t3 = t1+t2
print("Concatenate 2 tuples would be :", t3)
print("_"*50)


