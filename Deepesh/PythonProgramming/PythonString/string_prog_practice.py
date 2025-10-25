#Q1 write a python program to remove duplicate words from given string.

str1= "RAHUL PREETI PARTHA ARUN RAHUL PARTHA"
word_list = str1.split(" ")
print(word_list)
result = ""
for word in word_list:
    if word not in result:
        result = result + word + " "
    else:
        continue

    print(result)


print("Final Result :", result)


print("_"*40)
#Q2 write a python program to get longest word from given string.

str2 = "We are Learning Python Programming ,Its easy to learn"
word_list = str2.split(" ")
long_len = 0 # 2
long_word = "" # we, Are, Learning
for word in word_list: # We, Are, Learning, Python, Programming
    print(word, len(word)) # (we, 2) (Are, 3), (Learning, 8) (Python, 6), (Programming, 11)
    word_len = len(word)
    if word_len > long_len: # 2 > 0 | 3 > 2 | 8 > 3 | 6 > 8 | 11 > 8
        long_len = word_len  # 2, 3, 8, 11
        long_word = word # we, Are, Learning, Programming
    else:
        continue


print("Longest word :", long_word)
print("Long len :", long_len)







