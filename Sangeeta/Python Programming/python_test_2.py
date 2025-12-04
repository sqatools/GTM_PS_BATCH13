# print("Count Vowels in a String \nTakes a string as input from the user.\n  Counts how many vowels (a, e, i, o, u – both uppercase and lowercase) are present in the string.\n  Prints the total count of vowels.")
#
# str1 = str(input("Enter a word of your choice :"))
# list1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']
# count = 0
# str2 = ' '
# # Bazooka
# for char in str1:
#     if char in list1:
#         print(f'char ' + char + ' is a vowel ')
#         count += 1
#     else:
#         print("This is not a vowel - ", char)
# print("Total count of char is :", count)

print("-*-"*50
      )
print("List Operations – Even Numbers - Write a Python program that: \n Takes n integers as input from the user and stores them in a list.\n From this list, creates another list containing only the even numbers.\n")
print("both the original list and the even-number list.")

list1 = []
list2= []

for num in range(10):
    num = int(input("Enter a number of your choice : ", ))
    list1.append(num)
    print(list1)

