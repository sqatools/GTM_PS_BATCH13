# Python program to print the square of the number if it is divided by 11.

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

# Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

str1 = 'Empathy'
str2 = ' '

for char in str1:
    str2 = print(str1.index(2)+str1.index(-3))
print(str2)

print ("-*-" * 50)