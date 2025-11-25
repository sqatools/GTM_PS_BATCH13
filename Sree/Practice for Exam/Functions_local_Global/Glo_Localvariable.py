"""
local variable:  variable we declare inside the function is called the local variable
                 ->  local variable scope is limited to the function, can not use outside of the function.
                 ->  we can define global variable inside the function using the global keyword.
global variable :  variable we declare outside of the function is called global variable, the scope of global variable
                is across the module.
                 ->  if we want to define a global variable inside the function, then we have to use a keyword call global
nonlocal variable
"""

var_x = 80 # global variable

def function1():
    global var_A # global variable
    var_y = 90  # local variable
    var_A = 500
    print("global var_x:", var_x)
    print("local var_y :", var_y)

def function2():
    var_z = 100
    print("global var_x:", var_x)
    print("local var_z :", var_z)
    print("Global var_A :", var_A)

#function1()
#print("_"*50)
#function2()

print("_"*50)
########################################################

var_p = 300  # global variable

def outer_function():
    var_q = 400 # nonlocal variable

    def inner_fun1():
        var_r = 500 # local
        print("var p :  global :", var_p)
        print("var q :  non local :", var_q)
        print("var r :  local :", var_r)

    def inner_fun2():
        var_s = 600 # local
        print("var p :  global :", var_p)
        print("var q :  non local :", var_q)
        print("var s :  local :", var_s)


    inner_fun1()
    print("_"*50)
    inner_fun2()

outer_function()






print("_"*50)
########################################################
var_K = 300  # global variable
def outer_function2():
    var_L = 500

    def inner_fun1():
        var_r = 500 # local
        print("var K :  global :", var_K)
        print("var L :  non local :", var_L)
        print("var r :  local :", var_r)

    def inner_fun2():
        global var_K
        nonlocal var_L
        var_s = 600 # local
        var_K = 1000
        var_L = 2000
        print("var K :  global :", var_K)
        print("var L :  non local :", var_L)
        print("var s :  local :", var_s)


    inner_fun1()
    print("_"*50)
    inner_fun2()
    print("_" * 50)
    inner_fun1()

print("_"*50)
outer_function2()