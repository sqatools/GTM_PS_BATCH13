#Write programme for count the vowels

str1= "Good morning, Hope you are doun good"
vowels ="aeiouAEIOUE"
count = 0
for char in str1:
    print (char)
    if char in vowels:
        count +=1
    else:
        continue
print("Total count of vowels:", count)
        