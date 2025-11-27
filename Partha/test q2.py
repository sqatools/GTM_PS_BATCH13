num=int(input("Enter a number: "))
rem = 0
for i in range (1,num+1):
    if i == 1 or i == num:
        continue
    rem = num % i
    if rem == 0:
        break
    i+=1
if(rem != 0):
        print(num, "is a prime number")
else:
    print(num,"is not a prime number")