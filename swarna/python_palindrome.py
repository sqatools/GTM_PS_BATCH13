# This program checks if a given string is a palindrome.
x= input("Enter a string to check if it's a palindrome: ")
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome(x))