#write a python program to remove duplicate words from given string
str1 = "RAHUL PREETI PARTH ARUN RAHUL PARTH"
#while working on string with statment, always split the word
word_list = str1.split()
result = ""
#go thorugh each word
for word in word_list:
    if word not in result:
        result = result + word + " "
    else:
        continue #move to the next word
    print(result)
    """
    RAHUL 
RAHUL PREETI 
RAHUL PREETI PARTH 
RAHUL PREETI PARTH ARUN 
    """
print("final result",result)
#RAHUL PREETI PARTH ARUN

print("_"*40)
#############################################################################
#Q2 write a python program to get longest word from given string.
str2 = "We are Learning Python Programming ,Its easy to learn"
word_list1 = str2.split(" ")
max_len = 0
long_word = ""
for word in word_list1:
    print(word,len(word))
    # now compare the word len
    word_len = len(word)
    # now this word_len have to compare with something i.e max_len which is currently 0
    # now if that word is long then we need to store in something - then store in long_word
    if word_len > max_len:
        max_len = word_len
        long_word = word
    else:
        continue
print("output is :",long_word)
"""
We 2
are 3
Learning 8
Python 6
Programming 11
,Its 4
easy 4
to 2
learn 5
"""
#output is : Programming

#####################################################################
#27th Oct 25 -Class
####################################################################
# Q3 :  Wright a prograaam to count vowels from string.
#vowels = a,e,i,o,u
str3 =  "good morning, hope you are doing good."
vowels = "aeiouAEIOU"
count = 0
for char in str3:
    if char in vowels:
        count +=1
    else:
        continue
print("Vowel count is :",count)
#Vowel count is : 14

#######################################
#print each character 3 times
str4 = "Morning"
for x in str4:
    print(x*3)

