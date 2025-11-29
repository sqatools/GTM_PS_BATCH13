string1=input("Enter the string :")
count=0

for ch in string1:
    if ch in 'aeiou':
        count=count+1

print("Count is :",count)