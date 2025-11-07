def addition_values(x, y):             #defining a function_name() pass parameters
    """
    This function will provide addition of x and y
    :param x: first parameter
    :param y: second parameter
    :return:v
    """
    result=x +y
    print(result) # Need to call fuction(addition_values) then only it print
addition_values(10,20)           # 1.Pass  value to the parameter . Here we are passing values directly to the function

addition_values(500,400)

# There r 2 ways to pass param to the function:
#2. pass by reference: Need to take reference by another "variable"
#for example:
a=80
b=60
addition_values(a,b)  # throws error if we don't provide required parameter
def multiplication_value(x,y):
   result=x * y
   print('mul value:',result)
multiplication_value(30,22)
multiplication_value(430,222)
def division(a,b):
    #result=a/b
    print('division value:',a*b)
division(33, 33)
#  pass by reference:
c=44
d=34
def sub(c,d):
    result= c-d
    print("sub value",result)
sub(c,d)
print('-'*44)
def x(a,b):
    result= a%b
    print('%value:',result)
x(15,3)
print('-'*44)
#Function with Default parameter
def mathoperation(a,b=20):  # default value is always right side-Non default follows default value
    print('a:',a)
    print('b:',b)
    print('add value:',a+b)
    print('sub:',a-b)
    print('div:',a/b)
mathoperation(50)
print('-'*44)
#Override default value of "b"
mathoperation(50,70)
print('-'*44)
#function with return statement








