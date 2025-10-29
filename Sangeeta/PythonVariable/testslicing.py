#Test slicing rules.

str1 = 'Scarlet Knight'
print(str1[0:5])
print(str1[0:5:2])
print(str1[-1:-10])
print(str1[:-7:-1])
print(str1[:])


# Reverse string
str2 = "Good Morning"
print(str2[::-1])
print(str2[-1:-len(str2)-1:-1]) # This is elaboration of the reversal syntax mentioned above.

# Convert upper case to lower and vice versa.
# Use lower() and uperr() method

str3 = "hello tHERe"
print("Result for upper case ", str3.upper())
print("Result for upper case ", str3.lower())

# isupper() and islower() method
str4 = "Hello"
str5 = "PYTHOM"
str6 = "programming"
print("str4 :",str4.isupper(), str4.islower())
print("str5 : ",str5.isupper())

#capitalize method

# title method
str9 = "We are learning Python. Its easy to Learn."

# Count method - This would return total count of occurences of characters / substring in a string.
str10 = "We are learning Python. Its easy to Learn."
print("Count of e : ", str10.count('e'))
print("Count of ing : ", str10.count('ing'))

# Index() method : This method return the index postiion of the character / substring
str11 = "Good Morning, Hope you are doing good"
print("Index of hope :", str11.Index("hope"))