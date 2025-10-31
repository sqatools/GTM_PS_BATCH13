# list1 = [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {5, 7, 9}, True]
# print(list1, type(list1))
#
# # [12, 3.5, 'Hello', (5, 6, 7), [6, 7, 8], {'a': 123}, {9, 5, 7}, True] <class 'list'>
#
# print(list1[2])  # Hello
# print(list1[-3]) # {'a': 123}
# print(list1[4])  # [6, 7, 8]
# print(list1[4][1]) # 7
#
# print("_"*50)
# ###################################
# list2 = ['a', 'b', 'c', 10, 20, 30]
#
# # loop to get value without indexing
# for val in list2:
#     print(val)
# print("_"*50)
# # loop to get value with indexing
# list_len = len(list2)
#
# for i in range(list_len):
#     print(i, list2[i])
#
# print("_"*50)
# for i in range(-list_len, 0, 1):
#     print(i, list2[i])
#
# ###############################
test = "Hello world"
print(len(test))
# for i in range(len(test)):
#     print(i, test[i])
# print(test[0:3])
test = test[0:4] + 'a' + test[6:]
print(test)

# print(test[0:1])
# print(test[0:2])
# print(test[1:3])