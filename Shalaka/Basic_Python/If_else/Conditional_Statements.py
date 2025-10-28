print('_'*5, "if condition", '_'*5)
a =23
b= 30
print(a==b)
if a==b:
    print('both number are euqal')
else:
    print('number are not equals')

print("1.Find the given number is even or odd")

num1=1977

if num1%2 ==0:
     print('Given number is even :', num1)
else:
     print('Given number is odd :', num1)


print('_'*5, "elif condition", '_'*5)
print("2.Find the given number is divisible by 3,5,7")

x= 1990
if x%3 ==0:
    print('Number is divisible by 3:', x)
elif x%5 ==0:
    print('Number is divisible by 5:', x)
elif x%7 ==0:
    print('Number is divisible by 7:', x)
else:
    print('Number is not divisible by any given number:', x)

print('_'*5, "Nested condition", '_'*5)
print("3.Write a program for with nested if condition provide solution for interview process")

round1 = 'pass'
round2 = 'pass'
round3= 'fail'
round4 = 'pass'

if round1 == 'pass':
    print ('First round is clear')

    if round2 == 'pass':
        print('Second round is clear', round2)
    else:
        print('Second round is fail', round2)

        if round3 == 'pass':
            print('Third round is clear', round3)
        else:
            print('Third round is fail', round3)
            if round4 == 'pass':
                print('Fourth round is clear', round4)
            else:
                print('Fourth round is fail', round4)
else:
    print ('Round 1 is fail, Sorry', round1)




print('_'*5, "One line if condition", '_'*5)
print("4.Find the given number is even or odd")
var1 = 23

result ='even' if var1%2 ==0 else 'odd'

print ('number is :', result)


















