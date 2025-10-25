print("Write a program to replace spaces with hyphens in a string.")

string=input("Enter string :")
string=string.replace(" ","_")
print("Replaced string is:")
print(string)

print()
print("Write a program to extract digits from a given string.")
test_string="Hello Where are you called 2 times now it's 4 oclock"

numbers=[]
for char in test_string:
    if char.isdigit():
        numbers.append(int(char))
print("The numbers are:",numbers)