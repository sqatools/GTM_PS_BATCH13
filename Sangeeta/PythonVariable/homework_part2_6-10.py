n = "_"
print(n*75)

print("6. Python program to get the median of given set of numbers - [45, 60, 61, 66, 70, 77, 80].")
list1 = [45, 60, 61, 66, 70, 77, 80]
sortedlist = list.sort(list1)
n1 = len(list1)
print(n1)


print(n*75)
print(" ")

print("7. Python program to print the square and cube of a given number.")
num1 = 9
print("Value of num1 :", num1)
print("Square of num1=", num1**2)
print("Cube of num1=", num1**3)
print(n*75)

print("8. Python program to interchange values between variables.")
a=10
b=20
print("Value of a & B are", a, "&", b)
a, b = b, a
print("When values are interchanged, the new values would be")
print ("New Values of a & B are :", a, "&", b)
print(n*75)

print("9. Python program to solve the Pythagoras theorem.")
print("Theorem a2+b2=c2")
a = 8
b = 7
c = a*b
print("Value of a, b & c(a*b)=)", a, b, "&", c)
a2 = a**2
b2 = b**2
c2 = a2*b2
print("value of a2, b2 & c2 are", a2, b2, "&", c2)
print("Value of a square :", a**2)
print("Value of b square :", b**2)
print("Value of c square :", c2)

print("10. Python program to solve the given math formula.")
print("Solve the given formula : (a + b)2 = a^2 + b^2 + 2ab")
a = 5
b = 2
c = a+b
d = c**2
print("Value of (a+b)2 =", d)
print ("Compare this output  to the output from the calculation below")
a1 = a**2
b1 = b**2
c1 = 2*a*b
d1 = a1 + b1 + c1
print("Value of a^2", a1)
print("Value of b^2", b1)
print("Value of (a+b)2 =", c1)
print("The answer for a^2 + b^2 + 2ab =", d1)

print(d == d1)
print(n*75)






