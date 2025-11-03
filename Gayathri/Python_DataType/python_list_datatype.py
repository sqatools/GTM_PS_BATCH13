#11th Oct -25
#####################################List Data Type ###########################################
"""
# Properties
-> List is mutable datatype.
-> List can contains any types of data e.g int, float, string, complex, list, tuple, bool, dict, set.
-> List follow positive and negative indexing.
-> List contains values in square bracket.
"""
list1 = [1, 4.5, 'Hello', [4, 7], (3, 7), {'a': 123}, {45, 67}, True]
print(list1, type(list1))
# [1, 4.5, 'Hello', [4, 7], (3, 7), {'a': 123}, {67, 45}, True] <class 'list'>
print(list1[2])  # Hello

#        0    1       2 - Positive Indexing
list2 = [20, [4, 8], True]
#       -3    -2     -1 - Negative Indexing

#Now if you want to get the list item from the list2
print("retreive the list item:",list2[1])  #[4, 8]
#now if we want to get the 2nd item from that list we retreived
print("get the 2nd value from the list:",list2[1][1])  #8
#if negative indexing
print("negative indexing to fetch the list value ",list2[-2][-1]) #8

# Add value to the list
list2.append(100)
print("list2 :", list2)
# list2 : [20, [4, 8], True, 100]

print("_"*40)
