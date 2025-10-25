print("Write a program to reverse a string without using slicing.")
print("."*100)

name=input("Enter string :")
rev= ''.join(reversed(name))
print(rev)

#####################################################################################
# USing a loop

reverse=""
for ch in name:
    reverse=ch+reverse
    print(reverse)
print(reverse)

