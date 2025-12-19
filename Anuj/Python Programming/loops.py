sum = 0
for i in range(1,11):
    sum = sum + i
print("Sum of first 10 natural numbers is:", sum)

#write a program to print all the values divisible by  3 and 5 between 1 to 50
for j in range(1,51):
    if j % 3 == 0 and j % 5 == 0:
        print(j)

list1 = [1,2,3,4,5,6]
for item in list1:
    print(item)

py_lib = ["Django", "Flask", "Pyramid", "Bottle", "numPy","pandas"]
for lib in py_lib:
   print("Python Library:", lib)