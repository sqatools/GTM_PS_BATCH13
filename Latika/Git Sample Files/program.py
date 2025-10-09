print("Even and ODD program")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit(1)

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")