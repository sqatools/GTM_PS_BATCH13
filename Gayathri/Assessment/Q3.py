"""
Q3. Count Vowels in a String
Write a Python program that:
•	Takes a string as input from the user.
•	Counts how many vowels (a, e, i, o, u – both uppercase and lowercase) are present in the string.
•	Prints the total count of vowels.

"""
s1 = str(input("Enter the string: "))
vowels = "aeiouAEIOU"
count = 0 # taking an variable and settingit to 0 so can be used as reference further
for char in s1:
    if char in vowels:
        count += 1
        print("vowel values :", char)
print("The vowel count in string :", count)

"""
output :
Enter the string: my name is gayathri
vowel values : a
vowel values : e
vowel values : i
vowel values : a
vowel values : a
vowel values : i
The vowel count in string : 6
"""