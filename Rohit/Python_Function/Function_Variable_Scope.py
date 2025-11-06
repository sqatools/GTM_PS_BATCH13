"""
local variable:  variable we declare inside the function is called the local variable
                 ->  local variable scope is limited to the function, can not use outside of the function.
                 ->  we can define global variable inside the function using the global keyword.
global variable :  variable we declare outside of the function is called global variable, the scope of global variable
                is across the module.
                 ->  if we want to define a global variable inside the function, then we have to use a keyword call global
nonlocal variable
"""
var_A = 100 # Global variable
def function1():
    var_B = 200 # Local variable
    print("Global Var :", var_A)
    print("Local Var :", var_B)

function1()
'''
Global Var : 100
Local Var : 200
'''
print("-"*50)
###############################################
var_C = 10  # Global
def function2():
    var_D = 20  # Non Local

    def function3():
        var_E = 30 # Local
        print("Global var_C :", var_C)
        print("local var_E :", var_E)
        print("non local var_D :", var_D)


    function3()
function2()
'''
Global var_C : 10
local var_E : 30
non local var_D : 20
'''
print("-"*50)
#####################################################
var_p = 50
def outer_function():
    var_q = 60
    print("var_q :", var_q)
    print("var_p :", var_p)

    def inner_function1():
        var_s = 70
        print("var_s :", var_s)
        print("var_q :", var_q)
        print("var_p :", var_p)


        def inner_function2():
            global var_t

            var_x = 80
            var_t = 90

            print("global var_x :", var_x)
            print("local var_t :", var_t)
            print("Global var_p :", var_p)
            print("nonlocal var_s :", var_s)

        inner_function2()
    inner_function1()

outer_function()
'''
var_q : 60
var_p : 50
var_s : 70
var_q : 60
var_p : 50
global var_x : 80
local var_t : 90
Global var_p : 50
nonlocal var_s : 70
'''
print("-"*50)
