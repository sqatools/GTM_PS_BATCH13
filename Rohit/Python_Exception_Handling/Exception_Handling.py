def exception_handling():
    try:
        a= 10
        b=20
        print("Addition result :",a+b)
    except Exception as e:
        print(e)  # Addition result : 30

exception_handling()

print("-"*50)
def exception_handling2():
    try:
        a= 20
        b="Python"
        print("Addition :",a+b)
    except Exception as e:
        print(e) # unsupported operand type(s) for +: 'int' and 'str'
        print("Int and str are not allowed")  # Int and str are not allowed
exception_handling2()
print("Good Morning")

print("-"*50)
###### raise exception explicitly.  ########
def exception_handling_with_raise(a ,b):
    try:
        print("Addition values :", a+b)
        print("Division values :", a/b)
    except Exception as e:
        print(e)
        print("Int and String not allowed")
        raise

#exception_handling_with_raise(20,30)
#exception_handling_with_raise(20,0)

#Traceback (most recent call last):
#  File "C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\Python_Exception_Handling\Exception_Handling.py", line 35, in <module>
#    exception_handling_with_raise(20,0)
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
#  File "C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\Python_Exception_Handling\Exception_Handling.py", line 28, in exception_handling_with_raise
#    print("Division values :", a/b)
#                              ~^~
#ZeroDivisionError: division by zero

############### try-except-else ################
# else block code only executes when there is no exception

def exception_handling_try_except_else(a,b):
      try:
          print("Addition of value :", a+b)
      except Exception as e:
          print(e)
          print("Int and str are not allowed")
      else:
          print("Code is excuted successfully")

#exception_handling_try_except_else(10,30)

#Addition of value : 40
#Code is excuted successfully

#exception_handling_try_except_else(10,"Hello")
"""
unsupported operand type(s) for +: 'int' and 'str'
Int and str are not allowed
"""

############### try-except-else-finally ################
# else block code only executes when there is no exception
# finally : finally block of code will always execute, if there is exception or no exception.

def exception_handling_try_except_else_finally(a,b,c):
    try:
        print("Addition :", a+b)
    except Exception as e:
        print(e)
        print("Int and str are not allowed")
    else:
        print("code is executed successfully")
    finally:
        # finally block will execute in all condition.
        print("finally result")
        for i in range(1,11):
            print(i,"*",c,"=",i*c)


#exception_handling_try_except_else_finally(10,20,5)
"""
Addition : 30
code is executed successfully
finally result
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
#exception_handling_try_except_else_finally(10,"Hello",2)
'''
unsupported operand type(s) for +: 'int' and 'str'
Int and str are not allowed
finally result
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
6 * 2 = 12
7 * 2 = 14
8 * 2 = 16
9 * 2 = 18
10 * 2 = 20

'''

############### nested level exception ################

def exception_handling_nested_level_exception(a,b,c):
    try:
        print("addition :", a+b)
        try:
            print("division :", b/c)
        except Exception as e2:
            print(e2)
            print("Division with zero is not allowed")
    except Exception as e1:
        print(e1)
        print("Int and str are not allowed")

#exception_handling_nested_level_exception(5,10,0)
'''
addition : 15
division by zero
Division with zero is not allowed
'''
##################  Handle multiple Exception ###############
def handle_multiple_exception(a,b,c,d,e=5):
    try:
        print("addition :", a+b)
        print("division :", b/c)
        assert c == d, "values are not equal"
        print("Multiplication :", d*e)
   # except TypeError:
      #  print("All input values should be numbers")
    except ZeroDivisionError:
        print("can not be divided by zero")
    except AssertionError:
        print("Both values are not equal :",c,d)
    except Exception as e:
        print(e)
        print("Program failed with error")

#handle_multiple_exception(5,'A',10,20) # All input values should be numbers

#handle_multiple_exception(10,20,0,5)
'''
addition : 30
can not be divided by zero
'''

#handle_multiple_exception(10.,20,5,40)
'''
addition : 30.0
division : 4.0
Both values are not equal : 5 40
'''
