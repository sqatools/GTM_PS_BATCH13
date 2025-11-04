##Class - 1 Variables- 08-10-2025
a = 10
b = 20
c = a + b
print(c)
print("Value of c is {}".format(c)) # Value of c is 30

#######################################################
x = [10,20,30]
y = x
print(y)
print(x)
print("id of x is:",id(x))  # id of x is: 1745762951616
print("id of y is:",id(y))  # id of y is: 1745762951616
y.append(40)
print(y)  # [10, 20, 30, 40]
print(x)  # [10, 20, 30, 40]

########### multiple values - multiple variables#############
i,j,h = 10,20,30
print("vale of i is:", i)  # vale of i is: 10
print("value of j is:",j)  # value of j is: 20
print("value of h is :", h) # value of h is : 30
print(i,j,h)  # 10 20 30
print(j,h,i)  # 20 30 10

############## Assign one single value to multiple variables ###############
p = q= r = 100
print("value of p is:", p)  # value of p is: 100
print("value of q is:", q)   #value of q is: 100
print("value of r is:", r)  #value of r is: 100
print("value of p:",p,',',"value of q:",q,',',"value of r:",r) #value of p: 100 , value of q: 100 , value of r: 100

#################if value of variables are same, they share same memory/address ###############
l= 50
m = 100
n = 50
print("id of l is :",id(l)) #id of l is : 140722181274056
print("id of m is :",id(m)) # id of l is : 140722181274056
print("id of n is :",id(n)) # id of n is : 140722181274056

