"""num=int(input("enter a number"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
    else:
        continue
if prime==True:
    print("It is a Prime number")
else:
    print('not a prime number')
################################################

string = input("Enter a string: ")

vowels = "aeiousAEIOU"

count = 0


for char in  string:
    if char in vowels:
        count += 1

print("Total number of vowels:", count)


n = int(input("enter even numbers"))

numbers = []
even_numbers = []

for i in range(n):
    num = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)


for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Oral List:", numbers)
print("Eve Numbers List:", even_numbers)


name = "Ram"
mar1 = 85
mar2 = 90
mar3 = 80


student = {
    "name": name,
    "marks": [mar1, mar2, mar3]
}

average = (mar1 + mar2 + mar3) / 3

print("Student Data:", student)
print("Average Marks:", average)
########################################
num1 = 10
num2 = 5
operator = input("Enter the operator: ")

if operator == '+':
    result = num1 + num2
    print("addition val:", result)
elif operator == '-':
    result = num1 - num2
    print("subtraction val:", result)
elif operator == '*':
    result = num1 * num2
    print("multiplication val:", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("division val:", result)
    else:
        print("valid")
else:
    print("Invalid operator")
"""""
x = 5

y = 2

print(x // y)

a = 10

b = 20

a, b = b, a

print(a, b)
