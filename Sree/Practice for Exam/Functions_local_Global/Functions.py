
def addition_values(x, y):
    result=x+y
    print(result)
addition_values(200,30)
a = 100
b = 200
def addition_values(a, b):
    return a + b   # or print(a + b)

result = addition_values(a, b)
print(result)
###########def bill_calculator():
Allfruit_price = {"Apple": 50, "Mango": 30, "Banana": 10, "Watermelon": 25, "lichi": 30, "Pinapple": 60}
fruit_purchased = {"Banana": 12, "Apple": 10, "Mango": 5, "Watermelon": 2}
total_bill=0
#for k,v in dict.items()
for fruits, purchased in fruit_purchased.items():
      Myfruits=Allfruit_price[fruits]
      myfruitbill= Myfruits*purchased
      total_bill =total_bill+myfruitbill
      print(fruits,':',Myfruits,purchased,":",myfruitbill)
print('Total bill:',total_bill)
###########   ################ function with default parameter ###########
# non default param has to come on left of the param list.
# default parma has to come on the right side of param list
def math_operation(n1, n2=20):
    print("n1 :", n1)
    print("n2 :", n2)
    print("addition :", n1+n2)
    print("multiplication :", n1*n2)
###############################     Function with return statement
def mul(n,m):
    return n*m
result=mul(5,5)
print(result)
###### print the string 10 times
def String(str1):
    print(str1*10)

string = input("Enter a string: ")

String(string)
##### print a table of a given number.
def table(n):
   a=0
   for i in range(1,11):
       a=i*n
       print(i,'*',n,'=',a)

## n = int(input("Enter a number: "))
table(5)
##########  aximum of three numbers.
def largest(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is the greatest number")
    elif b>a:
        if b>c:
            print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

largest(num1,num2,num3)
######## sum of all the numbers in a list.
def total(list1):
    t = 0
    for val in list1:
        t += val
    print("Sum of given list: ",t)

l = [6,9,4,5,3]
total(l)
### reverse a string
def rev(str1):
    a = str1[::-1]
    print("Reverse of the given string: ",a)

string = input("Enter a string: ")
rev(string)
##########check whether a number is in a given range.
def check(num):
    if num in range(2,20):
        print("True")
    else:
        print("False")
##num = int(input("Enter a number: "))
check(20)
#######l = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6] remove duplicate numbers
def remdup(list1):
    print(list(set(list1)))

list1 = [2, 2, 24, 5, 5, 6, 7]
remdup(list1)





