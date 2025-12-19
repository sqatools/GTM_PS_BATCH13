from fontTools.ufoLib import convertUFO1OrUFO2KerningToUFO3Kerning

sum1 = 0
for i in range(1,11):
    sum1 = sum1 + i
print("Sum of first 10 natural numbers is:", sum1)

#write a program to print all the values divisible by  3 and 5 between 1 to 50
for j in range(1,51):
    if j % 3 == 0 and j % 5 == 0:
        print(j)

list1 = [1,2,3,4,5,6]
for item in list1:
    print(item)

py_lib = ["Django", "Flask", "Pyramid", "Bottle", "numPy","pandas"]
for lib in py_lib:
   print("Python Library:", lib)

# while loop
num = 1
while True:
    print("Number is:", num)
    num += 1
    if num > 10:
        break

for i in range(10):
    if i == 3 or i == 5 or i==7:
        continue
    print("Value is:", i)

#break : break statement is used to terminate the loop
#continue : continue statement is used to skip the current iteration and continue with next iteration

#write a program to check whether a number is prime or not
number = int(input("Enter a number: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
    else:
        continue
if is_prime == True:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")