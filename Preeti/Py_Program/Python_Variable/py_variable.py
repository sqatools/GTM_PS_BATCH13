#Python is dynamic language

a=10
b=20
c=a+b
print("value of c:",c)

#assign multiple values to multiple variable to at a time

x=10
y=11
z=12
print("x,y,z",x,y,z)

#assign one single value to multiple variables
p=q=r=100
print("value of p:","value of q:","value of r:", p,q,r)

#practicing
values=[1,2,3]
x,y,z=values
print(values)

#if the variable value is same , then thier address is also same (memory address)
a=10
b=3
c=10
print("value of a:",id(a))
print("value of b:",id(b))
print("value of c:",id(c))

###### There should not be space in variable name
#var 123=100
var_123=100

##### cannot start variable name with number
#1_var="hello"
var_1=100

##### there is no limit for variable name
hello_we_are_learning_program=30

##### variable name cannot take speacial characters
#var$_1=19
sur_name="Gurav"

#### Variable names are case sensitive

name="Raj"
Name="Ram"
NAME="Rohit"
print(name,Name,NAME)

################## VARIABLE OPERATIONS #####################

  #1) Addition
a=20
b=30
c=a+b
print("addition of c:", c)

  #2)Substraction
a=40
b=59
c=a-b
print("substraction of c:", c)

  #3)Multiplication
a=2
b=4
c=a*b
print("multiplication of c:",c)

  #4)Division
a=4
b=8
c=b%a
print("division of c:",c)

   #5)Reminder
a=60
b=21
c=a%b
print(c)

   #6)Power operation
print("square of 5:",5**2)
print("cube of 3:",3*3*3)

   #7)Compare 2 values with == equal to operation
val1=100
val2=100
print(val1==val2)
print(val1>val2)
print(val1<val2)
