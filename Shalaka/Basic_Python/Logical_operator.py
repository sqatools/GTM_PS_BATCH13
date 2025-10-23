print('_'*5, "And opertator", '_'*5)
a= 50
b= 23
c= 30

if a>b and a>c:
    print ('a is grater',a)
elif b>a and b>c:
    print ('b is grater',b)
elif c>a and c>b:
    print('c is grater', c)



print('_'*5, "No is div by 3 & 5... also take user input", '_'*5)

var1 = input('enter no')
print('var1',type(var1))
num1 = int(var1)
print(num1, type[num1])

print('_'*5, " Use and opertator", '_'*5)
if num1%3 ==0 and num1%5==0:
    print('no is div by 3&5',num1)
else:
    print('no is not div by 3&5')

print('_'*5, " Use OR opertator", '_'*5)

if num1%3 == 0 or num1%5 ==0:
    print('no is div by 3&5',num1)
else:
    print('no is not iv by 3&5',num1)


print('_'*5, " Use 'in' opertator", '_'*5)

list1 = [23,30,19,77,92]
n1 = 30
if n1 in list1:
    print ('n1 is present in list')
else:
    print ('n1 is not present in list')


print('_'*5, " Use 'not in ' opertator", '_'*5)

str1  = "Hello world"
val = 'Shalaka'

if val in str1:
    print ('val is present in list')
else:
    print ('val is not present in list')













