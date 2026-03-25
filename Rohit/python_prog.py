s = "Rohit Ramchandra Chavan"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

with open("TestFile.txt","r") as f:
    data = f.read()
    print(data)

with open("TestFile.txt","w") as f:
    f.write("I am Rohit Ramchandra Chavan 334455")


n =5
a, b = 0 ,1

for _ in range(n):
    print(a,end='')
    a,b = b, a+b

num = 7
if num > 1:
    for i in range(2,num):
        if num%i==0:
            print("Prime Number")
    else:
        print("Not Prime Number")