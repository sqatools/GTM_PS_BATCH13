#while executing scripts - if there is any error in between the code
#the program terminates in bewteen as it has encounterred the error

#with execption handling -we can show that error to the user and program will not terminate in
#bewteen but it will proceed further code execution

#in case want to customize the errors -with your own message - that is  done in exception handling

# a = 10
# b = "hello"
# print("Addition is:", a + b)
# #it throws error ->TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# print("Good Morning")

#what happenewd above was line - 11 - it throws error - so line 14 wont get executed

#Now above lines let me comment

def handle_exception():
    try:
        a = 10
        b = "hello"
        print("Addition is:", a + b)
    except Exception as e:
        print(e)  #unsupported operand type(s) for +: 'int' and 'str'
        print("Addition of integer and string is not allowed") # customized message
        #Exception - class

handle_exception()
print("Good Morning")

print("*"*50)
#try except will not handle - Logical error

###### raise exception explicitly.  ########
"""
raise:
The raise keyword is used to explicitly trigger an exception.
This can be a built-in exception (like ValueError, TypeError, ZeroDivisionError) or a
 custom exception defined by the programmer.
raise is typically used when a specific condition or invalid state is detected within the code, 
and an error needs to be signaled to the calling code.
When raise is encountered, the normal flow of execution is interrupted, and Python searches for 
an appropriate except block to handle the raised exception. If no matching except block is found in the current scope or any calling scopes, the program will terminate with an unhandled exception.
"""

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 2)
    print(f"Result: {result}")

    result_error = divide(5, 0)
    print(f"Result with error: {result_error}") # This line will not be reached
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")
except TypeError:
    print("Caught a TypeError!")
else:
    print("No exceptions occurred in the try block.")
finally:
    print("This will always execute.")

print("*"*50)
##########################################################################################

# def handle_exception_with_raise(a, b):
#     try:
#         print("Addition:", a+b)
#         print("division :", a//b)
#     except Exception as e:
#         print(e)
#         print("Addition of int and string is not allowed")
#         raise
#
# handle_exception_with_raise(10, 20)  #Addition: 30, division : 0
# handle_exception_with_raise(10,0)
# """
# Traceback (most recent call last):
#   File "C:\Users\Sriram\PycharmProjects\GTM_PS_BATCH13\Gayathri\Python_Exception\python_exception.py", line 81, in <module>
#     handle_exception_with_raise(10,0)
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
#   File "C:\Users\Sriram\PycharmProjects\GTM_PS_BATCH13\Gayathri\Python_Exception\python_exception.py", line 74, in handle_exception_with_raise
#     print("division :", a//b)
#                         ~^^~
# ZeroDivisionError: integer division or modulo by zero
# """

print("*"*50)
###########################################################################################
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
        print("Else Code block execution is successful")

#handle_exception_try_except_else(10, 20)
#Addition: 30
#Else Code block execution is successful

#handle_exception_try_except_else(10, 'Hello') #else block not executed
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
        print("else Code blobk execution is successful")

    finally:
        # finally block will execute in all condition.
        print("------ Finally block --------")
        for i in range(1, 11): #print table of any
            print(i,"*", c, "=", i*c)

handle_exception_try_except_else_finally(10, 40, 5)

"""
Addition: 50
else Code blobk execution is successful
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

handle_exception_try_except_else_finally(10, 'Python', 5)

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

print("*"*50)
#####################################################################
#############Nested Exceptions###########################
#have an exception inside an exception
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
# got outer exception - bcz it starts from outer exception
whne there is error in outer try block - it wont go to inner block of try- so it stops there

unsupported operand type(s) for +: 'int' and 'str'
Addition of int and string is not allowed
"""

handle_nested_level_exception(10, 15, 0)
"""
# inner exception:
Addition: 25 - here bcz outer block is cleared 
integer division or modulo by zero
Division with zero is not allowed

"""
print("*"*50)
##################  Handle multiple Exception ###############
def handle_multiple_exception(a, b, c, d, e=10):
    try:
        print("Addition:", a+b)
        print("Division :", a//c)
        assert c == d, "values are not equal"
        multiplication = d*e
    #except TypeError:
        #print("All input values should be number")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except AssertionError:
        print("Both values are not equal:", c, d)
    except Exception as e:
        print(e)
        print("Program failed with error")

#handle_multiple_exception(10, 'A', 20, 30)
#All input values should be number -
# so what happens is it executes line 214 - print("Addition:", a+b) - since it fails
#it wont execute further lines and check if ther is an exception for same and throws it

#handle_multiple_exception(10, 30, 0, 30)
#Addition: 40, Can not divide number with zero

#handle_multiple_exception(10, 30, 2,5)
#Addition: 40, Division : 5, Both values are not equal: 2 5

handle_multiple_exception(10, 30, 2, 2, {'a': 123})
#Addition: 40, Division : 5, All input values should be number