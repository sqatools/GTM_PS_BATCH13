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

###################################################################################################
print("."*100)

# properties
# List is mutable datatypes
# List can contain any types of data
# e.g. int,float,string,complex,tuple,list,boolean,dict,set
# List follows positive and negetive indexing
# List contain value in square bracket

list1=[1,4.5,"python",[4,5],(3,5),{'a':345},True]
print(list1,type(list1))
print(list1[2])

print("MultiIndexing")
list2=[20,[4,8],True]

print(list2[-2])
print(list2[-2][1])

list2.append(50)
print("list2:",list2)

print("."*100)
print("Tuple")

# properties
# tuple is immutable datatypes
# tuple can contain any types of data
# e.g. int,float,string,complex,tuple,list,boolean,dict,set
# tuple follows positive and negetive indexing
# List contain value in round bracket
# When we want to keep data constant we should use tuple

tup1=(4,7.9,'python',[6,7],{'a':345},True)
print(tup1,type(tup1))
print(tup1[4])

# print(tup1[4][1])

print(tup1[-4][-1])
print(tup1[-4])
##########################################################################################
print("."*100)
print("Dictionary")

# properties
# dict is mutable datatypes, we can modify any point of time
# dict contain data in curly braces in key value pair e.g {key:value}
# dict contains unique keys, duplicate keys are not allowed.
# {'a':123,'b':456,'a':789}
# if we mention the duplicate then it will only consider the latest defined value.
# Only immutable data can be key in the dict
# Not allowed as a key - list,dict,set
# dict value can contain any types of data
# dict not following the index

dict1={'a':123,
        'b':345,
        'c':678}
print(dict1,type(dict1))
print(dict1['a'])

##########################################################################################
print("."*100)
print("Set")

# Set is mutable data types we can modify any point of time
# Set on;y store unique values, duplicate data is now allowed
# Set stored values in curly braces
# only immutable data types allowed
# List allowed a set member
set1={2,3.4,60+4j,True,2,3.4}
print(set1,type(set1))

##########################################################################################
print("."*100)
print("Boolean")

# Boolean is a immutable datatypes
# Boolean contains value true or false
# Boolean is result of any conditional o/p

var1=True
var2=False
print(var1,type(var1))
print(var2,type(var2))




