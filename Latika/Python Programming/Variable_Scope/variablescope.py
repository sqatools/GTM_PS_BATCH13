"""
Global variable
Local variable
non local variable
"""

var_g=80

def function1():
    var_l=90
    print("Global var_g is",var_g)
    print("Local var_l is",var_l)

function1()

def function2():
    var_l2=100
    print(var_l2)
    print(var_g)
    #var_l can not access here

function2()

##################################################3

var_p=300

def outer_function1():
    var_q=400                                                      #non-local variable

    def inner_func1():
        var_r= 500                                                  #local variable

        print("global variable",var_p)
        print("non local variable",var_q)
        print("local variable",var_r)

    inner_func1()
outer_function1()