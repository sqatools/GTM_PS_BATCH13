"""
local variable:  variable we declare inside the function is called the local variable
                 ->  local variable scope is limited to the function, can not use outside of the function.
                 ->  we can define global variable inside the function using the global keyword.
global variable :  variable we declare outside of the function is called global variable, the scope of global variable
                is across the module.
                 ->  if we want to define a global variable inside the function, then we have to use a keyword call global
nonlocal variable
"""
var_x=100 #global
def function1():
    var_a=200 #local
    var_b=300
    print("global var_x:", var_x)
    print("local var_a:", var_a)
    print("local var_b :", var_b)
function1()

