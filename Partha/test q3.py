myString = input("Enter a string: ")
count = 0
for char in myString:
    if char in ['a','e','i','o','u', 'A','E','I','O','U']:
        count += 1
print(myString, "has ", count, "vowels")