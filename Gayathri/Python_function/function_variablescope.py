"""
local variable:  variable we declare inside the function is called the local variable
                 ->  local variable scope is limited to the function, can not use outside of the function.
                 ->  we can define global variable inside the function using the global keyword.
global variable :  variable we declare outside of the function is called global variable, the scope of global variable
                is across the module.
                 ->  if we want to define a global variable inside the function, then we have to use a keyword call global
nonlocal variable ->In nested loop, the variable declared in outermost loop is called nonlocal varaible
                    ->This variable scope is inside the outer lopp and also inside the loops declared from the outerloop
                ->to override the global variable anywhere - first define the varibale, global var_x
                and then initiate the value
                ->to override the nonlocal varaible -> declare the variable ->nonlocal var_y
                and then initiate the value
"""

var_x = 80 # global variable, declared outside the function

def function1():
    global var_A # global variable, Inside the function declaring the global variable using the keyword
    var_A= 500 #initiating the value for the global vriable
    var_y = 90  # local variable
    print("global var_x:", var_x) #80
    print("local var_y :", var_y) #90
    print("global var_A :", var_A) #500


def function2():
    var_z = 100  #local varaible
    print("global var_x:", var_x) #80
    print("local var_z :", var_z)  #100
    print("Global var_A :", var_A)  #500 since its global can be accessed in any functions

function1()
print("_"*50)
function2()

print("_"*50)
########################################################

var_p = 300  # global variable

def outer_function():
    var_q = 400 # nonlocal variable, since its outermost loop

    def inner_fun1():
        var_r = 500 # local variable
        print("var p :  global :", var_p) #300
        print("var q :  non local :", var_q) #400
        print("var r :  local :", var_r) #500

    def inner_fun2():
        var_s = 600 # local variable
        print("var p :  global :", var_p)  #300
        print("var q :  non local :", var_q) #400
        print("var s :  local :", var_s) #600


    inner_fun1()
    print("_"*50)
    inner_fun2()

outer_function() #doesnt have any print stataments
print("_"*50)
########################################################
var_K = 300  # global variable
def outer_function2():
    var_L = 500  #non local varaiable

    def inner_fun1():
        var_r = 500 # local variable
        print("var K :  global :", var_K) #300
        print("var L :  non local :", var_L) #500
        print("var r :  local :", var_r) #500

    def inner_fun2():
        global var_K #here we are overriding the global varaible value, so first declare the variable
        var_K = 1000 #then initiate the value

        nonlocal var_L #here we are overriding the nonlocal varaible value, so first declare the variable
        var_s = 600 #then initiate the value

        var_L = 2000  #local variable
        print("var K :  global :", var_K) #1000
        print("var L :  non local :", var_L)  #600
        print("var s :  local :", var_s) #600


    inner_fun1() #here the gobal variable value will be the ones which were declafed first and not modified values
    #as modified values are in inner_fun2() which is not called first
    print("_"*50)
    inner_fun2() #here the values for global and non local has been changed, so it prints those changed values
    print("_" * 50)
    inner_fun1() #now again when we call inner_func1, since fun2 is alrady executed, now it takes the latest
    #value which were changed

print("_"*50)
outer_function2() # no print statments

"""
__________________________________________________
var K :  global : 300  ->This is inner_fun1, with no latest value
var L :  non local : 500
var r :  local : 500
__________________________________________________
var K :  global : 1000 ->This is inner_fun2 - with modified values
var L :  non local : 2000
var s :  local : 600
__________________________________________________
var K :  global : 1000 ->This is again inner_fun1 ->willtake the latest modified value
var L :  non local : 2000
var r :  local : 500
"""