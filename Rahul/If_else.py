num = int(input("Enter the number:"))
if num % 2 == 0:
    print("it is divisible by 2:", num)
elif num % 8 == 0:
    print("it is divisible by 8:", num)
elif num % 3 == 0:
    print("it is divisible by 3:", num)
else:
    print(" Not divisible by any number:", num)
