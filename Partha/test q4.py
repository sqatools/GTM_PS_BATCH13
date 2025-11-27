
# Take n integers as input and store them in a list
n = int(input("Enter how many numbers you want: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Create a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Print both lists
print(numbers)
print(even_numbers)