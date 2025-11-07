a=25
b=40
c=a+b
print(c)
print("Value of c:" ,c)

print("-"*50)
#############Assign different value to different variable at a time###########
x,y,z=15,33,42
print(x,y,z)
print("value of x:",x)
print("value of y:",y)
print("value of z:",z)

print("value of y:",y)
print("value of z:",z)
print("value of x:",x)

print("-"*50)
################Assign same value to multiple variables################
p=q=r=35
print(p,q,r)

print("value of p:",p)
print("value of q:",q)
print("value of r:",r)

print("p:",p)
print("q:",q)
print("r:",r)

print("-"*50)
###########If the variable values is same, then their address is also same i.e.id(A)
# means memory#####
A=100
B=200
C=300
print("value of A:",A,id(A))
print("value of B:",B,id(B))
print("value of C:",C,id(C))

print("-"*50)
##############Variable name are case sensitive##################
name= "Rohit"
NAME= "Rohan"
nAME= "Jay"
NAMe= "Pushkar"

print(name,NAME,nAME,NAMe)

print("-"*50)
################################### Variable Operations #######################
# Addition of value  +
n1=10
n2=20
n3=n1+n2
print("value of n3:",n3)
print("Addition :", n3)
print("Addition of n1,n2:",n3)

# Multiplication *
a1=5
b2=25

print("Multiplication:",a1*b2)

# subtraction -
a1=20
b2=5
print("subtraction:",a1-b2)

# division /, //(by // decimal will get removed)
a1=12
b2=6

print("division:",a1/b2)  #2.0 #
print("division:",a1//b2) # 2 #

# remainder %
a1=13
b2=6
print("Remainder of divsion:", a1%b2) # 1 #

# power operator : **

print("square of 4:",4**2) # square of 4 : 16#
print("cube of 3:", 3**3) # cube of 3 : 27#

# compare 2 values with == equal to operator
val1= 20
val2= 10
val3= 20
print(val1==val2)
print(val1==val3)

###########question Home work##############
# (a+b)^2 = a^2 + b^2 + 2ab
a=4
b=6
lhs=(a+b)**2
rhs=a**2+b**2+2*a*b
print("square of (a+b):",(a+b)**2)
print("Result of lhs:",lhs)
print("Result of rhs",rhs)

print("-"*50)

###################################################################

#(a+b)^2 = a^2 + b^2 + 2ab
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print ("lhs:", lhs)
print("rhs :", rhs)