# Q1 write a python program to remove duplicate words from given string.

str1 = "MAHA vidya lakshmi shastik"
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

##String Slicing

text = "MAHAvidya"
print(text[0:4])   # from index 0 to 3 → 'MAHA'
print(text[4:])    # from index 4 to end → 'vidya'
print(text[:4])    # from start to 3 → 'MAHA'
print(text[-5:])   # last 5 characters
print(text[:-5]) # from start to -5

##Substring
text = "Python is fun"
print("Python" in text)      # True
print("Java" in text)    # False

#changing case

text1 = "Maha Vidya"
print(text1.upper())
print(text1.lower())   # 'maha vidya'
print(text1.title())   # 'Maha Vidya'
print(text1.capitalize())  # 'Maha vidya'

#remove space

text2 = "   hello   "
print(text2.strip())    # removes spaces from both sides
print(text2.lstrip())   # removes left spaces
print(text2.rstrip())   # removes right spaces


#Q2 write a python program to get longest word from given string.

text4= "I want to learn python programming"
word_list = text4.split(" ")
long_len = 0 # 2
long_word = ""
for word in word_list:
    print(word, len(word)) #
    word_len = len(word)
    if word_len > long_len: #
        long_len = word_len  #
        long_word = word #
    else:
        continue


print("Longest word :", long_word)
print("Long len :", long_len)

