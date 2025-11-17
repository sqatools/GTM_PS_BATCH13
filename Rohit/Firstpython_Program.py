print("Hello World this is my first python program")
print("I have started my python class from 9th of Oct")

result = []
for i in range(1, 21):
    if i % 2 == 0:
        result.append(i)
        print(result)
print("-"*50)

A = [2,3,5,7,9,10]
for i in A:
    if i%2==0:
        print(i)
print("-"*50)
a= 100
b= 200
c= a+b
print(c)

print("sub :",a/b)

print("-"*50)
x,y,z=15,33,42

list1 = ['x','y','z']
list2 =15,33,42
result = dict(zip(list1,list2))
print(result)

list1= [2,4,7,5,8,9,12]
for val in list1:
    if val%2==0:
        print("even number :", val)
    else:
        print("odd number :",val)

list1= [2,4,5,7]
list2 = [3,4,8,9]
list2.extend(list1)
print(list2)

print("-"*50)
#########################################
