'''Properties:
->  Dict is mutable datatype, we can modify any point of time.
->  Dict contains data in curly braces in keys value pair e.g.   {key : value}, {'a': 123}
->  Dict contains unique keys, duplicate keys are not allowed.
     {'a': 123, 'b': 456, 'a': 789}
     if we mention the duplicate then it will only consider the latest defined value
     it means it will consider a = 789

->  Only immutable data can be key in the dictionary e.g. int, float, complex,  string, tuple, boolean
   not allowed as key e.g. list, dict, set
'''


dict1 = {'a': 123, 'b' : 456, 'c': 789}
print(dict1)
print(len(dict1))

for k,v in dict1.items():
    print(k, v)

# Add key to dictionary
dict1['d'] = 788
print(dict1)

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