a = 10
b = 20
print("Values for a,b = ", a, b)
print (a == b)
if a == b:
    print("Both values are equal")
else:
    print("Both values are not equal")

print("_"*50)

# write a program to check if given number is equal or not
num1 = 12
print("Value for num1 =", num1)
if num1 % 2 == 0:
    print("This is even number", num1)
else:
    print("This is odd number", num1)
print("_"*50)

#Write a Python prg to check if given number is divisible by 3,5 or 7
x = 15
print("Value of x=", x)
if x % 3 == 0:
    print("This is divisible by 3")
elif x % 5 == 0:
    print("This is divisible by 5")
elif x % 3 == 0:
    print("This is divisible by 3")
else:
    print("This is not divisible by any number ")
print("_"*50)

# Nested if condition
# Write a prog with nested if condition and provide solution for interview process.

round1 = "pass"
round2 = "fail"
round3 = "pass"
print ("Values for round1, round 2, round3 are ", round1, round2, round3)
if round1 == "pass":
    print("Congrats, first round cleared")
    if round2 == "pass":
        print("Congrats, second round cleared")
        if round3 == "pass":
            print("Congrats, final round cleared")
        else:
            print("Failed in 3rd round, try next time")
    else:
        print("Failed in 2rd round, try next time")
else:
    print("Failed in first round, try next time")
print("_"*50)

# Write a one line if statement to see if the number is even or not.
var1 = 20
print("Value for var1=", var1)
result = "even" if var1 % 2 == 0 else "odd"
print("Result to identify if var1 is even or odd:", result)
print("_"*50)