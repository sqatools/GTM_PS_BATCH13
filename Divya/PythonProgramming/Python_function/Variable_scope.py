"""
local vairable
global vairable
nonvlocal vairable

"""
var_x = 10
def fun1():
    var_y = 20
    print("global variable:",var_x)
    print("local variable:",var_y)
def fun2() :
    var_z = 30
    print("global variable:", var_x)
    print("local variable:", var_z)
