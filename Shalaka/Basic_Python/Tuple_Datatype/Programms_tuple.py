print ('1). Python tuple program to create a tuple with 2 lists of data.')
list1 = [4, 6, 8]
list2 = [7, 1, 4]
tup_1 = tuple(zip(list1, list2))
print(tup_1)

print ('2). Python tuple program to find the maximum value from a tuple.')
tup_2 = (41, 15, 69, 55)
max_tup = 0
for val in tup_2:
    if val > max_tup:
        max_tup =val
    else:
        continue
print(max_tup)

print('3). Python tuple program to find the minimum value from a tuple.')
tup_2 = (36,5,79,25)
min_tup =tup_2[0]
for val in tup_2:
    if val<min_tup:
        min_tup = val
    else:
        continue
print(min_tup)

print('3). Python tuple program to find the minimum value from a tuple.')








