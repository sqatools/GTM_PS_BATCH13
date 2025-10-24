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


