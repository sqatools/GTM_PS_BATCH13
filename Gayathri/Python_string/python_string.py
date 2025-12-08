#23-Oct-25 Class

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
name = "Rohan"
age = 25
city = "Mumbai"

result = "My name is Rohan and age is 25, I live in Mumbai"

# 1.  string concatenation: where we can combine two strings with + operator
result1 = "My name is "+name+" and age is "+str(age)+", I live in "+city
print(result1)
#above age cant be used directly as its int, we are combining string - so we need to convert that to string
#else will get the error - can only concatenate str (not "int") to str
#in this method we break the string into multiple parts and add + symbol wherever we need to join

# 2.  format method: #here pass the arguments. here we need to remember the sequnce of parameters that we pass
result2 = "My name is {} and age is {}, I live in {}".format(name, age, city)
print(result2)

# 3.  fstring formatting method:just add the argumemts and here no need of converting int to str to join strings
result3 = f"My name is {name} and age is {age}, I live in {city}"
print(result3)
#this is the most popular method of formatting strings. no need of converion of data type - it auto converts



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
#with indexing we are getting 1 character, but if we want a sub string - we use slicing
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

"""

str_b = "Learning"
print(str_b[0:5])  # Learn

# In this rule user can read sub string from left to right only.
str_c = "Deepesh Yadav"
print(str_c[5:1]) #retruns blank value as it cannot move from right to left

#negative Indexing
print(str_c[-5:-1]) #Yada , here -1 wil be exclusive so it starts rom -2
print(str_c[-5:])  #Yadav, by default end position wil be -1, so it will get till end of string, ifnot defined
print(str_c[-13:-6]) #Deepesh

#+ve Indexing
print(str_c[:7]) #here start index is not defined, so by default it takes 0, #Deepesh
print(str_c[:]) #Deepesh Yadav, Here no start and end index, so it stars from 0 till end of teh string
print(str_c[0:]) #here the end of the index not defined, it considers till end of string, Deepesh Yadav

print("_"*50)
"""
Rule2 = str[start index: end index: step value]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right or right left.
->  start index and end index could be +ve or -ve
->  and step value also could be +ve or -ve
->  default start index will be -1 if step value is -ve.
->  default start index will be zero if step value is +ve
->  default end index value will be end of string if step value is +ve
->  default end index value will be start of string if step value is -ve
"""

str1 = "Python Programming"
print(str1[-1:-12:-1])  #gnimmargorP, Here its printed the reverse of the string
print(str1[-1:-19:-1]) #entire string reversed, gnimmargorP nohtyP
print(len(str1))  #18

print(str1[:12:-1]) #here it has negative index , so it will take in reverse, while the end index is positive,mming
print(str1[-1:-6:-1])#this is same as above, so it will go from -1 to -5 from negative, while from positive it wil be 12


print(str1[:5:-1]) #printing reverse of this , Programming
print(str1[-10:12]) #rogr

###############################################################################################

#24th Oct-25
#write a program to reverse the string
str_r = "Good Morning"
print(str_r[::-1]) #gninroM dooG
#slicing way of reverse string
#starting value is -1 and end index is beginning of teh string -1 and end index is -1
print(str_r[-1:-len(str_r)-1:-1])  #gninroM dooG, here the length is negative as its going in reverse
#above 2 gives same result, above 1 is internal execution of ::-1

print(str_r[::1]) #Good Morning
#start is 0 index and end if end of the string
print(str_r[0:len(str_r):1]) #Good Morning

print("_"*50)
#################################################################################











