"""
numa = 250
numb = 20
print("Addition: ", numa +numb)
print("Subtraction: ", numa - numb)
print("Multiplication: ", numa*numb)
print("Division: ", numa//numb)


num = int(input("Enter a number: "))
count = 0
for i in range(1, num+1):
    if num%i == 0:
        count += 1

if count == 2:
    print("This is a prime number.")
else:
    print("This is not a prime number.")


char = input("Enter any letter: ")
vowel = ["a", "e", "i", "o", "u"]

if char in vowel:
    print("This is vowel.")
else:
    print("This is not vowel.")



n = int(input("Enter a number: "))
numbers = []
even_numbers = []

for i in range(n):
    num = int(input(f"(Enter a number {i+1}: )"))
    numbers.append(num)

for num in numbers:
    if num%2 == 0:
        even_numbers.append(num)

print("Original List: ", numbers)
print("Even Number List: ", even_numbers)

x = 5
y = 2
print(x // y)
"""

