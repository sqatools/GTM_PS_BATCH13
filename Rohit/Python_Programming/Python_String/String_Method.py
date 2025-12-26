##Reverse Entire String
str1 = "Good Morning"
print(str1[::-1]) ## gninroM dooG
print(str1[-1:-len(str1)-1:-1]) ## elaborate how its work -ve (Interview questions)
## gninroM dooG
print(str1[::1]) # Good Morning
print(str1[0:len(str1):1]) ## elaborate how its work +ve
# Good Morning

print("-"*50)
######################### String Method ####################################################
# lower () and upper () Method :
str2 = "I am Learning Python Programming"
print("lower case result :",str2.lower()) # i am learning python programming
print("upper case result :",str2.upper()) # I AM LEARNING PYTHON PROGRAMMING

print("-"*50)
########################################################################################
## isupper () and islower () Method: These methods check given string is in upper case or lower case and return boolean output (True/False)
str3 = "Hello"
str4 = "WORLD"
str5 = "python"
print("str3:",str3.isupper(),str3.islower()) # False False
print("str4 is upper :",str4.isupper()) # True
print("str5 is lower :",str5.islower()) # True

print("-"*50)
###############################################################################
##swapcase method : This method convert upper to lower and lower to upper in one single string
str6 = "GuYs I aM LearNinG pyThoN"
print("str6 result :",str6.swapcase()) # gUyS i Am lEARnINg PYtHOn

print("-"*50)
####################################################################
# Capitalize Method : convert first letter in upper case and keep remaining in lowe case
str7 = "guYs i aM learNinG pyThoN"
print("str7 result :",str7.capitalize()) #Guys i am learning python

print("-"*50)
#####################################################################
## title Method : convert first letter of each word in upper case
str8 = "good morning i have join the python class"
print("str8 result :",str8.title()) # Good Morning I Have Join The Python Class

str9 = "gooD moRnIng i haVe Join the pythOn clASs"
print("str9 result :",str9.title()) # Good Morning I Have Join The Python Class

print("-"*50)
#######################################################################
## Count Method :This method return the total count/occurrence of any character/substring in the string
str10 = "I am Leaving in karad city Learning Python Programming"
print("count of a :",str10.count('a')) # count of a : 6
print ("count of ing :",str10.count('ing')) # count of ing : 3

print("-"*50)
#######################################################################
# Index() method :  this  method return the index position of any character /substring
str11 = "Good Morning, Hope you are doing good"
print("Index of Hope :",str11.index('Hope')) # Index of Hope : 14
print("Index of are :",str11.index('are')) # Index of are : 23
print("Index of d :",str11.index('d')) # Index of d : 3

print("-"*50)

#######################################################################
# split method : this method split string from given char/space/comma and return as list of words.
str12 = "Good Morning, Hope you are doing good"
result = str12.split()
print(result)
#['Good', 'Morning,', 'Hope', 'you', 'are', 'doing', 'good']

str13 = "I,am, Learning, python"
result = str13.split(",")
print(result)
#['I', 'am', ' Learning', ' python']

print("-"*50)
##########################################################################
# replace method:  This method help us to replace one from another word.
str14 = "JAVA is great Programming Language, and JAVA is hard to understand JAVA"
result = str14.replace("JAVA","Python")
print(result)
# Python is great Programming Language, and Python is hard to understand Python

result1 = str14.replace("JAVA","Python").replace("hard","easy")
print(result1)
# Python is great Programming Language, and Python is easy to understand Python

result2 = str14.replace("JAVA","Python",2)
print(result2)
#Python is great Programming Language, and Python is hard to understand JAVA

print("-"*50)
#######################################################################
## Apply loop in string
str16 = "programming"
for char in str16:
    print(char, end="") ## programming

len_string = len(str16)
print(len_string)   ## 11

for i in range(len_string):
    print(i, str16[i])
""""
0 p
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
print("-"*50)
#######################################################################
# join method: This method join any string or iterable data with any character/special char/substring.
str = ["I" , "am","Leaving", "in", "Karad", "city"]
result = " ".join(str)
print("result :", result)  ## I am Leaving in Karad city

str1 = "Password"
result2 ="&%34*/".join(str1)
print("result2 :",result2) ## P&%34*/a&%34*/s&%34*/s&%34*/w&%34*/o&%34*/r&%34*/d

result3 =str1.replace("&%34*/","")
print("result3 :",result3)  ## Password

print("-"*50)
#######################################################################
# strip method :  this method remove all trailing spaces from given string.
# trailing spaces :  spaces which is available in the beginning and end of the string.

str17 = " Programming Language "
print(str17)
print(str17.strip()) #Programming Language space is removed here

# Remove left space
print(str17.lstrip()) #Programming Language here left space is removed

# Remove Right space
print(str17.rstrip()) # Programming Language here right space is removed

print("-"*50)
###################################################
# find method :  find method return the index position of given char/sub-string from target string, but if the char/sub-string
# is not available, then it will return the -1
# This find method is same as Index method only difference is find method we can get -ve value
# if char is not their in string but in index we will not get -ve value it will show error

str_a = "Karad is good city"
result = str_a.find("good")
# check existing word
print("result :",result) # 9

# check non - existing word
result1 = str_a.find("District")
print("result1 :",result1)  # -1

result2 =str_a.index("good")
print("result2 :",result2)

result3 =str_a.index("Great")
print("result3 :",result3)
## ValueError: substring not found