
a = 10

b = 20

print(a)
print(b)

################################## Assign different value to different variables at a time #######
p, q, r = 10, 20, 30
print("value of p :", p)
print("value of q :", q)
print("value of r :", r)


########### assign same value to multiple variables #######
x = y = z = 100
print(x, y, z) # 100 100 100


############
# If the variable value is same, then their address is also same
A = 50
B = 70
C = 50

print("value of A :", A, id(A)) # 50 140730549828040
print("value of B :", B, id(B)) # 70 140730549828680
print("value of C :", C, id(C)) # 50 140730549828040



############################ Rule to delclare variable ##############################

# 1. There should not be space in variable name
# var 123 = 50  # invalid
var_567 = 10  # valid

# 2.  can not start variable name with number

# 1_var = 400 # invalid
# var_1 = 500

# 3. there is no limit for variable name.
v = 20
hello_we_are_learning_programming = 300


# 4. Variable name can not contain special character except _
# var$value = 700  # invalid
sur_name = 'Gupta'  # valid
#full-name = "Dwijesh" #  invalid
# last=name = # invalid


# 5. Variable name are case sensitive.
name = "Rahul"
Name = "Mohit"
NAME = "Raj"
NAMe = "Raghu"
name = "Sangeet"

print(name, Name, NAME, NAMe) # Rahul Mohit Raj Raghu


################################### Variable Operations #######################
# Addition of value  +
n1 = 40
n2 = 50
print("Addition :", n1+n2)
n3 = n1+n2
print("Addition of n1, n2 :", n3)

# Multiplication *
a1= 40
a2 = 5
print("Multiplication :", a1*a2)


# subtraction -
b1 = 500
b2 = 200
print("subtraction value :", b1-b2)

# division /, //
c1 = 40
c2 = 3
c3 = 7

print("division with single /:", c1/c2)  # 13.333333333333334
print("division with double //:", c1//c3)  # 5

# remainder %
x1 = 12
x2 = 5
print("Remainder value :", x1%x2) #  2


# power operator : **
print("square of 5 :", 5**2) # square of 5 : 25
print("cube of 6 :", 6**3)  # cube of 6 : 216


# compare 2 values with == equal to operator
val1 = 100
val2 = 200
val3 = 100

print(val1 == val2) # False
print(val1 == val3) # True


####################### questions ##############
# (a+b)^2 = a^2 + b^2 + 2ab
a = 5
b = 6
lhs = (a+b)**2
print("lhs :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs :", rhs)

print(lhs == rhs)  # True


###################### Home work ############

