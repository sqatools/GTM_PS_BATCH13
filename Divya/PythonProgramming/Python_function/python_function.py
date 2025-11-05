def addition_values(x,y):
    result = x+y
    print("addition:",result)

def subtraction_values(x,y):
    return x-y

#non default param has to come on the left adn default para, has to come on the right
def math_operation(x,y=10):
    print("x:",x)
    print("y:",y)
    print("addition:",x+y)
    print("multiplication:",x*y)
print("_"*50)
math_operation(20)

v = math_operation(50,20)
print(v)
def get_square(x):
    return x*x
print("_"*50)
def get_cube(x):
    return x*x*x
print("_"*50)

def square_and_cube(num):
    square = get_square(num)
    cube = get_cube(num)
    return square, cube
print("_"*50)

a,b = square_and_cube(100)
print("square of number is:",a)
print("cubed of number is:",b)