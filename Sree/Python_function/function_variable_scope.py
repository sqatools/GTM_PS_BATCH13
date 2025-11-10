"""
Local variable - variable v declare inside the function-Scope: limited to that function
global variable -declare outside the function_ scope: accros the module. -if we want to define a global variable inside the function, then we have to use a keyword call global- must call the first fuction1(If we gave the golbal variable in function1, then only will result for funcion2
Non local variable
"""
gol_va=90
def function1():
    loc_val=20
    print('Glovar:',gol_va)
    print('Locvar:',loc_val)
function1()
def function2():
    print(gol_va)
function2()
print('-'*44)
def function3():
    loc_val=20
    global var_A
    var_A=300
    print('Glovar:',var_A)
    print('Locvar:',loc_val)
    print('globalvar:',gol_va )
function3()
print('-'*44)  #Nonlocal variable
print('-'*44)
Var_a =100   # Global Variable
def outer_fun():
    Var_b=300                 #Non local
    def inner_fun1():
       Var_c = 200  # Local vriable
       print('fun1',Var_a)
       print('fun1',Var_b)
       print('fun1',Var_c)

    def inner_fun2():
        Var_d=20
        print('fun2',Var_a)
        print('fun2',Var_b)
        print('fun2',Var_d)

    inner_fun1()
    inner_fun2()
outer_fun()




