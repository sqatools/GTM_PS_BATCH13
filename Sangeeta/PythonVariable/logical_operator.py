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

