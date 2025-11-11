var_B = 400 #global variable
var_A = 500 #global variable
#now we have 2 global variables - module 1 - A = >var_A = 400
#module 3 - var_A = 500,

def multiply(n1, n2):
    print("Multiply:", n1*n2)

def division(n1, n2):
    print("division:", n1//n2)

#now lets call these methods in module2