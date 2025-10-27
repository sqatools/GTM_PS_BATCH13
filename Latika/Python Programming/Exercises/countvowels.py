print("Write a program to count the number of vowels in a string.")
print("."*100)

string=input("Enter the string: ")
vowels=0
for i in string:
    if(i=='a' or i=='e'or i=='i'or i=='o'or i=='u'):
        vowels=vowels+1
        print(i)
print("Number of vowels are:")
print(vowels)

########################################################################
print("."*100)

vowels1="aeiouAEIOU"
count=0
for ch in string:
    print(ch)
    if ch in vowels1:
        count=count+1
    else:
        continue
print("Total vowels :",count)