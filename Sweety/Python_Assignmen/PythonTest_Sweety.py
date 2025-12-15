#Q1. Simple Calculator (Using if-else)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", n1 + n2)
elif op == "-":
    print("Result:", n1 - n2)
elif op == "*":
    print("Result:", n1 * n2)
elif op == "/":
    print("Result:", n1 / n2)
else:
    print("Invalid operator")

#Q2. Check Prime Number

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#Q3. Count Vowels in a String
name = (input("Enter a name: "))
vowel_count = 0
name = name.lower()

for ch in name:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        vowel_count = vowel_count+1
print("Vowel Count: ", vowel_count)

#Q4. List Operations – Even Numbers
numbers = [10, 3, 4, 7, 12, 15, 18]

for n in numbers:
    if n % 2 == 0:
        print(n)














