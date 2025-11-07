####Program with and operator############
# Write a program to compare three values is greater with and operator
##Below is logic of and operator
#True and False= False
#False and True= False
#False and False=False
#True and True=True

a= 50
b= 60
c= 80
if a>b and a>c:
    print("a value is greater value:",a)
elif b>a and b>c:
    print("b value is greater value:",b)
elif c>a and c>b:
    print("c value is greater value:",c)
else:
    print("None of value is greater value")

a = 50
b = 85
c = 80
if a > b and a > c:
    print("a value is greater value:", a)
elif b > a and b > c:
    print("b value is greater value:", b)
elif c > a and c > b:
    print("c value is greater value:", )
else:
    print("None of value is greater value")
print("-"*50)

################################################################
#write a program to check given number is divisible by 3 and 5 with and operator

val1= input("Please enter the Number:")
print(val1, type(val1))
num1=int(val1)
print(num1,type(num1))

if num1%3==0 and num1%5==0:
    print("The number is divisible by 3 and 5",num1)
else:
    print("The number is not divisible by 3 and 5:",num1)
print("-"*50)

    ####Program with or operator############
##Below is logic of and operator
#True and False= True
#False and True= True
#False and False=False
#True and True=True

num1=int(input("Please enter the Number"))
if num1%3==0 or num1%5==0:
    print("The number is divisible by 3 or 5:",num1)
else:
    print("The number is not divisible by 3 or 5:",num1)

print("-"*50)

###########################In operator#############
#write a program with In operator
list1= (1,5,8,34,66)
n1=9
if n1 in list1:
    print("n1 number present in list1")
else:
    print("n1 number not present in list1")
print("-"*50)

list1 = (1, 5, 8, 34, 66)
n1 = 34
if n1 in list1:
    print("n1 number present in list1")
else:
    print("n1 number not present in list1")

print("-"*50)

###########################Not In operator#############
#write a prigram with Not In operator

str= "Hello Guys join the python"
num1= "Rohit"
if num1 not in str:
    print("num1 number not present in str")
else:
    print("num1 number present in str")
print("-"*50)


str= "Hello Guys join the python"
num2= "python"
if num2 not in str:
    print("num2 number not present in str")
else:
    print("num2 number present in str")
print("-"*50)



str= "Hello Guys join the python"
num2= "Hello"
if num2 not in str:
    print("num2 number present in str")
else:
    print("num2 number not present in str")
print("-"*50)