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

# Conditional program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks")
print("_"*50)
print("If else program to assign grades as per total marks")
marks = int(input("Enter marks: "))
if marks<40:
    print("Since you secured less than 40, you failed")
elif marks>=40 and marks<=50:
    print("Since you secured marks in range of 41-50, you got grade C")
elif marks>50 and marks<=60:
    print("Since you secured marks in range of 51-60, you got grade B")
elif marks>60 and marks<=70:
    print("Since you secured marks in range of 61-70, you got grade A")
elif marks>70 and marks<+80:
    print("Since you secured marks in range of 71-80, you got grade A+")
elif marks>80 and marks<=90:
    print("Since you secured marks in range of 81-90, you got grade A++")
elif marks>90 and marks<=100:
    print("Since you secured marks in range of 91-100, you got Excellent grade")
else:
    print("Invalid marks")

print("_"*50)





