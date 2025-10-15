####Doubt 2,6,8

# 1). Python program to check given number is divided by 3 or not.
a = 18
if a%3 == 0:
    print(a, "is divided by 3")
else:
    print(a, "is not divided by 3")

print("_"*100)

#3). If else program to assign grades as per total marks.
marks = 101
if marks < 40:
    print("fail")
elif marks >= 40 and marks <= 50:
    print("grade C")
elif marks >= 50 and marks <= 60:
    print("grade B")
elif marks >= 60 and marks <= 70:
    print("grade A")
elif marks >= 70 and marks <= 80:
    print("grade A+")
elif marks >= 80 and marks <= 90:
    print("grade A++")
elif marks >= 90 and marks <= 100:
    print("grade Excellent")
else:
    print("Invalid marks")

print("_"*100)

#4). Python program to check the given number divided by 3 and 5.
b = 7
if b%3 == 0 and b%5 == 0:
    print(b, "is divisible by 3 and 5")
elif b%3 == 0:
    print(b, "is divisible by 3")
elif b % 5 == 0:
    print(b, "is divisible by 5")
else:
    print(b, "is not divisible by 3 and 5")


print("_"*100)
#5). Python program to print the square of the number if it is divided by 11.

c = 55
if c%11 == 0:
    print("Square root of c is: ", c**2)
else:
    print("c is not divisible by 11")

print("_"*100)
#7). Python program to check given number is odd or even.

d = 33
if d%2 == 0:
    print(d, "is even number")
else:
    print(d, "is odd number")

print("_"*100)
#9). Python program to check authentication with the given username and password.

username = "xyz"
password = "xyz6"
if username == password:
    print("User logged in successfully")
else:
    print("Invalid username or password")

print("_"*100)
#10). Python program to validate user_id in the list of user_ids.

user_id = [1, 2, 3, 4, 5]
id = 10

if id in user_id:
    print(id, "is valid id")
else:
    print(id, "is not valid id")

print("_"*100)
#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

e = 7
if e % 2 == 0:
    print(e, "is divisible by 2 therefore square root of", e, "is: ", e**2)
elif e % 3 == 0:
    print(e, "is divisible by 3 therefore cube of", e, "is: ", e ** 3)
else:
    print(e, "is not divisible by 2 and 3")

print("_"*100)












