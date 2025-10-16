print("Hello World")
print("this is first")
num = 11
if num > 5:
    print("the number is invalid.")
else:
    print("the number is valid.")

print('_'*100)

age = 50

if age >= 65:
    print("The human is senior.")
elif age >= 18:
    print("The human is adult.")
elif age >= 6:
    print("The human is child.")
else:
    print("The human is infant.")

print('_'*110)

bodytemperature = 80

if bodytemperature > 106:
    print("Invalid temperature.")
elif bodytemperature >= 104:
    print("Very high fever, take a cold water shower.")
elif 100 <= bodytemperature < 104:
    print("Fever detected, take medicine.")
elif 99 <= bodytemperature <= 98:
    print("No fever, enjoy!")
elif bodytemperature <= 97:
    print("Invalid temperature.")
else:
    print("Unable to determine condition.")


a = 5
b = 90
c = 10

if a > b and a > c:
    print("a is greater than b abd c")
elif b > a and b > c:
    print("b is greater than b and c")
elif c > a and c > a:
    print("c is greater than b and c")
else:
    print("There is no greater in a, b and c")

print('_'*90)

var1 = input("Please enter your number : ")
print(var1, type(var1))
num1= int(var1)
print(num1, type(num1))

print("-"*50)

list1 = [5, 7, 9 , 23, 56]
n1 = 9

if n1 in list1:
    print("n1 is available in the list1")
else:
    print("n1 is not available in the list1")
