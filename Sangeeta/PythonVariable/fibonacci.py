# Python program to check a given number is part of the Fibonacci series from 1 to 10

a = 0
b = 1
fib = []
while a <= 20:
    a, b = b, a+b
    fib.append(a)
print(", ".join(str(num) for num in fib))



