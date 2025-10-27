# Write a python program to remove duplicate word from given string
str1 = "Rohit Rahul Jay Pushkar Rohit Jay"
word_list = str1.split()
result = ""
print(word_list)
for word in word_list:
    if word not in result:
        result = result + word + " "
        print(result)
    else:
        continue

print("final result:", result)

print("-"*50)

## Write a python program to get logest word from given string
str2 = "We are Learning Python programming, It is easy to learn"
word_list = str2.split()
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

print("-"*50)

## 
