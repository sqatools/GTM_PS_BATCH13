stra= "python"
print(stra[2:4])  #th
##################################
print(""*44)
print()
str_b="MEMO BOOK"
#print(str_b[:6])
print(str_b[1:])   #EMO BOOK
##################################
print(""*44)
print()
Name="Sree"
age=30
Address="USA"

Info=f"My name is {Name} and age is {age},address is {Address}"
print(Info)
############################################
print("-"*44)
print()
###reverse entire string
str1= "Morning all"
print(str1[: : -1])
print(str1[::1])
print("-"*44)
print()
# lower() and upper() method :
str2="     we are learning python"
print(str2.upper())
print(str2.lower())
print(str2.capitalize())
print(str2.isupper())
print(str2.islower())
print(str2.swapcase())
print(str2.title())
print(str2.count("e"))
print(str2.index("are"))
print(str2.replace("python","Java"))
print(str2.strip())  #removes whitespace (or other specified characters) from both the beginning and end of a string.

print(str2.find("java"))             ##the index (position) of the first occurrence of substring, or
print(str2.strip())
str3="Password 1234"
str4="#$%^".join(str3)
print(str4)
list=["Hello ","How ","are ","You ""ornage,""apple,"'grape,']
Result="".join(list)
print(Result)

                                   ##-1 if the substring is not found.
#Q1 write a python program to remove duplicate words from given string.
str1= "Ram Sham Ram Rani Sham Kash "
a= str1.split()
print(a)
b = ""
for c in a :
    if c not in b:
        b=b+c+ "  "
    else:
         continue
print(b)

print("-"*44)
print()


