str1 = "Experiencing the pain in the muscle aching and go on thats wt makes the champion"
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

print("Longest word :", long_word)
print("Long len :", long_len)


