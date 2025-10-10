#Assignment 1 - Basic Python Program
# 9-Oct -25

 #1. Python Program to add two integer values.
i = 55
j = 20
print("Sum value of adding 2 integrers is :", i+j)
k = i + j
print("Sum value of adding 2 integers is :", k)

#2. Python Program to subtract two integer values.
print("diffrence of  2 integer value is :", i - j)
l = i - j
print(f"Difference of 2 integer value is : {l}")

#3. Python program to multiply two numbers.
print("product of 2 integers is :", i * j)

#4.  Python program to repeat a given string 5 times.
str1 = "SQATools"
print("String value is :", str1)
print("Repeated string value is :", str1 * 5)
#another way is
num = 5
print("Repeated string value is :",str1 *  num)

#5. Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number
a = 40
b = 50
c = 30
#Output : Average = 40
Sum = a + b + c
print("Total Value is :", Sum)
print("Average value of 3 numbers is : ", Sum // 3)

#6. Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
#Formula : (n+1)/2, n = Number of values
Input  = [45, 60, 61, 66, 70, 77, 80]
#first we need to sort
sorted_list = sorted(Input)
print("Sorted list is :", sorted_list)

Total= sum(sorted_list)
print("Total value is :", Total)
Median_Value = Total / len(Input)
print("Median value is :", round(Median_Value, 0))

#6. Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
#Formula : (n+1)/2, n = Number of values
# Steps to solve the program
# Take a list as input.
# Sort the given list using sort().
# Get the length of the list.
# If the length of the list is odd, then use the formula
# (n+1)/2 to find the median of the given list.
# If the length of the list is odd, then use the formula.
# Use the formula (n+1)/2 to find the median of the given list, where n is the length of the list.
# If the length of the list is even, then use the formula.
# Use the formula ((n/2 – 1) + n/2)/2 to find the median of the given list, where n is the length of the list
# Print the output.

list1 = [10, 20, 30, 40, 50,60]

#sort the list
list1.sort()

#get the length of the list
n = len(list1)
print("Length of list is :", n)

#here the length is odd, so follow the odd formula
if n%2 == 1:
    median_value = list1[n // 2]
else:
    median_value = (list1[n//2 - 1] + list1[n//2]) / 2
print(f"Median value is : {median_value}")

#7.Python program to print the square and cube of a given number.
#Input : num1 = 9
#Output :Square = 81, Cube =   729
num_new = 9
print("square of number 9 is :",num_new ** 2)
print("cube of number 9 is :",num_new ** 3)

#8. Python program to interchange values between variables.
#Input :a = 10, b = 20
#Output : a = 20, b = 10

a = 10
b= 20

temp = a # 10
a = b #a will get the value of b
print("value of a now is : ",a)

b = temp # b will have the value of temp, 10
print("value b is :", b)

######another way to handle this logic
x = 10
y = 20
x, y = y, x
print("value of x now is : ",x)
print("value y is :", y)

##### method 3 ###############
i = 10
j = 20
i = i + j #30
j = i - j # 10
i = i - j # 20
print("value of i now is : ",i)
print("value of j now is :", j)

#9. Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
a = 2
b = 3
c_value  = (a** 2) + (b**2)
print("value of c is : ",c_value)
#get the c2
c2 = c_value ** 2
print("value of c is : ",c2)

#10). Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab
a = 2
b = 3
lhs = (a + b) ** 2
rhs = (a **2) + (b**2) + (2 * a * b)
print("value of lhs is : ",lhs)
print("value of rhs is : ",rhs)
print(lhs == rhs)



