list1 = [1,2,3,4]
list2 = [5,6,7,8]
print("The combination of each items from both the lists from it's corresponding index is")
for val in range(0,len(list1)):
    print(tuple((list1[val],list2[val])))

print("_" * 50)

tup1 = (1,2,3,4)
print("The maximum value in the tuple is", max(tup1))

list1 = [1,2,3,4]
list2 = []
print("The combination of each item and it's square is: ")
for val in list1:
    list2.append((val,pow(val,2)))
print(list2)

tuple1 = (1,2,'a','cvs',['a','b','c'],{1,2})
print("The mid elements of the tuple are: ",tuple1[2:4:])

tuple1 = (1,2,3,4)
result = sorted(tuple1, reverse=True)
print("The reverse list of values in the tuple are: ",tuple(result))