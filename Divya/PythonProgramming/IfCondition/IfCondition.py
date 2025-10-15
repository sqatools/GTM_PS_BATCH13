print("_"*30)
print("Write  a program to compare 3 values")

a= int(input("Please enter a number for a: "))
b= int(input("Please enter a number for b: "))
c= int(input("Please enter a number for c: "))

if a>b and a>c:
    print("a is the greatest among the three numbers")
elif   b> a and b> c:
    print("b is the greatest among the three numbers")
elif c>a and c> b:
    print("c is the greatest among the three numbers")
else:
    print("No number is the greatest among the three numbers" )
