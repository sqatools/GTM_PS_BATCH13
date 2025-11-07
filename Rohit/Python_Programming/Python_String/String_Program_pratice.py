##Get a string made of first and the last 2 chars
from Rahul.String_Prgrms import word_len

str1 = "Rohit Chavan"
##print(str1[2]+str1[-2])
##print(str1[0:2:1])
##print(str1[-1:-3:-1])
print(str1[0:2:1]+str1[-1:-3:-1])  ## Rona

print("-"*50)
########################################################################
##String made of 4 copies of last 2 characters
str2 = "Rohit"
print(str2[-1:-3:-1]*4) ## titititi

print("-"*50)
########################################################################
## Reverse a string
str3 = "Samartha"
print(str3[::-1])

print("-"*50)
########################################################################
##program to count occurrences of a substring in a string.
#Write a program to count the occurrence of each character in a string.
str4 = "I am joining class of Python Programming"
print("count of a :",str4.count("a"))   ## count of a : 3
print("count of ing :",str4.count("ing")) ## count of ing : 2

print("-"*50)
###############################################################################
##to test whether a passed letter is a vowel or consonant
letter = "rohit"
for char in letter:
    if char == "a" or char == "o" or char =="h":
        print(f"{char} is vowel")
else:
    print(f"{char} is consonant")
'''
o is vowel
h is vowel
t is consonant
'''
print("-"*50)
####################################################################
##Write a program to count the number of vowels in a string.
letter = "rohit"
for char in letter:
    if char == "a" or char == "o" or char =="h":
        print(f"{char} is vowel:",letter.count(char))
'''
o is vowel: 1
h is vowel: 1
'''
print("-"*50)
####################################################################
#Write a program to reverse a string using slicing
str5 = "programming"
print(str5[-1:-5:-1]) ## gnim

print("-"*50)
####################################################################
#Write a program to capitalize the first letter of each word in a string.
str6 = "i aM USING pYChAm TOOl for WriTinG pyThiN ProGraM"
print("result :",str6.capitalize())   ## I am using pycham tool for writing pythin program

print("-"*50)
####################################################################
#Write a program to replace spaces with hyphens in a string

str7 = "I Join class of JAVA programming as JAVA has more scope in Market"

print("Result :",str7.replace("JAVA","Python"))
#I Join class of Python programming as Python has more scope in Market

print("-"*50)
####################################################################
# Find the longest and smallest word in the input string
str8 = "I learn python programming"
word_list = str8.split()
print(word_list)

print("longest word :",max(word_list,key=len)) #programming
print("smallest word :",min(word_list,key=len)) #I

print("-"*50)
####################################################################
#