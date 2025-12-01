
num=int(input("Enter the no :"))
flag=True

for i in range(2,num):
    if num%i==0:
        flag=False
    else:
        break
if flag:
    print(num, "Number is prime")
else:
    print(num, "Number is Not prime")

