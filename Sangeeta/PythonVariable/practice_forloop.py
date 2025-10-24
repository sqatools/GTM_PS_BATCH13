x = [3, 4, 2, 42, 5, 4]
for i in range(len(x)):
    i = i+1
    print(i)
print("*"*50)

print ("Hello World")
# continue and break

#for i in range[10]
#for i == 3


#Write a python prg to find out if the given number is a prime number
# prime is only divisible by 1 and self. not divisible by any other number.
num = 13
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break
    else:
        continue
if prime:
    print("This is prime number", num)
else:
    print("This is not a prime number", num)

print("*"*50)

#= Write a prg to print star pattern triangle

for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    print()
print("*"*50)
print(" ")
# To print upside down triangle

for i in range(6, 0, -1):
    for j in range(1, i):
        print('*', end=' ')
    print()

print("*"*50)
print(" ")
# To print upside down triangle with numbers repeating instead of stars.. like
# 1
# 2,2
# 3,3,3
# 4,4,4,4
# 5,5,5,5,5

for i in range(1, 6, 1):
    for j in range(1,i+1):
        print(i, end =' ')
    print()





