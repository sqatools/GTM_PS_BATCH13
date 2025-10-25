import re

str8 = "It's my Life. I live by my own rules. 12345y test."
word_list = str8.split(" ")
print(word_list)
max_word =''
max_length = 0
for word in word_list:
    word_length = len(word)
    if word_length>max_length:
        max_length = word_length
for word in word_list:
    if len(word) == max_length:
        max_word = max_word+" "+word+", "
print("The List of words with maximum length", max_length, "characters are: ", max_word)