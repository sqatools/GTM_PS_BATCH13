print('#'*50,"Armstrong Number",'#'*50)
num=a=int(input("Enter your Number:"))
b=0
c=len(str(a))
while a>0:
    b=b+((a%10)**c)
    a=a//10
if b==num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

print('#'*50,"Armstrong Number",'#'*50)