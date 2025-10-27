# srting Formatting
print("String Concatenation")
print("."*100)

name="Latika"
age=30
city="Thane"

result = "My name is Latika and age is 30, I live in Thane"
print(result)

# 1. String Concat
result1= "My name is "+name+", and age is "+str(age)+", I live in "+city+""
print(result1)

#2. Format Method
result2= "My name is {}, and age is {}, I live in {}".format(name,age,city)
print(result2)

#3.Fstring formatting method
result3 = f"My name is {name}, and age is {age}, I live in {city}"
print(result3)

#################################################################################################
# String indexing and slicing
print("String indexing and slicing")
str_a="Programming"
print(str_a[5])
print(str_a[-1])

###############################################################################################
print("**Slicing in string**")
"""
Rule 1 -
1. str[start index:end index]
-> output will be include start index value and exclude last index value.
2. In this rule user can read sub string from left to right only.
3. start index and end index could +ve and -ve
4. Default end index is end of string.
"""
str_b="Learning"
print(str_b[0:5])

str_c="Latika Patil"
print(str_c[5:1])
print(str_c[-5:-1])
print(str_c[-5:])
print(str_c[-3:-6])
print(str_c[:7])

####################################################################################################

"""
Rule 2 -
1. str[start index:end index]
-> output will include the start index value and exclude last index value.
2. In this rule user can read sub string from left to right and right to end.
3. Start index and end index could be +ve and -ve
4. Step value also could be +ve OR -ve
"""

str1="Python Programming"

print(str1[-1:-12:-1])

#########################################################################################################

# reverse entire string
str2 = "Hello Good Morning"
print(str2[::-1])

# internal execution of ::-1
print(str2[-1:-len(str2)-1:-1])

print(str2[::1])
print(str2[0:len(str2):1])
###################################################################################################################
print("."*50)
############################# string method ################
# lower() and upper() method :
str3 = "My Name Is Latika"
print("upper case result :", str3.upper())

print("lower case result :", str3.lower())

#########################################################################################################################
# isupper() and islower() :  These methods check given string is in upper case or lower case and return boolean output (True/False)
str4= "Hi"
str5 = "HELLO"
str6 = "Good Morning"
print("str4 :", str4.isupper(), str4.islower())
print("str5 is upper :", str5.isupper())
print("str6 is lower :", str6.islower())

########################################################################################################################
# swapcase method :  This method convert upper to lower and lower to upper in one single string.
str7 = "We ArE LeArNing PytHon"
print("str7 result :", str7.swapcase())

####################################################################################################################

# capitalize method : convert first letter in upper case and keep remaining in lower case.

str8 = "We ArE LeArNing PytHon, Its Easy to Learn"
print("str8 output :", str8.capitalize())

#######################
# title method: convert first letter of each word in upper case.
str9 = "we arE leArNing PytHon, itS easY to LearN"
print("str9 output :", str9.title())

print("."*50)
#######################
# count method :  This method return the total count/occurrences of any character/substring in the string
str10 = "We Are 12345 Learning Python, Its Easy 12345 To Learn doing 12345"
print("Count of e :", str10.count('e'))
# Count of e : 4
print("count of ing :", str10.count("ing")) # count of ing : 2
print("count of 12345 :", str10.count("12345")) # count of 12345 : 3c

print("."*50)
#######################
# index() method :  this  method return the index position of any character /substring
str11 = "Good Morning, Hope you are doing good"
print("Index of Hope :", str11.index("Hope"))
print("Index of o:", str11.index("o"))

print("."*50)
#######################
# Apply loop on string.
str_a = "Programming"
for var in str_a:
    print(var)

print("."*50)
len_string = len(str_a)
print(len_string)

for i in range(len_string):
    print(i, str_a[i])

print("."*40)
# get all o from string
str12 = "Good Morning, Hope you are doing good"
temp = 0
for char in str12:
    if char == "o":
        print(char)
        temp +=1

print("total count :", temp)

print("."*50)
#######################
# split method : this method split string from given char/space/comma and return as list of words.
str13 = "Good Morning, Hope you are doing good"
result = str13.split(" ")
print(result)
str14 = "we,are,Learning,Python"
print(str14.split(","))

print("."*50)
#######################
# replace method:  This method help us to replace one from another word.
str15 = "JAVA is great Programming Language, and JAVA is hard to understand JAVA"
# replace all occurrences
result1 = str15.replace("JAVA", "Python")
print(result1)

result2 = str15.replace("JAVA", "PYTHON").replace("hard", "easy")
print(result2)

# replace first occurrence
result3 = str15.replace("JAVA", "Python", 2)
print(result3)
##########################################################################################3

str16="Hello students lets learn java"
word_list=str16.split(" ")
print(word_list)
result=""
for word in word_list:
    print(word)
    if word.lower()=="java":
        result=result +"Python"+  " "
    else:
        result=result+word+ " "
print("result : ",result)

#################################################################################################
print("."*100)
"""
Join Method - This Method join any string or interable data with any character/special char/substring.
"""
list1=["Hello","We","Are","Learning","Python"]
result1=" ".join(list1)
print("result1",result1)

pass1="P@ssw0rd"
result2="&^%*".join(pass1)
print("Result2 :", result2)

pass2=result2.replace("&^%*"," ")
print("Result pass2 is:",pass2)

#################################################################################################
print("."*100)

"""
Strip Method - this method remove all trailing spaces from given string
"""
str_b="  Added Space in the start and end  "
print("Orignal String is: ",str_b)
print("strip result is:",str_b.strip())

print("Remove left and right spaces")
print("Remove left spaces:", str_b.lstrip())
print("Remove right spaces:",str_b.rstrip())

#################################################################################################
print("."*100)
"""
Find method return the index position of given char/sub string from target string, but if the char/substring is not available then it will return -1
"""
str_c="India is my country"
r2=str_c.find("my")
print("find of my is:",r2)

r3=str_c.find("python")
print("find of python is:",r3)


