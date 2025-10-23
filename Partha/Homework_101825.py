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

print('#'*50,"Factorial",'#'*50)
num=int(input("Enter your Number:"))
num2=num
fact = 1
while num>0:
    fact = fact*num
    num=num-1
print('The Factorial of ',num2,'is',fact)

print('#'*50,"Fibonacci",'#'*50)
num1=0
num2=1
count=0
range1=int(input("Enter your range:"))
print("The Fibonacci sequence upto",range1,"is")
while count<range1 and num1<=range1:
    print(num1)
    num3=num1+num2
    num1 = num2
    num2=num3
    count+=1
