# *args accept any type of data

def accept_multiple_values(*args):
    print(args)
    for val in (args):
        print(val)

accept_multiple_values(3,5.0,'Hello')

# **kwargs param accept values in key value format.

def user_details(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,':',v)
user_details(first_name='Mohit',Last_Name='Patil',age=30,DOB={'ddate':20,'month':12,'year':2025})