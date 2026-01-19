# one line if statement

var1=13
result = "even" if var1%2 == 0 else"odd"
print("result;",result) # result:even


#write a python program to check given number is divible 3,5,7

x = 15

if x%3 == 0:
    print("x is divible by 3",x)
elif x%5 == 0:
    print("x is divible by 5",x)
elif x%7 == 0:
    print("x is diviable by 7",x)
else:
    print("x is not divible by any number",x)


#######################
("_"*40)

age =20

print("Eligible for voting") if age>=18 else print ("Not eligible for voting")