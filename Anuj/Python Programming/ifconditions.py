round1= "pass"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("round 1 is cleared")
    if round2 == "pass":
        print("round 2 is cleared")
        if round3 == "pass":
            print("round 3 is cleared")
        else:
            print("round 3 not cleared")
    else:
     print("round 2 not cleared")
else:
    print("round 3 not cleared")

a =10
b=20
if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b")

num = 15
if num % 2 == 0:
    print("The number is even",num)
else:
    print("The number is odd",num)

list1 = [10,20,30,40,50]
n= 20
if n in list1:
    print(n,"is present in the list")
else:
    print(n,"is not present in the list")

a=80
b=60
c=70

if a>b and a>c:
    print("a is the greatest",a)
elif b>a and b>c:
    print("b is the greatest",b)
elif c>a and c>b:
    print("c is the greatest",c)
else:
    print("no one is greatest")

