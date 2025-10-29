"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""
list1 = [10, 4.7, 'Morning', (17,20, 10), [8, 0, 1], {'z': 890}, {55, 6, 0}, True]
print(list1, type(list1))
print(list1[2])
print(list1[-1])
print(list1[3])
print(list1[3][1])
print("-"*50)
print("")
# loop to get value without indexing
list2=[1,3,6,'i','am','in']
for x in list2:
    print(x)
print("-"*50)
print("")
# loop to get value with indexing
Y = len(list2)
for i in range(Y):
    print(i)
print("-"*50)
print("")
for i in range(-Y,0,1):
    print(i)
print("-"*50)
print("")
#####################################tuple##################
tupl=(5,5.5,'Hi',[1,2,3],{'a': 55},{22,9},False,(2,5))
print('tupl',type(tupl))

