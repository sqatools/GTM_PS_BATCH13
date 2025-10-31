dict1 = {'a': 1, 'b' : 76, 'c': 56}
print(dict1, type(dict1))


# Add new key to dictionary
dict1['d'] = 77
dict1['b'] = 50
print("dict1 :", dict1)


# Apply loop on dictionary
for k, v in dict1.items():
    print(k, "|", v)




print("_"*50)
#######################
# write a python program to create a dictionary from given string.
str1 = "My age is twentyfour"

word_list = str1.split(" ")
print(word_list)
result = {}
for word in word_list:
    first_char = word[0]
    result[first_char] = word
    print(result)

print("Result :", result)


####################

# update method:  this method combine 2 dicts data
dict1 = {'a': 77, 'b': 88, 'c': 99}
dict2 = {12: 'Hello', 13: [5, 6, 7], 16: (3, 5, 7)}