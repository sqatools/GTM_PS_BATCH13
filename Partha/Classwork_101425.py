a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if (a>b and a>c) and b!=c:
    print("First number is the largest number among the three numbers")
elif (b>a and b>c) and a!=c:
    print("Second number is the largest number among the three numbers")
elif (c>a and c>b) and a!=b:
    print("Third number is the largest number among the three numbers")
elif c==a and c==b:
    print("All numbers are the same")
elif b==c and (a>b or a>c):
    print("First number is the largest number and the other two are same")
elif a==c and (b>a or b>c):
    print("Second number is the largest number and the other two are same")
elif a==b and (c>a or c>b):
    print("Third number is the largest number and the other two are same")
elif a==b and c<a:
    print("First and Second number are same and larger than the third number")
elif b==c and a<b:
    print("Second and Third number are same and larger than the first number")
elif c==a and b<c:
    print("First and Third number are same and larger than the second number")