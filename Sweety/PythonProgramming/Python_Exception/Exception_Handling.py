def handle_exception():
    try:
        a = 10
        b = "Hello"
        print("Addition: ", a+b)
    except Exception as e:
        print(e)
        print("addition of two strings not allowed")


#handle_exception()
#print("Good Morning")

###### raise exception explicitly.  ########

def handle_exception_with_raise(a, b):
    try:
        print("Addition:", a+b)
        print("Mul:", a*b)
    except Exception as e:
        print(e)
        raise

#handle_exception_with_raise("jsk", "dafgd")

#print("Hi")


#Addition: jskdafgd
#can't multiply sequence by non-int of type 'str'
#Traceback (most recent call last):
# File "C:\PythonAutomation\GTM_PS_BATCH13\Sweety\PythonProgramming\Python_Exception\Exception_Handling.py", line 24, in <module>
#    handle_exception_with_raise("jsk", "dafgd")
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
#  File "C:\PythonAutomation\GTM_PS_BATCH13\Sweety\PythonProgramming\Python_Exception\Exception_Handling.py", line 19, in handle_exception_with_raise
#    print("Mul:", a*b)
#                  ~^~
#TypeError: can't multiply sequence by non-int of type 'str'

############### try-except-else ################
# else block code only executes when there is no exception

def handle_exception_try_except_else(a, b):
    try:
        print("Addition:", a+b)
    except Exception as e:
        print(e)
        print("Addition of int and string is not allowed")
    else:
        # else block of code will not execute if there is exception
        print("Code execution is successful")

        # handle_exception_try_except_else(10, 20)
        # Addition: 30
        # Code execution is successful

        # handle_exception_try_except_else(10, 'Hello')
        """
        unsupported operand type(s) for +: 'int' and 'str'
        Addition of int and string is not allowed
        """

############### try-except-else-finally ################
# else block code only executes when there is no exception
# finally : finally block of code will always execute, if there is exception or no exception.

def handle_exception_try_except_else_finally(a, b, c):
    try:
        print("Addition:", a+b)
    except Exception as e:
        print(e)
        print("Addition of int and string is not allowed")
    else:
        # else block of code will not execute if there is exception
        print("Code execution is successful")

    finally:
        # finally block will execute in all condition.
        print("------ Finally block --------")
        for i in range(1, 11):
            print(i,"*", c, "=", i*c)



#handle_exception_try_except_else_finally(10, 40, 5)
"""
Addition: 50
Code execution is successful
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50


"""

#handle_exception_try_except_else_finally(10, 'Python', 5)
"""
unsupported operand type(s) for +: 'int' and 'str'
Addition of int and string is not allowed
------ Finally block --------
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
"""


def handle_nested_level_exception(a, b, c):
    # outer exception block
    try:
        print("Addition:", a+b)
        try:
            # inner exception block
            div = b//c
            print("division :", div)
        except Exception as e2 :
            print(e2)
            print("Division with zero is not allowed")
    except Exception as e1:
        print(e1)
        print("Addition of int and string is not allowed")


#handle_nested_level_exception(10, 'H', 20)
"""
# got outer exception

unsupported operand type(s) for +: 'int' and 'str'
Addition of int and string is not allowed
"""

#handle_nested_level_exception(10, 15, 0)
"""
# inner exception:
Addition: 25
integer division or modulo by zero
Division with zero is not allowed

"""

##################  Handle multiple Exception ###############
def handle_multiple_exception(a, b, c, d, e=10):
    try:
        print("Addition:", a+b)
        print("Division :", a//c)
        assert c == d, "values are not equal"
        multiplication = d*e
    except TypeError:
        print("All input values should be number")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except AssertionError:
        print("Both values are not equal:", c, d)
    except Exception as e:
        print(e)
        print("Program failed with error")

# handle_multiple_exception(10, 'A', 20, 30)
# All input values should be number


#handle_multiple_exception(10, 30, 0, 30)
"""
Addition: 40
Can not divide number with zero
"""
#handle_multiple_exception(10, 30, 2,5)
"""
Addition: 40
Division : 5
Both values are not equal: 2 5
"""

handle_multiple_exception(10, 30, 2, 2, {'a': 123})


