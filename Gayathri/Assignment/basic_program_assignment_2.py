#11. Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab

a = 3
b = 2
lhs = (a - b)**2
print("value of lhs :", lhs)
rhs = (a**2) + (b**2) - (2 * a* b)
print("value of rhs :", rhs)
if lhs == rhs:
    print("LHS and RHS are equal")
else:
    print("LHS and RHS are not equal")

print("*"*50)
#############################################################

#12. 12). Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
a = 3
b = 2
lhs = (a**2)- (b**2)
print("value of lhs :", lhs)
rhs = (a - b) * (a + b)
print("value of rhs :", rhs)
if lhs == rhs:
    print("LHS and RHS are equal")
else:
    print("LHS and RHS are not equal")

print("*"*50)
#################################################################
#13. 13). Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3