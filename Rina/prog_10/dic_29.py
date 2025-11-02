"""
dict1 = {'a': 60, 'b': 94, 'c': 77}
dict1['d'] = 100
dict1['e'] = 1
print("dic1: ", dict1)


str1 = "We are learning Python"
word_list = str1.split(" ")
print(word_list)
result = {}
for word in word_list:
    first_char = word[0]
    result[first_char] = word
print(result)

dict4 = {'e': (4,8,44), 'b': 'hello', 'a': 'pinch', 'g': (66,11,90)}
val = dict4.pop('a')
print("remove value: ", val)

list1 = ['v', 'w', 'g']
list2 = [10, 2200, 130]
dict1 = dict(zip(list1, list2))
print(dict1)



dict7 = {'a': [3, 3, 3], 'b': [4, 4, 4], 'c': [9, 9, 9]}
output = {}
for k, v in dict7.items():
    output[k] = sum(v)
    print("output :", output)


dic8 = {'a': 19, 'b': 29, 'c': 29, 'd': 49}
dic9 = {'e': 79, 'g': 59, 'h': 99, 'd': 49}

dic9.update(dic8)
print("dic9 :", dic9)


dict8 = {'a': 19, 'b': 29, 'c': 29, 'd': 49}
val_c = dict8.pop('c')
val_b = dict8.pop('b')
print("Removed values :", val_c, val_b)
print('dict8 :', dict8)
"""



