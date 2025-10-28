# String formatting

name = "Maha"
age = "30"
city = "Chennai"

result = "My name is Maha and age is 30, I live in  Chennai"

# 1.  string concatenation:
result1 = "My name is "+name+" and age is "+str(age)+", I live in "+city
print(result1)

# 2.  format method:
result2 = "My name is {} and age is {}, I live in {}".format(name, age, city)
print(result2)


# 3.  fstring formatting method:
result3 = f"My name is {name} and age is {age}, I live in {city}"
print(result3)

###
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

"""

str_b = "Learning"
print(str_b[0:5])  # Learn

# In this rule user can read sub string from left to right only.
str_c = "Maha Lakshmi"
print(str_c[5:1])  # blank output as can not move from right o left
print(str_c[-5:-1])  # kshm
print(str_c[-5:])  # kshmi
print(str_c[-13:-6])  # Maha L
print(str_c[:7])  # Maha La
print(str_c[1:]) # aha lakshmi
print(str_c[:]) # Maha Lakshmi

"""
Rule2 = str[start index: end index: step value]
->  Output will include the start index value and exclude last index value.
->  In this rule user can read sub string from left to right or right left.
->  start index and end index could be +ve or -ve
->  and step value also could be +ve or -ve
->  default start index will be -1 if step value is -ve.
->  default start index will be zero if step value is +ve
"""


                   #12
str1 = "Python Programming"
                   #-6
print(str1[-1:-12:-1])  # gnimmargorP
print(str1[-1:-12:-2]) # gimroP
print(str1[-1:-12:-12]) # g


#default start index will be -1 if step value is -ve.
print(str1[:12:-1])  # gnimm
print(str1[:12:1])  # Python Progr
print(str1[-1:-6:-1]) # gnimm


print(str1[:12:1])  # Python Progr

print(str1[-10:16])









