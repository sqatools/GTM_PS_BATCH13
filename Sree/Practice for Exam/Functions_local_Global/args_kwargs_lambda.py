# *args param accepts multiple values as param in the functions.
# args accepts the values in form of tuple
#*args allows a function to accept any number of positional arguments,
# even if you don’t know how many will be passed.
def accept_mut_val(*args):
    print(args)
    for i in args:  # for loop: To access each argument separately
        print(i)
accept_mut_val(3,90,'sree', {'a': 345},[5, 7, 8],4.5)

####  # **kwargs param accepts values in key value format as dict.
def fun(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,':',v)
fun(firstname='Mohit', lastname='Sharma', email='mohit@gmail.com', phone=654565464, DOB={'year':2025, 'month': 5, 'day': 20})