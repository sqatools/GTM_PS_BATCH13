#######################Python DataTypes###############################

# Integer is immutable data types
# Integer only contains whole number
# There is no range limit for integer

print("First python data type is Integer")
num1=0
num2=400
num3=1234567890

print("num1:",num1,type(num1))
print("num2:",num2,type(num2))
print("num3:",num3,type(num3))

#########################################################################
# Float is immutable data types
# Float contains pointer/decimal value
# There is no range limit for Float

print("Second Data Type is Float")
f1=0.0
f2=11.89
f3=98765432.1234567
print("f1 is:",f1,type(f1))
print("f2 is:",f2,type(f2))
print("f3 is:",f3,type(f3))

############################################################################

# Complex is immutable data types
# Complex number is combination of real and imaginary number e.g. x+yj
# There is no range limit for Complex

print("Third Data Type Is Complex")
comp1=10+20j
comp2=0+1j
print(comp1,type(comp1))
print(comp2,type(comp2))
print("Real value is:",comp1.real)
print("Imag value is:",comp1.imag)

##############################################################################
# String is immutable data types
# We can define a string with single/double/triple quote
# String follows positive and negetive indexing
# There is no range limit for String

#   """
#   0   1   2   3   4   5               +Ve Indexing
#   P   Y   T   H   O   N
#  -6  -5  -4  -3  -2  -1               -Ve Indexing
#   """

print("Fourth Data Type Is String")
s1='a'
s2="Hello"
s3="""Three string we used to assign a paragraph value """

print("Single char string",s1)
print("Double string",s2)
print("Triple String",s3)

