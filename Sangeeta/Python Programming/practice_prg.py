print("-*-" * 50)
print('\n Python program to print the square of the number if it is divided by 11.\n')

x = [11, 100, 22, 121, 55]
y = 11
z = []
i = 1
for i in range(len(x)):
    if x[i] % y == 0:
        a = x[i]
        print(a)
        print("The number" + str(a) + "is divisible by 11 and its square is = ", a ** 2)
        z.append(a)
    else:
        print ("The number" + str(a) + "is not divisible by 11")
print ("Numbers divisible by" + str(y) + "are in this list :", z)

print ("-*-" * 50)

print('\n Write a Python program to get a string made of the first and the last 2 chars from a given string.\n If the string length is less than 2, return instead of the empty string.\n')

str1 = 'Empathy'

print(str1[:2] + str1[-2]+str1[-1])
print(str1[:2] + str1[5]+str1[6])
print("Str 2 =", str1[:2])
print("Str3 = ", str1[5]+str1[6])
str4 = str1[-2:]*4
print("last 2 characters repeated 4 times :", str4)

print("-*-" * 50)

print('\n Python prg to construct half diamond pattern, using nested for loop \n')

x = [1,2,3,4,5,6]
y = 1

for i in range(len(x)):
   y = i+0
   z = y
   print(z*'*')
for j in range(len(x)):
    a = len(x)-j
    b = a
    print(b*'*')

print("-*-" * 50)

print("\n Write a prg. to print all numbers from 0 - 6 except 3 and 6 using python\n")

num = [1, 2, 3, 4, 5, 6, 7]
num2 = []
count = 0
for n in range(0, 7, 1):
    count += 1
    if count == 2:
       count = 0
       continue
    num2.append(n)

print(num2)



print("-*-" * 50)





