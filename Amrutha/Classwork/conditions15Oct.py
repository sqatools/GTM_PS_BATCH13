# write a program to compare 3 values and find the greater value

a=80
b=50
c=50

if a>b and a>c:
    print('A is greater value: ', a)
elif b>a and b>c:
    print('C is greater value: ',b)
elif c<a and c<b:
    print('B is greater value: ',c)
else:
    print('No value is greater')