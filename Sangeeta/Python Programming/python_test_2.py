# print("Count Vowels in a String \nTakes a string as input from the user.\n  Counts how many vowels (a, e, i, o, u – both uppercase and lowercase) are present in the string.\n  Prints the total count of vowels.")
#
# str1 = str(input("Enter a word of your choice :"))
# list1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U']
# count = 0
# str2 = ' '
# # Bazooka
# for char in str1:
#     if char in list1:
#         print(f 'char ' + char + ' is a vowel ')
#         count += 1
#     else:
#         print("This is not a vowel - ", char)
# print("Total count of char is :", count)

print("--*--"*50)

print("List Operations – Even Numbers - Write a Python program that: \n Takes n integers as input from the user and stores them in a list.\n From this list, creates another list containing only the even numbers.\n")
print("both the original list and the even-number list.")

list1 = []
list2 = []

for num in range(10):
    num = int(input("Enter a number of your choice : ", ))
    list1.append(num)
    print("list1 = ", list1)
int_value = 0
odd_no = []
for val in list1:
    val = val + int_value
    if val % 2 == 0:
        list2.append(val)
    else:
        odd_no.append(val)
print("These numbers from List 2 are not even but are odd numbers", odd_no)
print("List 2 numbers are even numbers = ", list2)

print("**---**"*50)

print("Write a python program- Takes names of student and marks for 3 subjects as input. \n Stores name in the form of dictionary {'name':<student_name>, 'marks':[m1,m2,m3]}")
print("Calculates the average marks. \n Print dictionary and average")

student1 = input()