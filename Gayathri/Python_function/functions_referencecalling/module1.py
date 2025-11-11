#here we are declaring an Global variable and an function'
#here we are doing the declaryion but not calling the function
from xml.dom.expatbuilder import theDOMImplementation


#also remember since var_A is global variable, when calling in any function the variable has to be declared
#first before calling them - else will get error
#like below - if addition is called before the var_A is declared below - we get this error
#name 'var_A' is not defined. Did you mean: 'vars'?
def addition(n1, n2):
    print("Add:", n1+n2)
    print(var_A)

#addition(40, 50) ->Since we get this error, have commented this sine var_A is declared post calling the function


var_A = 400 #global variable
#addition(40, 50) # now if we call teh function after variable_A declared will have no issues
"""
Add: 90
400
"""

#now we are going to use this method in another module
