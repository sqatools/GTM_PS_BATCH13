# Simple Calculator using if-else (no user input)

num1 = 2
num2 = 4
# Performing operations using if-else
# Addition
operator = "+"
if operator == "+":
    print("Addition:", num1 + num2)

# Subtraction
operator = "-"
if operator == "-":
    print("Subtraction:", num1 - num2)

# Multiplication
operator = "*"
if operator == "*":
    print("Multiplication:", num1 * num2)

# Division
operator = "/"
if operator == "/":
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: Error (division by zero)")


# Check Prime Number

num = 5

# Prime number check
if num > 1:
    # Loop from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")





