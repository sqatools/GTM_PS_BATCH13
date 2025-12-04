"""
Write a Python program that:
•	Takes n integers as input from the user and stores them in a list.
•	From this list, creates another list containing only the even numbers.
•	Prints both the original list and the even-number list.
________________________________________

"""

#creating an empty list so as to append it further with value
list1 = []
list_even = [] #created one more list to store even values
list_odd = []  #created to store odd values

# lets check with user - how many integers he wants to provide
n = int(input("number of integers you want to key in: "))
num = int(input("key in a number: "))
#now using for loop to run it as per the number of inetgers keyed in by user
for i in range(n):
    #we got just 1 number from the user, but we want a list , so lets increment that number
    num = i + num
    print("Number value is : ", num)
    list1.append(num)
    print("The original list is : ", list1)

    #now we want to see if number is even or odd
if num % 2 == 0:
    list_even.append(num)
    print("The Even list is : ", list_even)
else:
    list_odd.append(num)
    print("The list odd is : ", list_odd)

"""
Output:
number of integers you want to key in: 4
key in a number: 2
Number value is :  2
The original list is :  [2]
Number value is :  3
The original list is :  [2, 3]
Number value is :  5
The original list is :  [2, 3, 5]
Number value is :  8
The original list is :  [2, 3, 5, 8]
The Even list is :  [8]

-----------------------------------------------------------------
number of integers you want to key in: 4
key in a number: 3
Number value is :  3
The original list is :  [3]
Number value is :  4
The original list is :  [3, 4]
Number value is :  6
The original list is :  [3, 4, 6]
Number value is :  9
The original list is :  [3, 4, 6, 9]
The list odd is :  [9]

"""






