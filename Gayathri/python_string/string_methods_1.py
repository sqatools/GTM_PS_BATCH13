#24th Oct-25
############################# string method ################
# lower() and upper() method :
str3 = "We Are Learning Python"
print("upper case result :", str3.upper())
# WE ARE LEARNING PYTHON

print("lower case result :", str3.lower())
#  we are learning python
#camel case - camel case starts with a lowercase letter

######################
# isupper() and islower() :  These methods check given string is in upper case or lower case and return boolean output (True/False)
str4= "Hello"
str5 = "PYTHON"
str6 = "programming"
print("str4 :", str4.isupper(), str4.islower()) # False False
print("str5 is upper :", str5.isupper()) # True
print("str6 is lower :", str6.islower()) # True

#######################
# swapcase method :  This method convert upper to lower and lower to upper in one single string.
str7 = "We ArE LeArNing PytHon"
print("str7 result :", str7.swapcase())
# wE aRe lEaRnING pYThON

#######################
# capitalize method : convert first letter in upper case and keep remaining in lower case.

str8 = "We ArE LeArNing PytHon. Its Easy to Learn"
print("str8 output :", str8.capitalize()) # We are learning python, its easy to learn
strc = "123 Testing Learn"
print("strc output :", strc.capitalize()) #123 testing learn

#######################
# title method: convert first letter of each word in upper case.
str9 = "we arE leArNing PytHon, itS easY to LearN"
print("str9 output :", str9.title())
# We Are Learning Python, Its Easy To Learn
#this is Pascal case starts with an uppercase letter

print("_"*50)
###########################################################################################
# count method :  This method return the total count/occurrences of any character/substring in the string
str10 = "We Are 12345 Learning Python, Its Easy 12345 To Learn doing 12345"
print("Count of e :", str10.count('e'))
# Count of e : 4
print("count of ing :", str10.count("ing")) # count of ing : 2
print("count of 12345 :", str10.count("12345")) # count of 12345 : 3

print("_"*50)

#######################
# index() method :  this  method return the index position of any character /substring
str11 = "Good Morning, Hope you are doing good"
print("Index of Hope :", str11.index("Hope")) # 14
print("index of you is :",str11.index("you"))  #19
print("Index of o:", str11.index("o")) # 1


print("_"*50)
#######################
#get the index of the oo which is in good statment above, to do that we need to use loop
# Apply loop on string.
str_a = "Programming"
for var in str_a:
    print(var)
"""
P
r
o
g
r
a
m
m
i
n
g

"""
#above just prints the string using loop, but we need to nkow the indexing
print("_"*50)
len_string = len(str_a)
print(len_string)

for i in range(len_string):
    print(i, str_a[i])
"""
0 P
1 r
2 o
3 g
4 r
5 a
6 m
7 m
8 i
9 n
10 g
"""
###############################################################
print("_"*40)
# get all o from string
str12 = "Good Morning, Hope you are doing good"
temp = 0
for char in str12:
    if char == "o":
        print(char)
        temp +=1

print("total count :", temp)

#another way of counting the o without loop
print("count of o is :", str12.count("o")) #count of o is : 8

print("_"*50)

"""
o
o
o
o
o
o
o
o
total count : 8
"""
#######################
# split method : this method split string from given char/space/comma and return as list of words.
str13 = "Good Morning, Hope you are doing good"
result = str13.split(" ")
print(result)
# ['Good', 'Morning,', 'Hope', 'you', 'are', 'doing', 'good']

str14 = "we,are,Learning,Python"
print(str14.split(","))  # ['we', 'are', 'Learning', 'Python']

print("_"*50)

#######################
# replace method:  This method help us to replace one from another word.
str15 = "JAVA is great Programming Language, and JAVA is hard to understand JAVA"
# replace all occurrences of JAVA with PYTHON
result1 = str15.replace("JAVA", "Python")
print(result1) # Python is great Programming Language, and Python is hard to understand

result2 = str15.replace("JAVA", "PYTHON").replace("hard", "easy")
print(result2)
# PYTHON is great Programming Language, and PYTHON is easy to understand

# replace first occurrence and seond occurance, so there are 3 java, 1st 2 occurance of Java is replaced with Python
result3 = str15.replace("JAVA", "Python", 2)
print(result3)
# Python is great Programming Language, and Python is hard to understand JAVA


print("_"*50)
#####################################################################