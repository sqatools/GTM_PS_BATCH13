print("Write a program to get all the even value from list")
print("."*100)

list1=[3,8,10,7,12]
output=[]
for i in list1:
    if i%2==0:
        output.append(i)
    else:
        continue
print("Even values are: ",output)
#.....................................................................................................
print()
print("Solve above even program with list comprehensive")

result=[x for x in list1 if x%2==0]
print("result is:",result)

#......................................................................................................

print()
print("Write a python to get all the required output values from list")

list2=[4,7,9,12,13]
output1=[]

for val in list2:
    if val%2==0:
        output1.append((val,"even"))
    else:
        output1.append((val,"odd"))
print(output1)

#..........................................................................................
print()
print("with list compr")

result2=[(y,'even') if y%2==0 else (y,'odd') for y in list2]
print(result2)

