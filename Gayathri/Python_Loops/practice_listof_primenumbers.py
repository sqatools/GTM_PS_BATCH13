#write a program to get list of prime numbers from 1- 100 and print it

for num in range(1,101):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    if prime: #since we are exepcting this to be true
    #if prime is True #another way of defining
        print("prime number is :",num)
    else: #this might not be required
        pass


