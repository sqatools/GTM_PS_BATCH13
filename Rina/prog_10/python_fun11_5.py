var_x = 100
def function1():
    global var_A
    var_y = 90
    var_A = 50
    print("global var_x :", var_x)
    print("local var_Y :", var_y)
    print("local var_A :", var_A)

function1()


def function2():
    var_B = 45
    print("global var: ", var_x)
    print("local var: ", var_B)
    print("global var: ", var_A)