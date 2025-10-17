##Prime number or not
# prime number is divisble by 1 or itself

num = 13
prime = True

for i in range(2, num):
    print(i)
    if num % i == 0:
        prime = False
    else:
        continue
        if prime == True:
            print("This is prime number :", num)
        else:
            print("this is not a prime number:", num)

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")  # print stars on same line
    print()


    ##reverse patter

    for i in range(5, 0, -1):
        for j in range (1, i + 1):
            print ("*", end="")
            print()

    
