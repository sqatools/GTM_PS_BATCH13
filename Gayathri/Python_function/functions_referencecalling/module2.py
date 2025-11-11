# import everything from module1
from module1 import *
#if we give * that meands all teh variables,methods defined all will be imported

#now lets add another module 3
#if we want to import sepcifc methods or global variables - define them alone
#module 3 - has 2 functions, multiply and divide outof whoich we are calling only 1
from module3 import multiply, var_A



print(var_A**2) #since this is global variable
addition(40, 50) #function defined in module 1
"""
160000
Add: 90
400
"""

#from module - 3
multiply(4, 5)
#division() # we cant call - we get error as its not imported

print("var_A :", var_A) # to see which value it takes
#first module1 is imported with * - so A = 400
#again then we are importing module 3, where A = 500
#so it takes latest value i.e 500

"""
250000, SInce A is 500
Add: 90
400 -Here A is 400, as its inside module 1 - function
Multiply: 20
var_A : 500

"""

