
# Writing program 
a=30
b=70
c=50
if a>b and a>c:
    print("A is largest:")
elif b>c and b>a:
    print("B is largest")
elif c>a and c>b:
    print("C is largest")
else:
    print("No one is largest")

############ in operator #########

list=[2,3,5,7]
n1=10
if n1 in list:
    print("n1 is there in list")
else:
    print("n1 is not there in list")

########## not in operator ############

str1="Hello world"
val="JAVA"
if val not in str1:
    print("val is not available in the string")
else:
    print("val is available in the string")

############# find vowels ############

ch=input("Enter character")
if ch.lower() in 'aeiou':
    print("Its Vowel")
else:
    print("Its not a Vowel")

