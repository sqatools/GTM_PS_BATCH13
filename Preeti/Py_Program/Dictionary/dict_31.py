dict = {'a': 123, 'b' : 456, 'c': 789}
print(dict)
print(len(dict))

for k,v in dict.items():
    print(k, v)

# Add key to dictionary
dict['d'] = 788
print(dict)

# write a python program to create a dictionary from given string.
str1 = "We are learning Python"
# output = {"W": We, "a": "are", "l": "learning", "P": "Pyt

word_list=str1.split()
print(word_list)
result={}
for word in word_list:
    first_char = word[0]
    result[first_char] = word
    print(result)
print("Result :", result)