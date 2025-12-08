"""Q2. Check Prime Number
Write a Python program that:
•	Takes an integer as input from the user.
•	Checks whether the number is prime or not prime.
•	Prints an appropriate message.
"""

num = int(input('Enter a number: '))
num_prime = False #flag to check if its prime or not
if num <= 1:
    num_prime = False
    print(f'{num} is not prime number.')
elif num == 2:
    num_prime = True
else:
    for i in range(3, num):
        if num % i == 0:
            num_prime = False
            break

if num_prime:
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')

