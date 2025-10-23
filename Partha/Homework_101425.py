a = int(input("Enter the number: "))
print("The Square of ",a,"is",a**2)
print("The Cube of ",a,"is",a**3)

print("#"*50)

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=b
b=a
print("The 1st number is", c)
print("The 2nd number is", b)

print("#"*50)
import math
a=int(input("Enter the length of the 1st side of the right angle: "))
b=int(input("Enter the length of the 2nd side of the right angle: "))
print("As per pythagorean theorem the length of the hypotenuse of the right angle is", math.sqrt(a**2+b**2))

print("#"*50)
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("The value of the quadratic equation of (",a,"+",b,")^2 is", a**2+b**2+2*a*b)

print("#"*50)
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("The value of the quadratic equation of (",a,"-",b,")^2 is", a**2+b**2-(2*a*b))

print("#"*50)
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
print("The value of the quadratic equation of ",a,"^2 -",b,"^2 is", (a-b)*(a+b))
print("#"*50)

