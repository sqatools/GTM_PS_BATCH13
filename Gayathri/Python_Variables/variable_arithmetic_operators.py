#Class - 2 Variables - 09-10-2025
#############Variable Operations#########################

#1. Arithmetic operation (+)
a = 13
b = 2
print("Sum is :",a+b)
c = a + b
print("summation of a + b is  :",c)

#2. Subtraction (-)
print("Difference is :",a-b)
d = a - b
print("differnce of a - b :",d)

#3. Multiplication - (*)
print("Multiplication is :",a*b)
e = a * b
print("product of a * b is  :",e)

#4. Divsion (/)- Gives with floater points
#Divsion (//) - Gives the whole number - nearest 1st wholenumber value
print("Division with single slash is :",a/b)
f = a / b
print("Division with Double slash is  :",a // b)
g = a // b
print("Division with Float  is  :",f)
print("Division with Float removal is  :",g)

#5. Reminder (Mod operator - %)
print("Reminder of a/b is", a % b)
i = a % b
print("Remainder of a/b is", i)

#6. Expeonential (**)
print("Expenential of a sqaure is ", a**2)
j = a**2
print("Expenential of a is", j)

#7. compare 2 values with == equal to operator, return value is boolen value
num1 = 100
num2 = 200
num3 = 100
print(num1 == num2) #False
print(num1 != num2) #True
print(num1 == num3) #True

############# Question 1 : # (a+b)^2 = a^2 + b^2 + 2ab################
a = 6
b = 3
lhs = (a + b) ** 2
print("value of lhs is : ", lhs) #81

rhs = (a**2) + (b**2)+ (2 * a * b)
print("value of rhs is : ", rhs) #81

print(lhs == rhs) #True

