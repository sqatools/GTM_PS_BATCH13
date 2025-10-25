str8 = "It's my Life. I live by my own rules."
word_list = str8.split(" ")
print(word_list)
max_word = ""
max_length = 0
for word in word_list:
    word_length = len(word)
    if word_length>max_length:
        max_word = word
        max_length = word_length
    else:
        continue
print(max_word)