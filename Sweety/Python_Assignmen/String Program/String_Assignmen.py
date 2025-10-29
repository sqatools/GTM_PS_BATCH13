# 1. Wright a prograaam to count vowels from string.
name = "Ramesh"
vowels = "aeiouAEIOU"
count = 0
for char in name:
    if char in vowels:
        count = count + 1
print(count)

print("_"*50)
############################################################################
# 2. write a python program to remove duplicate words from given string.
str1 = "abc xyz abc jkl mno pqr xyz"
result = ""
string_split = str1.split()

for word in string_split:
    #print(word)
    if word not in result:
        result = result+word+" "
    else:
        continue
print(result)

print("_"*50)
############################################################################
# 3. write a python program to get longest word from given string.
str2 = "write a python program to get longest word from given string"
str_split = str2.split()
long_len = 0
long_word = ""

for word in str_split:
    #print(word, len(word))
    word_len = len(word)
    if word_len > long_len:
        long_len = word_len
        long_word = word
    else:
        continue
print(long_len)
print(long_word)










