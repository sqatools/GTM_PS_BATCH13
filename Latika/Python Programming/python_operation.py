
print("Python Learning Session with Basic Arithmatic Operations")

print("If the variable value is same, the their address is also same.")
A=50
B=60
C=50
print("Value of A",A,id(A))
print("Value of B",B,id(B))
print("Value of C",C,id(C))


print("Rules to declare variables")

print("#1. There should not be space in the variable name")
print("#var 123=50     #invalid")
print("var_123=50      #valid")

#2. Can not start variable name with numer
#1_var=60    #invalid
var_1=50

#3. There is no limit for variable name

v=20
hello_friends_good_morning = 300

#4. Variable name can not contain special character expect _
#var$value =700
last_name='Dhanavade'

#5. Variable names are case sensitive

name ="Shalaka"
Name="Sweety"
NAME="Latika"
NAMe="Sadhna"
print(name,Name,NAME,NAMe)


################################Variable Operations##########################################

print("Addition of Values")
a1=30
a2=40

print("Addition of a1 and a2",a1+a2)
a3=a1+a2
print("Addition of a1 + a2",a3)

print("Subtraction")
print("Subtraction of a1-a2",a1-a2)

print("Multiplication")
print("Multiplication of a1*a2",a1*a2)

print("Division")
print("Division with single / of a1/a2",a1/a2)
print("Division with double // of a1//a2",a1//a2)

print("Remainder")
print("Remainder value ", a1%a2)

print("Power operator **")
print("Square of 5:",5**2)
print("Cube of 3:",3**3)

print("Compare 2 values with == equal to operator")
var1=50
var2=40
var3=50
print("Compare result of var1 ==var2:",var1==var2)
print("Compare result of var1 ==var3:",var1==var3)

print("Solve the (a+b)^2=a^2+b^2+2ab")
a=4
b=5
lhs=(a+b)**2
rhs=a**2+b**2+2*a*b
print("LHS value is:",lhs)
print("RHS value is:",rhs)
print("LHS and RHS is equal to ",lhs==rhs)






