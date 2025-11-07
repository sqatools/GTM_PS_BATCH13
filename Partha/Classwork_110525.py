def number_play(*argus):
    print(argus)
    for arg in argus:
        print(arg)
number_play('a', 1, -789, (1,2,3),[1,2,3])


def num_sq(a):
    return a*a
num_pi = 3.14
r = int(input("Enter the radius :"))
print("The area of a circle of radius",r, "is", num_pi*num_sq(r))
print("The perimeter of a circle of radius",r, "is", 2*num_pi*r)