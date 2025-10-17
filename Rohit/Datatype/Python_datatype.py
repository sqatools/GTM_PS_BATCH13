######################### Integer ##########################
num1=0
num2=30
num3=44683738383836682
print("num1:", num1, type(num1)) # num1: 0 <class 'int'> #
print("num2:",num2,type(num2))   # num2: 30 <class 'int'> #
print("num3:",num3,type(num3))   # num3: 44683738383836682 <class 'int'> #

print("-"*50)
######################### Float #########################
f1=0.0
f2=40.45
f3=4793780388.8378373
print("f1:",f1,type(f1)) # f1: 0.0 <class 'float'> #
print("f2:",f2,type(2))  # f2: 40.45 <class 'int'>  #
print("f3:",f3,type(f3))  # f3: 4793780388.837837 <class 'float'> #

print("-"*50)
######################### Complex #########################
comp1=0+0j
comp2=23+12j
comp3= 75j
print("comp1:",comp1,type(comp1)) # comp1: 0j <class 'complex'> #
print("comp2:",comp2,type(comp2)) # comp2: (23+12j) <class 'complex'> #
print("comp3:",comp3,type(comp3)) # comp3: 75j <class 'complex'> #

print("-"*50)
######################### string #########################

s1='Hello Guys'
s2=""
s3="""
Started learning python programming language with AI from 9th oct 2025

"""
s4='''
Automation testing for python written programming language to learn

'''

print("s1:",s1,type(s1))
print("s2:",s2,type(s2))
print("s3:",s3,type(s3))
print("s4:",s4,type(s4))

s5= "Mumbai"

"""
 0   1   2   3   4  5     +ve indexing
 M   u   m   b   a  i
-6   -5 -4  -3  -2  -1    -ve indexing
"""
print(s5[4])  # a
print(s5[-3]) # b

print("-"*50)
#################################### List ###########################

list1=[1,23.45,1+3j,"Hello",{'a:',45},True]
print(list1,type(list1))

print("-"*50)
#################################### Tuple ###########################

tup1=(0,23,22.90,45+5j,'String value',{'a':34},False)
print(tup1,type(tup1))

print("-"*50)
#################################### dictionary ###########################

dict1={'a':222,'b':333,'c':444}
print(dict1,type(dict1))

print("-"*50)
#################################### set ###########################

set1={1,34.09,'Hello string',(6,9,7),True}
print(set1,type(set1))

print("-"*50)
#################################### Boolean ###########################
val1= True
val2= False
print(val1,type(val1))  # True <class 'bool'> #
print(val2,type(val2))  # False <class 'bool'> #

val1=50
val2=40
val3=50
print(val1==val2) # False #
print(val1==val3) # True #

print("-"*50)
##########################################################################