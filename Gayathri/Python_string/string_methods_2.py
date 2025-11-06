#25th oct 25 Class
###############################################################################################
# write a python program to replace all java word without replace method.

str16 = "JAVA is great Programming Language, and Java is HARD to understand JAva"
word_list = str16.split(" ")
print("split of the string is :", word_list)
#['JAVA', 'is', 'great', 'Programming', 'Language,', 'and', 'Java', 'is', 'HARD', 'to', 'understand', 'JAva']
result = ""
for word in word_list:
    print(word) # we get ech word seperately
    if word.lower() == "java":
        result = result + "PYTHON" + " "
    else:
        result = result + word + " "
print("result statement is :", result)
#PYTHON is great Programming Language, and PYTHON is HARD to understand PYTHON

#here replace will replace only certain words bcz JAVA above is having mixed case of Upper,lower,
#its difficult to use replace, so use above program
print(str16.replace("JAVA", "Python"))

#####################################################
# join method: This method join any string or iterable data with any character/special char/substring.

list1 = ["Hello", "We", "Are", "Learning", "Python"]
result1 = " ".join(list1)
print("result1 :", result1) # Hello We Are Learning Python


pass1 = "P@ssw0rd"
result2 = "&^%*".join(pass1)
print("result2 :", result2) # P&^%*@&^%*s&^%*s&^%*w&^%*0&^%*r&^%*d

#recover the old password
pass2 = result2.replace("&^%*","")
print("result pass2:", pass2) # P@ssw0rd

print("_"*50)
###################################

# strip method :  this method remove all trailing spaces from given string.
# trailing spaces :  spaces which is available in the beginning and end of the string.
str_b = "  Python Programming  "
print(str_b)
print(str_b.strip())  # Python Programming

# remove left spaces
print(str_b.lstrip()) #Python Programming  #

# remove right spaces
print(str_b.rstrip()) #  Python Programming#

#to remove the space bewteen words- we can use the replace method
###################################################
# find method :  find method return the index position of given char/sub-string from target string, but if the char/sub-string
# is not available, then it will return the -1

str_c = "India is great country"

# check existing word
r2 = str_c.find("great")
print("r2 :", r2)  # r2 : 9

# check non - existing word
r3 = str_c.find("city")
print("r3 :", r3) #  -1

# r4 = str_c.index("city")
# print(r4)
# ValueError: substring not found

