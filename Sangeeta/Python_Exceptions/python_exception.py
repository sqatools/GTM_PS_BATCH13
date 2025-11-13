
def handle_exception():
    try:
        a = 10
        b = 'Hello'
        print("Addition :", a+b)
    except Exception as e:
        print(e)
        print("Addition of int and string is not allowed")
handle_exception()
print("Good Morning")
#The above code will throw error without try and exception

# raise exception explicitly

def handle_exception_with_raise(a, b):
    try:
        print("Addition :", a+b)
    except Exception as e:
        print(e)
        print("Addition of int and string is not allowed")
        handle_exception_with_raise()

handle_exception_with_raise(10, 'h')
print("Good Morning")

## try-except-else####
#else block will execute when exception is not there

def handle_exception_try_except_else(a, b):
    try:
        print("Addition :", a+b)
    except Exception as e:
        print(e)
        print("Addition of int and string is not allowed")
    else:
        #else block won't execute if thre is exception
        print("Code execution is successful")

handle_exception_try_except_else(10, 20)

###try-except-else-finally###
# else block code executes when thereis no exception
#finally block of code will always execute, if there is execution of no exception.

def handle_exception_try_except_else_finally(a, b, c):
    try:
        print("Addition :", a+b)
    except Exception as e:
        print(e)
        print("Addition of int and string is not allowed")
    else:
        #else block won't execute if thre is exception
        print("Code execution is successful")

    finally:
        # this block will execution in all condition
        for i in range(1,11):
            print(i,"*",c,"c", i*c)

#handle_exception_try_except_else_finally(10, 40, 5)
handle_exception_try_except_else_finally(10, 'Python', 5)

###nested exception###

def handle_nested_exception(a, b, c):
    try:
        print("Addition :", a+b)
        try:
            div = b//c
            print("division :", div)
        except Exception as e2:
            print(e2)
            print("Division with zero is not allowed")
    except Exception as e1:
        print(e1)
        print("Addition of int and string is not allowed")

handle_nested_exception(10,'H',20) # get outer exception
handle_nested_exception(10,15,0) #get inner exception

### Handle multiple exception####

def handle_multiple_exception(a, b, c, d):
    try:
        print("Addition :", a+b)
        print("Division :", a//c)
        assert c == d, "values are not equal"
    except TypeError:
        print("All input values should be number")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except AssertionError:
        print("Both values are not equal", c,d)
    except Exception as e:
        print(e)
        print("Program failed with error")

handle_multiple_exception(10,'A', 20,30)
# This will give TypeError. All input values should be number
handle_multiple_exception(10,30,0,30)
#This will give ZeroError
handle_multiple_exception(10,40, 20,30)
#This will give AssertionError
handle_multiple_exception(10,40, 2, 2, 'Programming')