def math_operation(n1, n2=20):
    print("n1 :", n1)
    print("n2 :", n2)
    print("addition :", n1+n2)
    print("multiplication :", n1*n2)

# consider default value of n2
math_operation(30)

print("-"*70)
def get_addition_value(num_range):
    sum = 0
    for i in range(num_range):
        print(i)
        if sum >= 20:
            return sum
            #print("hello")  # code is unreachaable
        else:
            sum += i

v1 = get_addition_value(30)
print("v1 :", v1)
