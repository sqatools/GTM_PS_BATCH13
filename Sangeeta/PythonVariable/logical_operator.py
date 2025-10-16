print("_"*50)
print("Write a program using logical operator to see which value is bigger")
a = int(input('Input a number for a : '))
b = int(input('Input a number for b : '))
c = int(input('Input a number for c : '))
if a > b and a > c:
    print(a, "is greater")
elif b > a and b > c:
    print(b, "is greater")
elif c > a and c > b:
    print(c, "is greater")
else:
    print("Greater # not found")
print("_"*50)

print("check if year is a leap year")
a = int(input("Input the year : "))
if a%4 == 0:
    print(a, "is a leap year ")
else:
    print(a, "is not a leap year")
print("_"*50)

print("check if a number is within range(1-100)")
a=int(input("Input a number : "))
print("A =", a+1)
if a > 100:
    print(a, "is out of range")
else:
    print(a, "is within range")