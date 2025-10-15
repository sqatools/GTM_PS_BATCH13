
n = "_"
print(n*75)

print("Python program to solve the given math formula.")
print("Solve the given formula :  (a + b)3 = a3 + 3ab(a+b) + b3")
a = 4
b = 3
c = a+b
d = c**3
e = a*b
print("Value of (a+b)3 =", d)
print ("Compare this output  to the output from the calculation below")
a1 = a**3
c1 = 3*e*c
b1 = b**3
d1 = a1 + c1 + b1
print("Value of a3 =", a1)
print("Value of 3ab(a+b) =", c1)
print("Value of b3 =", b1)

print("The answer for a3 + 3ab(a+b) + b3 =", d1)
print(d == d1)
print(n*75)

print("Solve the given formula :  (a – b)3 = a3 – 3a2b + 3ab2 – b3")
a = 6
b = 2
c = a-b
d = c**3
print("Value of a,b,c,d =", a, b, c, d)
print("Value of (a-b)3 =", d)
print("Compare this output  to the output from the calculation below")
a1 = a**3
b1 = b**3
c1 = 3*(a**2)*b
d1 = 3*a*(b**2)
e1 = a1 - c1 + d1 - b1
print("Value of a3 =", a1)
print("Value of 3a2b =", c1)
print("Value of 3ab2 =", d1)
print("Value of b3 =", b1)

print("The answer for a3 - 3a2b + 3ab2 - b3 =", e1)
print(d == e1)

print(n*75)

print("Python program to calculate the area of the square.")
print(''' Since all sides of a square are equal, you only need measurement of 1 side.
      So the formula is : area = side1*side1''')
side1 = 15
print("Measurement of side1 in cm =", side1)
area = side1*2
print("Area of square is =", area, "cm")
print(n*75)

