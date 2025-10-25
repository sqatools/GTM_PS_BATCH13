print("Write a python program to get longest word from given string")
print("."*100)
str="Hello friends goodmorning lets have a tea and cofee"
word_list=str.split(" ")
max_len=0
long_word=" "

for word in word_list:
    print(word,len(word))
    word_len=len(word)
    if word_len > max_len:
        max_len=word_len
        long_word=word
    else:
        continue
print("Longest Word :", long_word)
print("Long Length :",max_len)