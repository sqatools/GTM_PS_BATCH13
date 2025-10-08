a = 10
b = 20
c = a + b
print(c)
print("Value of c is {}".format(c))

#######################################################
x = [10,20,30]
y = x
print(y)
print(x)
y.append(40)
print(y)
print(x)

########### multiple values - multiple variables#############
i,j,h = 10,20,30
print("vale of i is:", i)
print("value of j is:",j)
print("value of h is :", h)
print(i,j,h)
print(j,h,i)

############## Assign one single value to multiple variables ###############
p = q= r = 100
print("value of p is:", p)
print("value of q is:", q)
print("value of r is:", r)
print("value of p:",p,',',"value of q:",q,',',"value of r:",r)