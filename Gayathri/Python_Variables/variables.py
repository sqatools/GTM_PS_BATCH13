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
print("id of x is:",id(x))
print("id of y is:",id(y))
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

#################if value of variables are same, they share same memory/address ###############
l= 50
m = 100
n = 50
print("id of l is :",id(l)) #id of l is : 140722181274056
print("id of m is :",id(m)) # id of l is : 140722181274056
print("id of n is :",id(n)) # id of n is : 140722181274056

