str8 = input("Enter a string: ")
translator = str.maketrans('','','.,:&')
cleanstr = str8.translate(translator)
word_list = cleanstr.split(" ")
print(word_list)
max_word = []
max_length = 0
for word in word_list:
    word_length = len(word)
    if word_length>max_length:
        max_length = word_length
for word in word_list:
    if len(word) == max_length and word not in max_word:
        max_word.append(word)
print("The List of words with maximum length", max_length, "characters are: ", max_word)