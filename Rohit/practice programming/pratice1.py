num = float(input("Enter the float number: "))
print(num)
if num.__float__():
    print("Given number is float")
elif num == 0.0:
    print("Given number is not float")