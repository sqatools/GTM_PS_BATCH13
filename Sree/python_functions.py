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




print('-'*44)
##  * args param accepts multiple values as param in the function; Gave output: in "tuple" or args Also accept in "tuple"form
def accept_multiple_values(*args):
    print(args)
    for i in args:
        print(i)
accept_multiple_values(7,9.0,'Functions',(6,7,4),[4,6,2],{'Q':876})
print('-'*50)
def add_all(*args):
    Total_sum=0
    for i in args:
        Total_sum +=i
    print("addition total",Total_sum)
add_all(5,10,20,40)

print('-'*50)
def sub(*args):
    total=0
    for i in args:
        total -=i
    print("sub_value:",total)
sub(-10,10,10,2)
print('-'*50)
def mul_val(*args):
    total=1
    for i in args:
        total *=i
    print("mul:",total)
mul_val(5,5,5,5,5)
print('-'*50)
## Average of numbers
def Average_numbers(*args):
    if len(args)==0:
        print("no numbers given:")
    else:
        print("Average:",sum(args)/len(args))
Average_numbers(2,2,2,2,2,)
print('-'*30)
def average_value(*args):
    x=sum(args)/len(args)
    print("ave_val:",int(x))
average_value(2,2,2,2,2,)

print('-'*45)
def addition(a,b,c):
    x=a+b+c
    print(x)
addition(44,30,10)
addition(400,20,60)
def add(a,b,c):
    return(a+b+c)
print("add_val:",add(2,2,2))
add =lambda a,b,c:a+b+c
print("add_total:",add(2,2,2))
print('-'*50)
add=lambda *args: sum(args)
print("sum",add(2,2,2))
print('-'*50)
def multipication(v,m):
    a=v*m
    print('Mul.val',a)
multipication(5,5)
print('-'*50)
sub=lambda x,y: x-y
print("subval:",sub(50,20))
print('-'*50)
#accepting values in "dictionary" -kwargs**-  key value formate:
def user_details(**kwargs):
   # print(kwargs)
   # for k in kwargs.values():
   #for k in kwargs.keys():
  for k, v in kwargs.items(): #items() - Returns key:'value' Pairs
     print(k,":",v)
user_details(firstname="Ram", Lastname="k", phonenumber=123456789)
    #for k,v in kwargs.items():
    # ##kwargs is a dictionary.kwargs → holds all keyword arguments passed to the function.kwargs.items() → returns key–value pairs from that dictionary.
print('-'*45)
##4) Swap key & value
def dict(**kwargs):
    swapped={v:k for k, v in kwargs.items()}
    print(swapped)
dict(a=9,b=10,c=12)  # Because of "kwargs" no need to specify in "" qotations

DATA={'A':20,'B':30,'C':40}
swapped ={v:k for k,v in DATA.items()}
print(swapped)
print('-'*45)









