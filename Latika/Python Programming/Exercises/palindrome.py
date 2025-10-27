print("Write a program to check if a string is a palindrome")

# Slicing method
print("Using slicing")
print("."*100)

s=input("Enter the string: ")
if s==s[: : -1]:
    print(s,"Yes it is palindrome")
else:
    print(s,"No it is not palindrome")

# Use reversed()
print("."*100)
print("Using reversed()")
rev=''.join(reversed(s))
if s==rev:
    print("Yes")
else:
    print("No")

# Using loop
print("."*100)

print("Using loop")
reverse=""
for ch in s:
    reverse=ch+s
if s==reverse:
    print("Yes")
else:
    print("No")