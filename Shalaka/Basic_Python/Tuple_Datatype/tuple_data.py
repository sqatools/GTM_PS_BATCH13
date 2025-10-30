tup1= (2,3.3,'hello',[4,5],(2,1),{'a',90},True)
print(tup1,type(tup1))

# apply loop
for val in tup1:
    print(val)

# apply loop with indexing
for i in range (len(tup1)):
    print(i, tup1[i])

#Slicing Method
tup2 = (3,56,7,4,9,45,20)
print(tup2[2:5])

# Reverse tuple
print(tup2[::-1])

# Methods in Tuple #

# count Method

tup3 = (43,55,65,72,90,43,)
#get count of 43
print("Total conut of 43 : ", tup3.count(43))


#index method
tup4 = (43,55,65,72,90,43,)
print(tup4.index(90))

# Concatination
tup5 = (5,6,7)
tup6 = (30,23,77)
tup7 = tup5 + tup6
print(tup7)

#Sorted functions

tup8 = (23,45,67,30,77)
#in ascending order
result1 = sorted(tup8)
print(result1)
#in descending order
result2 = sorted(tup8, reverse=True)
print(result2)

