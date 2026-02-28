def handle_exception():
    try:
        a=10
        b='Functions'
        print('1.','Addition:',a+b)
    except Exception as e:          ##except=built in  Exception is a Class

        print('2.',e)
        print('3',"Addition of int and string is not allowed")

handle_exception()
print('4.','The next print statement is printed')
###### raise exception explicitly.  ########
def handle_exception_raise():
    try:
        a=10
        b='Functions'
        print('5.','Addition:',a+b)
    except TypeError:

        print('6.',e)
        print('7.',"Addition of int and string is not allowed")
        raise
handle_exception_raise()
print('-'*45)


