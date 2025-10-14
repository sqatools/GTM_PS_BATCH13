# Write a prg. to check if a number is divisible by 3 or 4 or 10
print("_"*50)
x = 20
a = 3
b = 4
c = 10
print("Check if x", x, "is divisible by", a, "or",  b)
if x % 3 == 0:
    print("This is divisible by", a)
elif x % 4 == 0 :
    print("This is divisible by", b)
elif x % 10 == 0 :
    print("This is divisible by", c)
else:
    print("This is not divisible by any number")
print("_"*50)




