################## If variable value is same, then their address is also same #############
a = 10
b = 20
c = 10
print("value of a", a, "Memory allocated to a is", id(a))
print("value of b", b, "Memory allocated to b is", id(b))
print("value of c", c, "Memory allocated to c is", id(c))

############################ Variable Operations ##################################################
num1 = 44
num2 = 2

#Addition
print("addition of num1 and num2", num1+num2)

#Subtraction
print("subtraction of num1 and num2", num1-num2)

#Division
print("division of num1 and num2", num1/num2)  # / It will print decimal value
print("division of num1 and num2", num1//num2)  # // It will print whole value


#Multiplication
print("multiplication of num1 and num2", num1*num2)

#Remainder
print("remainder of num1 and num2", num1%num2)

#Power Operator **
print("square of num1", (num1**2))
print("cube of num2", (num2**3))

#Compare two values with == operator
if (num1==num2):
    {
        print("both values are same")
    }
else:
    {
        print("both values are different")
    }