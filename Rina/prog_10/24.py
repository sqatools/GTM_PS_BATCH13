"""

str1 = "we are learning PYTHON programming and its easy to learn."
word_list = str1.split(" ")
long_len = 0
long_word = ""

for word in word_list:
    print(word, len(word))
    word_len = len(word)
    if word_len > long_len:
        long_len = word_len
        long_word = word
    else:
        continue

print("Longest Word :", long_word)
print("Long Len :", long_len)

"""

str2 = "Rina Reena Preena Preen Preena Rina RINA"
word_list = str2.split()
print(word_list)
result = ""
for word in word_list:
    if word not in result:
        result = result + word + " "
    else:
        continue
print(result)

