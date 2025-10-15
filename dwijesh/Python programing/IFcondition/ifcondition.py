a=100
b=101
c=102
d=103

if a==b==c:
    print("pass")
else:
    print("fail")

print ("_"*50)
####################################

if \
        a == b:
    print("pass")
elif b == c:
    print("pass")
elif c == a:
    print("pass")
else:
    print("fail")
print ("_"*50)
####################################
if a==b:
  print("paas")
  if b==c:
      print("paas")
      if c==a:
          print("paas")
      else:
          print("fail")
  else:
      print("fail")
else:
    print("fail")
#######################################

a=input("enter a value")
b=input("enter b value")
c=input("enter c value")
a1=int(a)
b1=int(b)
c1=int(c)


if a1%2 == 0 and a1%1 == 0:
    print("statement1")
elif b1%3==0 or c1%4 == 0:
    print("statement2")
elif c1>=1 and b1<=2:
     print("statement3")
elif a1!=0 and b1==1:
    print("statement4")
else :
     print("You are perfect")

print("-"*50)

listone=[1,2,3,4,5,6,7,8,9]
num=input("enter the value")

if num in listone:
    print("num is good")
    if num not in listone:
        print("nim is ok ")
    else:
        print("num is fine")
else:
    print("num is not good")




















