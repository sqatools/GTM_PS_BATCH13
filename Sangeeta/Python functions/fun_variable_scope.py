"""
local variable : variable we declare inside function is called local variable
It is limited to function and cannot use outside
global variable : variable we declare outside of function is called global variable, scope of global variable
non local variable
"""

var_x = 80

def func():
    var_y = 90
    print("global_var_x :", var_x)
    print("local var_y :", var_y)

def func2():
    var_Z = 100
    print("global_var_x :", var_x)
    print("local var_z :", var_z)

func()

##################

var_p = 300 #global variable

def order_function():
    var_q = 400 #nonlocal

    def inner_fun1():
        var_r = 500 #local
        print("var p :", var_p)
        print("var q :", var_q)
        print("var r :", var_r)

    def inner_fun2():
        var_r = 500 #local
        print("var p :", var_p)
        print("var q :", var_q)
        print("var s :", var_s)

    inner_fun1()
    inner_fun2()
