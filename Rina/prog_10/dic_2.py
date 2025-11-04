"""
str1 = "We are learning Python Programing"
word_list = str1.split(" ")
print(word_list)
result = {}
for word in word_list:
    first_char = word[0]
    result[first_char] = word
    print(result)


"""

dict9 = {'e': 79, 'g': 59, 'h': 99, 'd': 49, 'e': 69, 'f': 79}
result1 = dict(sorted(dict9.items()))
print("sorted with keys: ", result1)
