
print('_'*20)
print('Data Types - 1] Number')

print('Data Types - 1.Number - Integer')

print("_____Integer_______" *40)
 #Integer

num1 = 0
num2 = 23
num3 = 45678909876554678

print ('num1 :',num1, type(num1))
print ('num2 :',num2, type(num2))
print ('num3 :',num3, type(num3))

print('_'*20)
print('Data Types - 1.Number - Float')


print("_____Float_______" *40)

#Float

f1 = 0.0
f2 = 23.30
f3 = 156567.787889

print ('f1 :',f1, type(f1))
print ('f2 :',f2, type(f2))
print ('f3 :',f3, type(f3))

print('_'*20)
print('Data Types - 1.Number - Complex')


print("_____Complex_______" *40)
#Complex

comp1 = 10+20j
comp2 = 60j+50
comp3 = 10*20j
comp4 = 60j*50

print ('comp1 :',comp1, type(comp1))
print ('comp2 :',comp2, type(comp2))
print ('comp3 :',comp3, type(comp3))
print ('comp4 :',comp4, type(comp4))


print('Sequential - String')

s1 = ''
s2 = "Shalaka"
s3 = """ Let the improvement of yourself keep you so busy that you have no time to criticize others."""

print ('s1 :', s1, type(s1))
print ('s2 :', s2, type(s2))
print ('s3 :', s3, type(s3))

print('_'*20)
print('Sequential - Positive & Negative String')

char = "All the best"

print(char[0])
print(char[-4])


print('____'*4,'List Data Type', '____'*4)

list1= [1,2.3,'Hellow', [42,3],(3,7),{'a': 2330},{23,30},True]
print (list1,type(list1))

list2=[30,[5,3],True]
print(list2[-2])
print(list2[-2][1])

# add value to list using append
list2.append(2330)
print('list2', list2)


print('____'*4,'Tuple Data Type', '____'*4)

tup1 =(2,30,'python',[3,6],(2,7),{'a': 345},{23,30},True)

print("tup1 :", type[tup1])

print(tup1[4])
print(tup1[4][1])

print(tup1[-4])
print(tup1[4][-1])


print('____'*4,'Dictionary Data Type', '____'*4)
dict1 = {'a' : 23,'b':30, 'c':2330}
print ('dict1 :', dict1)


print('____'*4,'Set Data Type', '____'*4)
set1 = {3,2.3, 23+30j, 'Hellow',(19,77,92),True}
print('set1:',set1)


print('____'*4,'Boolean Data Type', '____'*4)
bool1 = True
bool2 = False

print ('bool1:', type[bool1])
print ('bool2:', type[bool2])

print(200 == 800)

print(300 == 300)








