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