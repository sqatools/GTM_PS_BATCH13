print("And Operator & or Operator Programs and understanding")

"""
And Operator Logic
cond1 and cond2
true and false : false
false and true : false
false and false : false
true and true : true

OR Operator Logic
cond1 and cond2
true or false : true
false or true : true
false or false : false
true or true : true

> : greater than
< : less than
>= greater than equal to
<= less than equal to
= =: equal
!= : not equal
"""

print("Write a program to compare three values which is greater")

a=int(input("Please enter the first no :"))
b=int(input("Please enter the first no :"))
c=int(input("Please enter the first no :"))

if a>b and a>c:
    print(a,"is the greater no")
elif b>a and b>c:
    print(b,"is the greater no")
elif c>a and c>b:
    print(c,"is the greater no")
else:
    print("No number is greater")

########################################################################################################################
print("."*100)
print("Write a program to check given no is divisible by 3 AND 5")

num1=int(input("Enter the no"))
if num1%3==0 and num1%5==0:
    print(num1," is  divisible by 3 and 5")
else:
    print(num1," is not divisible by 3 and 5")
########################################################################################################################
print("."*100)
print("Write a program to check given no is divisible by 3 OR 5")

num2=int(input("Enter the no"))
if num2%3==0 or num2%5==0:
    print(num2," is  divisible by 3 or 5")
else:
    print(num2," is not divisible by 3 or 5")
########################################################################################################################
print("."*100)
print("Use of in operator")

list1=[3,5,10,6,11]
val1=int(input("Enter the value :"))
if val1 in list1:
    print(val1," is the present in the list")
else:
    print(val1," is not present in the list")
########################################################################################################################
print("."*100)
print("Use of not in operator")

str="Hello Guys, how are you ?"
val2=input("Enter the value")
if val2 not in str:
    print(val2," is not present in the list")
else:
    print(val2," is present in the list")
