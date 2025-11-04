#Class : 10th Oct 25
"""
1. Numbers:
     i) Integer
     ii) Float
     iii) Complex

2. Sequential
     i)  String
     ii)  List
     iii) Tuple

3. Dictionary
4. Set
5. Boolean
"""

######################### Integer #########################
"""
# Integer :  Properties
1.  Integer is immutable data type - It can hold only one value, e.x if i had 100 rs first , then again i get 200 rs
then latest value will be considered i.e 200
2.  Integer only contains whole number.
3.  There is no range limit for integer
"""

num1 = 0
num2 = 400
num3 = 543543534543543543543545543

print("num1 :", num1, type(num1))  # num1 : 0 <class 'int'>
print("num2 :", num2,  type(num2)) # num2 : 400 <class 'int'>
print("num3 :", num3,  type(num3)) # num3 : 543543534543543543543545543 <class 'int'>


print("_"*50) #here the __ will be repeated 50 times
######################### Float #########################
"""
# Float :  Properties
1.  Float is immutable data type
2.  Float contains pointer/decimal value.
3.  There is no range limit for Float.
"""

f1 = 0.0
f2 = 56.78
f3 = 7189354435.3454353445678445
print("f1 :", f1, type(f1)) # 0.0 <class 'float'>
print("f2 :", f2, type(f2)) # 56.78 <class 'float'>
print("f3 :", f3, type(f3)) # 7189354435.345435 <class 'float'>


print("_"*50)

######################### Complex #########################
"""
# Complex :  Properties
1.  Complex is immutable data type
2.  Complex number is combination of real and imaginary number e.g. x+yj
3. here j is mandatory and cant replace j with any other character
"""

comp1 = 10 + 20j
# real = 10
# img = 20
comp2 = 0 + 1j
comp3 = 50j


print("comp1", comp1, type(comp1))  # (10+20j) <class 'complex'>
print("real value :", comp1.real) # 10.0
print("imag value :", comp1.imag) # 20.0

print("comp2", comp2, type(comp2))  # 1j <class 'complex'>
print("comp3 :", comp3,  type(comp3)) # comp3 : 50j <class 'complex'>


print("_"*50)