for i in range(1,10,1):
    print(i)
print("@"*50)
for i in range(5):
    print(i)

print("@"*50)
# show output with decrement value
for i in range(10, 0, -2):
    print(i)

print("@"*50)
#write program to find the sum of number in the range (1,10)
sum=0
for i in range(1,11):
    sum=sum+1
    #sum+=1
    print("sum:",sum)


# write a python program to print all the value divisible 3 and 5 from 1 to 50:
for i in range(1,50):
    if i%3==0 and i%5==0:
        print(i)
    else:
        pass

