str1 = "Hello"
str2 = '''Learning
Python 134&&&& '''
str3 = """
we are 
learning 0-=908989
Python
"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))

##################################################
print("_"*50)
# String formatting
name = "Ramesh"
age = 26
city = "Bengaluru"
Result = "My name is Ramesh and age is 26, I live in Bengaluru"
# 1.  string concatenation:
result1 = "My name is "+name+" and age is "+str(age)+" ,I live in "+city
print(result1)

# 2.  format method:
result2 = "My name is {} and age is {}, I live in {}".format(name, age, city)
print(result2)

# 3.  fstring formatting method:
result3 = f"My name is {name} and age is {age}, I live in {city}"
print(result3)

######################################################
# String indexing and slicing

str_a = "Programming"
print(str_a[5])  # a
print(str_a[-3]) # i

# Indexing
"""
 0   1   2   3  4    +ve indexing
 H   E   L   L  O
-5  -4  -3   -2 -1   -ve indexing
"""


print("_"*50)
######################### Slicing in string ############
"""
Rule1 = str[start index: end index]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right only.
->  start index and end index could be +ve or -ve
->  default start index is zero.
->  default end index is end of string.
->  default step value is 1

"""     #01234567
str_b = "Learning"
        #-8-7-6-5-4-3-2-1
print(str_b[0:8:1]) #Learning
print(str_b[0:8]) #Learning
print(str_b[:])   #Learning
print(str_b[0:])  #Learning
print(str_b[:7])  #Learnin
print(str_b[:8])  #Learning
print(str_b[-8:-1]) #Learnin
print(str_b[-8:]) #Learning
print(str_b[-4:-1])#nin

print("_"*50)
"""
Rule2 = str[start index: end index: step value]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right or right left.
->  start index and end index could be +ve or -ve
->  and step value also could be +ve or -ve
->  default start index will be -1 if step value is -ve.
->  default start index will be zero if step value is +ve
"""

str_c = "Python programming"

print(str_c[-1:-9:-1]) #gnimmarg
print(str_c[-1:-9:1]) #give blank output because for -ve index step value should be -ve
print(str_c[0:6:-1]) #give blank output because for +ve index step value should be +ve
print(str_c[0:10])
print(str_c[-10:-1])

print("_"*50)
############################# string method ################
# lower() and upper() method
str3 = "We Are Learning Python"
print(str3.lower())
print(str3.upper())

print("_"*50)
#######################
# isupper() and islower() :  These methods check given string is in upper case or lower case and return boolean output (True/Fals

str4 = "Hello"
str5 = "hello"
str6 = "HELLO"
print(str4.isupper(), str4.islower())
print(str5.islower())
print(str6.isupper())

print("_"*50)
#######################
# swapcase method :  This method convert upper to lower and lower to upper in one single string.
str7 = "wE aRE lEARNING pYTHON"
print(str7.swapcase())


print("_"*50)
#######################
# capitalize method : convert first letter in upper case and keep remaining in lower case.
str8 = "We ArE LeArNing PytHon, Its Easy to Learn"
print(str8.capitalize())

print("_"*50)
#######################
# title method: convert first letter of each word in upper case.
str9 = "we arE leArNing PytHon, itS easY to LearN"
print(str9.title())


print("_"*50)
#######################
# count method :  This method return the total count/occurrences of any character/substring in the string
str10 = "We Are 12345 Learning Python, Its Easy 12345 To Learn doing 12345"
print("count of e", str10.count('e'))
print("count of ing", str10.count("ing"))


print("_"*50)
#######################
# index() method :  this  method return the index position of any character /substring
str11 = "Good Morning, Hope you are doing good"
print(str11.index("Hope"))
print(str11.index('o'))

print("_"*50)
#######################
# Apply loop on string.
str_a = "Programming"
for character in str_a:
    print(character)


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

print("_"*40)
# get all o from string
str12 = "Good Morning, Hope you are doing good"
temp = 0
for char in str12:
    if char == "o":
        print(char)
        temp +=1

print("total count :", temp)

print("_"*50)
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
# replace all occurrences
result1 = str15.replace("JAVA", "Python")
print(result1) # Python is great Programming Language, and Python is hard to understand

result2 = str15.replace("JAVA", "PYTHON").replace("hard", "easy")
print(result2)
# PYTHON is great Programming Language, and PYTHON is easy to understand

# replace first occurrence
result3 = str15.replace("JAVA", "Python", 2)
print(result3)
# Python is great Programming Language, and Python is hard to understand JAVA


print("_"*50)
#####################################################################
# write a python program to replace all java word without replace method.
str16 = "PYTHON is great programming language and Python is easy to understand, PYthon"
word_list = str16.split()
print(word_list)
result = ""
for word in word_list:
    if word.lower() == "python":
        result = result + "JAVA" + " "
    else:
        result = result + word + " "
print("Result:", result)


print("_"*50)
#####################################################
# join method: This method join any string or iterable data with any character/special char/substring.
list1 = ["Hello", "We", "Learning", "Python"]
result1 = " ".join(list1)
print(result1)

pass1 = "P@ssw0rd"
result2 = "&^%*".join(pass1)
print(result2)

result3 = "".join(pass1)
print(result3)


print("_"*50)
###################################
# strip method :  this method remove all trailing spaces from given string.
# trailing spaces :  spaces which is available in the beginning and end of the string.
str_b = "    I am learning Python           "

# remove left and right spaces
print(str_b.strip())

# remove left spaces
print(str_b.lstrip())

# remove right spaces
print(str_b.rstrip())


print("_"*50)
###################################################
# find method :  find method return the index position of given char/sub-string from target string, but if the char/sub-string
# is not available, then it will return the -1

str_c = "India is great country"

# check existing word
r2 = str_c.find("great")
print(r2)

# check non - existing word
r3 = str_c.find("city")
print(r3)

# r4 = str_c.index("city")
# print(r4)
# ValueError: substring not found



